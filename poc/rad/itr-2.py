import zipfile
import os
import requests
import tempfile
import xml.etree.ElementTree as ET
import time
import re
import sys
import datetime
from HttpHelper import HttpHelper
from FileHelper import FileHelper
from CvmDemonstrativo import CvmDemonstrativo
from CvmDemonstrativoConta import CvmDemonstrativoConta

def toDate(value) -> datetime.date:
    try:
        # Tenta converter a string para um objeto datetime
        data = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        return data
    except ValueError:
        # Se ocorrer um erro de valor, retorna None
        return None
    
def toDateTime(value) -> datetime.datetime:
    try:
        # Tenta converter a string para um objeto datetime
        data = datetime.datetime.fromisoformat(value)
        return data
    except ValueError:
        # Se ocorrer um erro de valor, retorna None
        return None


def get_xml_principal(codigo: int, tipo_arquivo: str, diretorio: str) -> str:
    # Listando os arquivos extraídos
    arquivos_extraidos = os.listdir(diretorio)
    # Definindo o padrão para corresponder ao código + tipo_arquivo e que termina em ".xml"
    padrao = re.compile(rf".*{str(codigo)}{tipo_arquivo}.*\.xml$", re.IGNORECASE)
    
    for arquivo in arquivos_extraidos:
        if padrao.search(arquivo):
            caminho_completo = os.path.join(diretorio, arquivo)
            print(f"Arquivo encontrado [{caminho_completo}]")
            return caminho_completo
    
    print("Arquivo não encontrado!")
    return None

def get_xml_formulario(tipo_demonstrativo: str, diretorio: str) -> str:
    padrao = f"FormularioDemonstracaoFinanceira{tipo_demonstrativo}"
    # Listando os arquivos extraídos
    arquivos_extraidos = os.listdir(diretorio)
    # Definindo o padrão para corresponder ao código + "ITR" e que termina em ".xml"
    padrao = re.compile(rf".*{str(padrao)}.*\.xml$", re.IGNORECASE)
    
    for arquivo in arquivos_extraidos:
        if padrao.search(arquivo):
            caminho_completo = os.path.join(diretorio, arquivo)
            print(f"Arquivo encontrado [{caminho_completo}]")
            return caminho_completo
    
    print("Arquivo não encontrado!")
    return None


