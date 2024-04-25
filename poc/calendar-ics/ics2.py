import requests
import ics
from datetime import datetime

# URL do arquivo ICS
url = 'https://www.bls.gov/schedule/news_release/bls.ics'

# Definir o cabeçalho de usuário para simular uma requisição feita por um navegador comum
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    #'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    #'Sec-Ch-Ua-Platform': 'Windows',
    #'Sec-Fetch-Site': 'cross-site',
    #'Accept-Encoding': 'gzip, deflate, br, zstd',
    #'Sec-Fetch-Dest': 'image',
    #'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    #'Sec-Fetch-Mode': 'no-cors',
    #'Sec-Ch-Ua-Mobile': '?0',
    # ---------------------------------------------------------------------------
    #'Dnt': '1',
    #'Referer': 'https://www.bls.gov/',
    #'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    #'Priority': 'i'
}

# Faz o download do arquivo ICS
response = requests.get(url, headers=headers)
with open('calendario.ics', 'wb') as f:
    f.write(response.content)

# Lista para armazenar os eventos filtrados
eventos = []

# Lê o arquivo ICS e extrai as datas, horários e nomes dos eventos que contenham "Producer Price Index"
with open('calendario.ics', 'r') as f:
    cal = ics.Calendar(f.read())
    for event in cal.events:
        # if 'Producer Price Index' in event.name:
            eventos.append({
                'Data': event.begin.date(),
                'Hora': event.begin.time(),
                'Nome': event.name
            })

# Ordena os eventos pela data e hora
eventos_ordenados = sorted(eventos, key=lambda x: x['Data'])

# Imprime os eventos ordenados com data e hora
for evento in eventos_ordenados:
    print(f"Data e Hora: {evento['Data']} - {evento['Hora']} :: {evento['Nome']}")