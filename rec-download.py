#Definindo variáveis
SUA_ACCOUNT_SID = 'sidaccountexemplo'
SEU_AUTH_TOKEN = 'tokenauthexemplo'
 
# importação das bibliotecas necessárias
from twilio.rest import Client
import requests
import os
from datetime import datetime

#Definindo variáveis de conexão - substitua com suas informações de conta Twilio
account_sid = SUA_ACCOUNT_SID
auth_token = SEU_AUTH_TOKEN

# criação do objeto Client do Twilio
client = Client(account_sid, auth_token)
# lista todas as gravações disponíveis
recordings = client.recordings.list()

# percorre a lista de gravações e faz o download de cada uma
for recording in recordings:
    # pega a URL da gravação
    recording_url = recording.media_url
   # faz a requisição para a URL da gravação e recebe a resposta
    response = requests.get(recording_url)
    # obtém a data de criação da gravação no formato yyyyMMdd
    date_created = recording.date_created.strftime("%Y%m%d")
    # cria uma pasta com o nome da data de criação, caso ela ainda não exista
    folder_name = date_created
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    # salva a gravação na pasta com o nome da data de criação e com o SID da gravação como nome do arquivo
    with open(os.path.join(folder_name, f"{recording.sid}.mp3"), "wb") as file:
        file.write(response.content)
        print(f"Gravação {recording.sid} salva com sucesso!")
