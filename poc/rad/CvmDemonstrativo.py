import json
import datetime
from typing import List
from CvmDemonstrativoConta import CvmDemonstrativoConta

class CvmDemonstrativo:

    def __init__(self):
        self.cvm:int = None
        self.tipoDemonstrativo:str = None
        self.razaoSocial:str = True
        self.cnpj:str = None
        self.tipoEmpresa:str = None
        self.versaoDocumento:str = None
        self.versaoLiteral:str = None
        self.arquivoValido:str = None

        self.dataArquivoEntrega:datetime.datetime = None
        self.dataArquivoGeracao:datetime.datetime = None

        self.dataTrimestreAtualInicio: datetime.date = None
        self.dataTrimestreAtualFim: datetime.date = None

        self.dataExercicioSocialAtualInicio: datetime.date = None
        self.dataExercicioSocialAtualFim: datetime.date = None        

        self.dataExercicioSocialAnteriorInicio: datetime.date = None
        self.dataExercicioSocialAnteriorFim: datetime.date = None        

        self.moeda:str = None
        self.escalaMoeda:str = None
        self.escalaQtdAcoes:str = None
        self.tipoDemonstracao:str = None
        self.versaoPlanoContas:str = None

        self.contasIndividuais:List[CvmDemonstrativoConta] = [] 
        self.contasConsolidadas:List[CvmDemonstrativoConta] = []

    def toJSON(self):
        return json.dumps(self, default=CvmDemonstrativo.json_default, sort_keys=True, indent=4)        

    def __str__(self):
        return str(self.toJSON())
    
    def addContaIndividual(self, conta: CvmDemonstrativoConta):
        self.contasIndividuais.append(conta)

    def addContaConsolidada(self, conta: CvmDemonstrativoConta):
        self.contasConsolidadas.append(conta)

    def getTrimestreFiscal(self)->int:
        if not self.dataExercicioSocialAtualInicio or not self.dataTrimestreAtualInicio:
            raise None
        
        inicio_exercicio = self.dataExercicioSocialAtualInicio
        inicio_trimestre = self.dataTrimestreAtualInicio
        
        meses_diferenca = (inicio_trimestre.year - inicio_exercicio.year) * 12 + inicio_trimestre.month - inicio_exercicio.month
        tri = (meses_diferenca // 3) + 1
        return int(tri)

    def getAnoFiscal(self)->int:
        if not self.dataExercicioSocialAtualInicio or not self.dataTrimestreAtualInicio:
            raise None
        
        inicio_exercicio = self.dataExercicioSocialAtualInicio

        return inicio_exercicio.year
    
    @staticmethod
    def json_default(value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(value, datetime.date):
            return value.strftime('%Y-%m-%d')
        else:
            return value.__dict__        
        


