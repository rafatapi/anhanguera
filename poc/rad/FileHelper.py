import zipfile
import os

class FileHelper():

    @staticmethod
    def unzip(filename: str, path: str):
        try:
            with zipfile.ZipFile(filename, "r") as zip_ref:
                zip_ref.extractall(path)
        except Exception as e:
            print(f"An error occurred while unzipping the file: {e}")

    @staticmethod
    def list_files(path: str):
        try:
            list_of_files = os.listdir(path)
            for file in list_of_files:
                print(file)
            return list_of_files
        except Exception as e:
            print(f"An error occurred while listing the files: {e}")

    @staticmethod
    def delete_all(diretorio: str) -> None:
        if not os.path.exists(diretorio):
            print(f"O diretório {diretorio} não existe.")
            return
        
        if not os.path.isdir(diretorio):
            print(f"O caminho {diretorio} não é um diretório.")
            return

        # Listando todos os arquivos no diretório
        arquivos = os.listdir(diretorio)
        
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            # Verifica se é um arquivo antes de apagar
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
                print(f"Arquivo apagado: {caminho_arquivo}")
            else:
                print(f"{caminho_arquivo} não é um arquivo, não será apagado.")
                
        print(f"Todos os arquivos no diretório {diretorio} foram apagados.")            


    @staticmethod
    def delete(caminho_arquivo: str) -> bool:
        if not os.path.exists(caminho_arquivo):
            print(f"O arquivo {caminho_arquivo} não existe.")
            return False
        
        if not os.path.isfile(caminho_arquivo):
            print(f"{caminho_arquivo} não é um arquivo.")
            return False

        try:
            os.remove(caminho_arquivo)
            print(f"Arquivo apagado: {caminho_arquivo}")
            return True
        except Exception as e:
            print(f"Erro ao tentar apagar o arquivo {caminho_arquivo}: {e}")
            return False        