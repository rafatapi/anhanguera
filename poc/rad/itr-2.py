import zipfile
import os
import requests
import zipfile
import xml.etree.ElementTree as ET
import time


url = "http://www.rad.cvm.gov.br/ENETCONSULTA/frmDownloadDocumento.aspx?CodigoInstituicao=1&NumeroSequencialDocumento=136972"

# Tenta baixar o arquivo zip
# Número máximo de tentativas
max_attempts = 10
attempts = 1

while attempts <= max_attempts:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("documento.zip", "wb") as zip_file:
                zip_file.write(response.content)
            print("Download completo!")
            break  # Sai do loop quando o download for bem sucedido
        else:
            print("Erro ao baixar o arquivo")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Tentando baixar o arquivo novamente.")
    
    attempts += 1
    time.sleep(5)  # Espera alguns segundos antes da próxima tentativa

if attempts > max_attempts:
    print("Não foi possível baixar o arquivo após", max_attempts, "tentativas.")

# Descompactando o arquivo zip
with zipfile.ZipFile("documento.zip", "r") as zip_ref:
    zip_ref.extractall("arquivos_extraidos")

# Listando os arquivos extraídos
arquivos_extraidos = os.listdir("arquivos_extraidos")
print("Arquivos extraídos:")
for arquivo in arquivos_extraidos:
    print(arquivo)

# Descompactando o arquivo zip
with zipfile.ZipFile("documento.zip", "r") as zip_ref:
    zip_ref.extract("FormularioDemonstracaoFinanceiraITR.xml")
    zip_ref.extract("019640ITR31-03-2024v1.xml")

# Fazendo o parsing do arquivo xml
tree = ET.parse("FormularioDemonstracaoFinanceiraITR.xml")
root = tree.getroot()

# Extraindo as informações desejadas
data_entrega = root.find(".//DataEntrega").text
data_geracao_arquivo = root.find(".//DataGeracaoArquivo").text
numero_versao_documento = root.find(".//NumeroVersaoDocumento").text
numero_versao_literal = root.find(".//NumeroVersaoLiteral").text
indicador_arquivo_valido = root.find(".//IndicadorArquivoValido").text

# Fazendo o parsing do arquivo xml
tree = ET.parse("019640ITR31-03-2024v1.xml")
root = tree.getroot()

razaoSocial = root.find(".//RazaoSocialEmpresa").text
cnpj = root.find(".//CnpjEmpresa").text
tipoEmpresa = root.find(".//TipoEmpresa").text

dataReferencia = root.find(".//DataReferencia").text
dtInicioTrimestreAtual = root.find(".//DtInicioTrimestreAtual").text
dtFimTrimestreAtual = root.find(".//DtFimTrimestreAtual").text

dtInicioExercicioSocialCurso = root.find(".//DtInicioExercicioSocialCurso").text
dtFimExercicioSocialCurso = root.find(".//DtFimExercicioSocialCurso").text
dtInicioExercicioSocialAnterior = root.find(".//DtInicioExercicioSocialAnterior").text
dtFimExercicioSocialAnterior = root.find(".//DtFimExercicioSocialAnterior").text
moeda = root.find(".//Moeda").text
escalaMoeda = root.find(".//EscalaMoeda").text
escalaQtdAcoes = root.find(".//EscalaQtdAcoes").text
tipoDemonstracao = root.find(".//TipoDemonstracao").text
versaoPlanoContas = root.find(".//VersaoPlanoContas").text

print("-------------------------------------------------------------")
print("Informações extraídas:")
print("-------------------------------------------------------------")
print("Razaoo Social:", razaoSocial)
print("CNPJ:", cnpj)
print("Tipo de Empresa:", tipoEmpresa)
print("Data de Entrega:", data_entrega)
print("Data de Geração do Arquivo:", data_geracao_arquivo)
print("Número de Versão do Documento:", numero_versao_documento)
print("Número de Versão Literal:", numero_versao_literal)
print("Indicador de Arquivo Válido:", indicador_arquivo_valido)
print("-------------------------------------------------------------")
print("Trimestre atual:", dtInicioTrimestreAtual," - ",dtFimTrimestreAtual)
print("Exercicio Social Curso:", dtInicioExercicioSocialCurso," - ",dtFimExercicioSocialCurso)
print("Exercicio Social Anterior:", dtInicioExercicioSocialAnterior," - ",dtFimExercicioSocialAnterior)
print("-------------------------------------------------------------")


# Fazendo o parsing do arquivo xml
tree = ET.parse("019640ITR31-03-2024v1.xml")
root = tree.getroot()

# Mapeamento dos códigos e descrições das contas desejadas
codigos_descricoes = {
    "3.01": "Receitas de Intermediação Financeira",
    "3.09": "Conta 3.09",
    "3.09.01": "Subconta da Conta 3.09",
    "3.11": "Conta 3.11",
    "3.11.01": "Subconta da Conta 3.11",
    "3.13": "Conta 3.13"
}

# Extraindo as informações das contas desejadas - individuais
for df_individuais in root.iter("DfIndividuais"):
    for conta in df_individuais.iter("Conta"):
        codigo_conta = conta.find("CodigoConta").text
        if codigo_conta in codigos_descricoes:
            descricao_conta = conta.find("DescricaoConta").text
            trimestre_atual = conta.find("TrimestreAtual").text
            trimestre_anterior = conta.find("TrimestreAnterior").text
            if trimestre_atual != None:
                print("Código da Conta:", codigo_conta)
                print("Descrição da Conta:", descricao_conta)
                print("Trimestre Atual:", trimestre_atual)
                print("Trimestre Anterior:", trimestre_anterior)
                print()

# Extraindo as informações das contas desejadas - consolidados
for df_consolidadas in root.iter("DfConsolidadas"):
    for conta in df_consolidadas.iter("Conta"):
        codigo_conta = conta.find("CodigoConta").text
        if codigo_conta in codigos_descricoes:
            descricao_conta = conta.find("DescricaoConta").text
            trimestre_atual = conta.find("TrimestreAtual").text
            trimestre_anterior = conta.find("TrimestreAnterior").text
            if trimestre_atual != None:
                print("Código da Conta:", codigo_conta)
                print("Descrição da Conta:", descricao_conta)
                print("Trimestre Atual:", trimestre_atual)
                print("Trimestre Anterior:", trimestre_anterior)
                print()  