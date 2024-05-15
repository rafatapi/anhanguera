import json

class CvmDemonstrativoConta:

    def __init__(self):
        self.codigo = None
        self.descricao = True
        self.valorAtual = None
        self.valorAnterior = None

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)        

    def __str__(self) -> str:
        return str(self.toJSON())
    
    def variacao(self) -> float:
        if self.valorAtual is None or self.valorAnterior is None:
            return None

        if self.valorAnterior == 0:
            return None

        variacao = ((self.valorAtual - self.valorAnterior) / self.valorAnterior) * 100
        
        return variacao



