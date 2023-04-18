SUA_ACCOUNT_SID = 'sidaccountexemplo'
SEU_AUTH_TOKEN = 'tokenauthexemplo'
 
from twilio.rest import Client
import requests
import os
from datetime import datetime

# substitua com suas informações de conta Twilio
account_sid = SUA_ACCOUNT_SID
auth_token = SEU_AUTH_TOKEN

client = Client(account_sid, auth_token)

# lista todas as gravações disponíveis
recordings = client.recordings.list()


# percorre a lista de gravações e faz o download de cada uma
for recording in recordings:

    
    recording_url = recording.media_url
    response = requests.get(recording_url)
    date_created = recording.date_created.strftime("%d%m%Y")
    folder_name = date_created
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(os.path.join(folder_name, f"{recording.sid}.mp3"), "wb") as file:
        file.write(response.content)
        print(f"Gravação {recording.sid} salva com sucesso!")
