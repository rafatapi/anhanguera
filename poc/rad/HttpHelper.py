import requests
import time

class HttpHelper():

    @staticmethod
    def downloadFile(url: str, filename: str, tentativa_max: int = 10) -> bool:
        tentativa_nro = 1
        session = requests.Session()
        while tentativa_nro <= tentativa_max:
            try:
                response = session.get(url, timeout=(5, 15))  # (connect timeout, read timeout)
                if response.status_code == 200:
                    with open(filename, "wb") as zip_file:
                        zip_file.write(response.content)
                    return True
                else:
                    print("Erro ao baixar o arquivo. Status code:", response.status_code)
            except requests.exceptions.RequestException as e:  # Captura todas as exceções relacionadas ao requests
                print(f"Erro de conexão. Tentando baixar o arquivo novamente. Erro: {e}")
            except ConnectionResetError as cre:
                print(f"Erro de reset de conexão. Tentando baixar o arquivo novamente. Erro: {cre}")
            
            tentativa_nro += 1
            time.sleep(5)  # Espera alguns segundos antes da próxima tentativa
        
        print("Não foi possível baixar o arquivo após", tentativa_max, "tentativas.")
        return False
    
    @staticmethod
    def post(url: str, params, tentativa_max: int = 10)->str:
        tentativa_nro = 1
        session = requests.Session()
        while tentativa_nro <= tentativa_max:
            try:
                response = session.post(url,  data=params, timeout=(5, 15))  # (connect timeout, read timeout)
                if response.status_code == 200:
                    return response.content.decode('utf-8')
                else:
                    print("Erro ao baixar o arquivo. Status code:", response.status_code)
            except requests.exceptions.RequestException as e:  # Captura todas as exceções relacionadas ao requests
                print(f"Erro de conexão. Tentando baixar o arquivo novamente. Erro: {e}")
            except ConnectionResetError as cre:
                print(f"Erro de reset de conexão. Tentando baixar o arquivo novamente. Erro: {cre}")
            
            tentativa_nro += 1
            time.sleep(5)  # Espera alguns segundos antes da próxima tentativa
        
        print("Não foi possível baixar o arquivo após", tentativa_max, "tentativas.")
        return False    