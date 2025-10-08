from .Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, tipo_relacionado = None, nome_tarefa = None, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao, data_realizacao) # herdei os campos que tenho em Tarefa 
        self.tipo_relacionado = tipo_relacionado

    
    @property
    def tipo_relacionado(self):
        return self.__tipo_relacionado
    
    @tipo_relacionado.setter
    def tipo_relacionado(self, tipo_tar):
        self.__tipo_relacionado = tipo_tar

    
    def __str__ (self):
        infos = super().exibir_dados()
        infos +=  f"\nTipo: {self.tipo_relacionado}"
        return infos
    
    def exibir_dados (self):
        infos = super().exibir_dados()

        if self.tipo_relacionado != None:
             infos +=  f"\nTipo: {self.tipo_relacionado}"
        
        return infos