# monta o objeto
def build_demonstrativo(xml_principal:str, xml_formulario:str) -> CvmDemonstrativo:
    # ----------------------------------------------------------------------------------------
    # Fazendo o parsing do arquivo xml
    # ----------------------------------------------------------------------------------------
    tree = ET.parse(xml_formulario)
    root = tree.getroot()

    # Extraindo as informações desejadas
    data_entrega = root.find(".//DataEntrega").text
    data_geracao_arquivo = root.find(".//DataGeracaoArquivo").text
    numero_versao_documento = root.find(".//NumeroVersaoDocumento").text
    numero_versao_literal = root.find(".//NumeroVersaoLiteral").text
    indicador_arquivo_valido = root.find(".//IndicadorArquivoValido").text

    # ----------------------------------------------------------------------------------------
    # Fazendo o parsing do arquivo xml
    # ----------------------------------------------------------------------------------------
    tree = ET.parse(xml_principal)
    root = tree.getroot()

    razaoSocial = root.find(".//RazaoSocialEmpresa").text
    paramCodigoCvm = int(root.find(".//CodigoCvm").text)
    cnpjEmpresa = root.find(".//CnpjEmpresa").text
    tipoEmpresa = root.find(".//TipoEmpresa").text

    dataReferencia = root.find(".//DataReferencia").text
    dataInicioTrimestreAtual = root.find(".//DtInicioTrimestreAtual").text
    dataFimTrimestreAtual = root.find(".//DtFimTrimestreAtual").text

    dataInicioExercicioSocialCurso = root.find(".//DtInicioExercicioSocialCurso").text
    dataFimExercicioSocialCurso = root.find(".//DtFimExercicioSocialCurso").text
    dataInicioExercicioSocialAnterior = root.find(".//DtInicioExercicioSocialAnterior").text
    dataFimExercicioSocialAnterior = root.find(".//DtFimExercicioSocialAnterior").text
    moeda = root.find(".//Moeda").text
    escalaMoeda = root.find(".//EscalaMoeda").text
    escalaQtdAcoes = root.find(".//EscalaQtdAcoes").text
    tipoDemonstracao = root.find(".//TipoDemonstracao").text
    versaoPlanoContas = root.find(".//VersaoPlanoContas").text


    demonstrativo = CvmDemonstrativo()
    demonstrativo.cvm = paramCodigoCvm
    demonstrativo.razaoSocial = razaoSocial
    demonstrativo.cnpj = cnpjEmpresa
    demonstrativo.tipoEmpresa = tipoEmpresa
    demonstrativo.tipoDemonstrativo = paramTipoDemonstrativo
    demonstrativo.versaoDocumento = numero_versao_documento
    demonstrativo.versaoLiteral = numero_versao_literal
    demonstrativo.arquivoValido = indicador_arquivo_valido
    demonstrativo.moeda = moeda
    demonstrativo.escalaMoeda = escalaMoeda
    demonstrativo.escalaQtdAcoes = escalaQtdAcoes
    demonstrativo.tipoDemonstracao = tipoDemonstracao
    demonstrativo.versaoPlanoContas = versaoPlanoContas

    demonstrativo.dataArquivoEntrega = toDateTime(data_entrega)
    demonstrativo.dataArquivoGeracao = toDateTime(data_geracao_arquivo)

    demonstrativo.dataTrimestreAtualInicio = toDate(dataInicioTrimestreAtual)
    demonstrativo.dataTrimestreAtualFim = toDate(dataFimTrimestreAtual)

    demonstrativo.dataExercicioSocialAtualInicio = toDate(dataInicioExercicioSocialCurso)
    demonstrativo.dataExercicioSocialAtualFim = toDate(dataFimExercicioSocialCurso)

    demonstrativo.dataExercicioSocialAnteriorInicio = toDate(dataInicioExercicioSocialAnterior)
    demonstrativo.dataExercicioSocialAnteriorFim = toDate(dataFimExercicioSocialAnterior)


    # Extraindo as informações das contas desejadas - individuais
    for df_individuais in root.iter("DfIndividuais"):
        for conta in df_individuais.iter("Conta"):
            codigo_conta = conta.find("CodigoConta").text
            if codigo_conta in paramListOfContas:
                descricao_conta = conta.find("DescricaoConta").text
                valor_atual = conta.find("TrimestreAtual").text
                valor_anterior = conta.find("TrimestreAnterior").text
                if valor_atual != None:

                    # cria a conta
                    conta = CvmDemonstrativoConta()
                    conta.codigo = codigo_conta
                    conta.descricao = descricao_conta
                    conta.valorAtual = valor_atual
                    conta.valorAnterior = valor_anterior

                    # adiciona na lista
                    demonstrativo.addContaIndividual(conta)


    # Extraindo as informações das contas desejadas - consolidados
    for df_consolidadas in root.iter("DfConsolidadas"):
        for conta in df_consolidadas.iter("Conta"):
            codigo_conta = conta.find("CodigoConta").text
            if codigo_conta in paramListOfContas:
                descricao_conta = conta.find("DescricaoConta").text
                valor_atual = conta.find("TrimestreAtual").text
                valor_anterior = conta.find("TrimestreAnterior").text
                if valor_atual != None:
                    # cria a conta
                    conta = CvmDemonstrativoConta()
                    conta.codigo = codigo_conta
                    conta.descricao = descricao_conta
                    conta.valorAtual = valor_atual
                    conta.valorAnterior = valor_anterior

                    # adiciona na lista
                    demonstrativo.addContaIndividual(conta)
    
    return demonstrativo


# define os parametros
paramCodigoCvm = 19640
paramTipoDemonstrativo = "ITR"
paramListOfContas = {"3.01","3.09",    "3.09.01",    "3.11",    "3.11.01",    "3.13"}

url = "http://www.rad.cvm.gov.br/ENETCONSULTA/frmDownloadDocumento.aspx?CodigoInstituicao=1&NumeroSequencialDocumento=136972"
file_temp_zip = f"{str(paramCodigoCvm)}.zip"
path_temp = os.path.join(tempfile.gettempdir(), "unzip")


# faz o download do arquivo
if (HttpHelper.downloadFile(url, file_temp_zip) == False):
    sys.exit("Abortando o programa.")

# Descompactando o arquivo zip
FileHelper.unzip(file_temp_zip, path_temp)

# Listando os arquivos extraídos
FileHelper.list_files(path_temp)

# Definindo o arquivo xml principal.
print("Definindo os arquivos")
xml_principal = get_xml_principal(paramCodigoCvm, paramTipoDemonstrativo, path_temp)
xml_formulario = get_xml_formulario(paramTipoDemonstrativo, path_temp)
if (xml_principal == None) or (xml_formulario == None):
    print("Arquivos necessarios nao encontrados")
    sys.exit("Abortando o programa.")

# construindo o objeto
demonstrativo = build_demonstrativo(xml_principal, xml_formulario)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(demonstrativo)
print("--------------------------------------------------------")
print(f"Data Fiscal {demonstrativo.getTrimestreFiscal()}T/{demonstrativo.getAnoFiscal()}")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# apaga os arquivos descompactados
print(f"Apagando arquivos temporarios")
FileHelper.delete_all(path_temp)
FileHelper.delete(file_temp_zip)

