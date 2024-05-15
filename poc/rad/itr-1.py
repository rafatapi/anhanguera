import requests
import xml.etree.ElementTree as ET
import datetime
from HttpHelper import HttpHelper

# Parâmetros
txtLogin = '397DWLRHT'
txtSenha = 'F80FCBF8'

# Função para obter a lista de RAD
def get_rad_list(login, password, documento):
    print(f"Executando POST para documento {documento}")
    data = {
        'txtLogin': login,
        'txtSenha': password,
        'txtData': datetime.datetime.now().strftime('%d/%m/%Y'),
        'txtHora': '00:00',
        'txtAssuntoIPE': 'NAO',
        'txtDocumento': documento
    }
    # Realizando a requisição
    url = "http://seguro.bmfbovespa.com.br/rad/download/SolicitaDownload.asp"
    response_content = HttpHelper.post(url, data)

    # Parseando a resposta
    print(f"Parseando o resultado")
    
    # Convertemos o conteúdo da resposta de bytes para string
    #response_content = response.content.decode('utf-8')
    # Parseamos a string XML
    root = ET.fromstring(response_content)

    # Criando lista de objetos com os dados dos links
    print(f"Percorrendo links")
    links_list = []
    for link in root.findall('Link'):
        link_data = {
            'url': link.get('url'),
            'Documento': link.get('Documento'),
            'DataRef': link.get('DataRef'),
            'Situacao': link.get('Situacao'),
            'ccvm': int(link.get('ccvm'))
        }
        links_list.append(link_data)
    return links_list

# Busca a lista de ITR e DFP
links_itr = get_rad_list(txtLogin, txtSenha, 'ITR')
links_dfp = get_rad_list(txtLogin, txtSenha, 'DFP')

# Junta as duas listas
all_links = links_itr + links_dfp

# Percorre a lista e imprime os itens
for link in all_links:
    print(link)