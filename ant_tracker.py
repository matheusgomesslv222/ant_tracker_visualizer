import threading
import time
import pystray
from PIL import Image, ImageDraw
import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

# Inicializar o Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def monitor_endpoint():
    while True:
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
            if response.status_code == 200:
                dados = response.json()
                salvar_dados_no_firebase(dados)
            else:
                print(f"Erro ao acessar o endpoint: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição: {e}")
        
        time.sleep(10)  
def salvar_dados_no_firebase(dados):
    with open('dados.json', 'r') as f:
        dados_json = json.load(f)
    doc_ref = db.collection(u'dados_endpoint').add(dados_json)
    print("Dados inseridos no Firebase:", dados_json)

def setup_tray_icon():
    try:
        icon_image = Image.open("icone.png")  
    except FileNotFoundError:
        print("Arquivo de ícone não encontrado. Certifique-se de que 'icone.png' está no diretório.")
        icon_image = criar_icone()  
        
    menu = pystray.Menu(pystray.MenuItem('Fechar', quit_app))
    
    icon = pystray.Icon("Monitor App", icon_image, "Monitorando endpoint", menu, on_right_click=right_click_handler)
    
    icon.run()

def right_click_handler(icon, item):
    pass

def criar_icone():
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill="black"
    )
    return image

def quit_app(icon, item):
    print("Encerrando o aplicativo...")
    icon.stop()  
    exit(0)  
threading.Thread(target=monitor_endpoint, daemon=True).start()

setup_tray_icon()
