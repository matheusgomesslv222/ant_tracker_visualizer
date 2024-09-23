 # while True:
    #     try:
    #         # Substitua pela URL que você deseja monitorar
    #         response = requests.get('http://seu-endpoint.local/api')
    #         if response.status_code == 200:
    #             dados = response.json()
    #             salvar_dados_no_firebase(dados)
    #         else:
    #             print(f"Erro: {response.status_code}")
    #     except Exception as e:
    #         print(f"Falha na requisição: {e}")
        
    #     # Aguarda 1 minuto antes de verificar novamente
    #     time.sleep(60)