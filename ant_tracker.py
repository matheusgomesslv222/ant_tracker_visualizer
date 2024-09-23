import threading
import time
import pystray
from PIL import Image, ImageDraw
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar o Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Função que monitora o endpoint (com dados fictícios para teste)
def monitor_endpoint():
    while True:
        try:
            # Dados fictícios simulando resposta de um endpoint
            dados_ficticios = {
                "campo1": "Dado de teste 1",
                "campo2": "Dado de teste 2"
            }
            salvar_dados_no_firebase(dados_ficticios)

        except Exception as e:
            print(f"Falha na requisição: {e}")
        
        # Aguarda 1 minuto antes de verificar novamente
        time.sleep(60)

# Função para salvar os dados no Firebase
def salvar_dados_no_firebase(dados):
    # Adicione os dados no Firestore
    doc_ref = db.collection(u'dados_endpoint').add({
        u'campo1': dados.get('campo1', 'N/A'),
        u'campo2': dados.get('campo2', 'N/A')
    })
    print("Dados fictícios inseridos no Firebase.")

# Função para criar o ícone da bandeja do sistema a partir de um arquivo
def setup_tray_icon():
    try:
        # Carregar o ícone a partir do arquivo
        icon_image = Image.open("icone.png")  # Certifique-se de que o arquivo está no diretório correto
    except FileNotFoundError:
        print("Arquivo de ícone não encontrado. Certifique-se de que 'icone.png' está no diretório.")
        icon_image = criar_icone()  # Usa um ícone padrão se o arquivo não for encontrado
    
    # Criar o menu de contexto com a opção 'Fechar'
    menu = pystray.Menu(pystray.MenuItem('Fechar', quit_app))
    
    # Criar o ícone da bandeja
    icon = pystray.Icon("Monitor App", icon_image, "Monitorando endpoint", menu, on_right_click=right_click_handler)
    
    # Executar o ícone da bandeja
    icon.run()

# Função para lidar com o clique direito no ícone da bandeja
def right_click_handler(icon, item):
    # Implemente o código para lidar com o clique direito aqui
    pass

# Função para desenhar um ícone simples caso não tenha um ícone de arquivo
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

# Função para sair do aplicativo
def quit_app(icon, item):
    print("Encerrando o aplicativo...")
    icon.stop()  # Para o ícone da bandeja
    exit(0)  # Fecha o programa completamente

# Criar uma thread para rodar o monitoramento em segundo plano
threading.Thread(target=monitor_endpoint, daemon=True).start()

# Iniciar o ícone da bandeja do sistema
setup_tray_icon()
