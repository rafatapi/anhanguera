import requests
from bs4 import BeautifulSoup
import datetime
import requests
import zipfile
from io import BytesIO
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Função para obter os arquivos XML dentro de um arquivo ZIP
def extract_xml_from_zip(zip_content):
    xml_files = []
    with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
        for file in zip_file.namelist():
            if file.endswith('.xml'):
                xml_files.append(file)
    return xml_files

# Dados do formulário
current_date = datetime.datetime.now().strftime('%d/%m/%Y')
data = {
    'txtLogin': '397DWLESTADO4',
    'txtSenha': 'CVM_20240410',
    'txtData': current_date,
    'txtHora': '00:00',
    'txtAssuntoIPE': 'SIM',
    'txtDocumento': 'ITR'
}

# Realizando a requisição
response = requests.post('http://seguro.bmfbovespa.com.br/rad/download/SolicitaDownload.asp', data=data)

# Parseando a resposta
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('link')

# Criando lista de objetos com os dados dos links
links_list = []
for link in links:

    link_data = {
        'url': link.attrs['url'],
        'Documento': link.attrs['documento'],
        'ccvm': link.attrs['ccvm'],
        'DataRef': link.attrs['dataref'],
        'FrmDtRef': link.attrs['frmdtref'],
        'Situacao': link.attrs['situacao']
    }
    links_list.append(link_data)

# Imprimindo a lista de objetos
for link_data in links_list:
    print(link_data)

# baixa o zip
# Lista para armazenar os arquivos XML de cada link
xml_files_list = []
for link in links_list:
    link_url = link['url']
    link_response = requests.get(link_url)
    zip_content = link_response.content
    xml_files = extract_xml_from_zip(zip_content)
    xml_files_list.append({
        'url': link_url,
        'xml_files': xml_files
    })

# Imprimindo os arquivos XML de cada link
for xml_files_data in xml_files_list:
    print(f'URL: {xml_files_data["url"]}')
    print('Arquivos XML:')
    for xml_file in xml_files_data['xml_files']:
        print(xml_file)
    print('---')    



'http://www.rad.cvm.gov.br/ENETCONSULTA/frmDownloadDocumento.aspx?CodigoInstituicao=1&NumeroSequencialDocumento=136972'