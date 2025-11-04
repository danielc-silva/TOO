from .Tarefa import Tarefa
from datetime import date, time, datetime, timedelta
from .StatusTarefa import StatusTarefa

class TarefaProfissional(Tarefa):
    def __init__(self, projeto = None, data_entrega = None, nome_tarefa = None, descricao=None, data_realizacao=None, status = StatusTarefa.A_FAZER):
        super().__init__(nome_tarefa, descricao, data_realizacao, status) # herdei os campos que tenho em Tarefa 
        self.projeto = projeto
        self.data_entrega = data_entrega
    
    @property
    def projeto(self):
        return self.__projeto
    
    @projeto.setter
    def projeto(self, nome_projeto):
        self.__projeto = nome_projeto

    @property
    def data_entrega(self):
        return self.__data_entrega
        
    @data_entrega.setter
    def data_entrega(self, nova_data):
    # Mantém a sua ótima verificação para None
        if nova_data is None:
            self.__data_entrega = None
            return
        try:
            # Tenta converter a data no formato com hífens
            temporario = datetime.strptime(nova_data, "%d-%m-%Y") 
            self.__data_entrega = temporario.date()
            self.concluir() # recebi uma data q foi entregue então já marco como concluida

        except ValueError:
             #é a mesma logica q usei pra validar no Tarefa
             raise ValueError(f"ERRO: Data '{nova_data}' em formato inválido. Use DD-MM-YYYY.")
        
    def __str__ (self):
        infos = super().exibir_dados()
        infos +=  f"\nProjeto: {self.projeto}"
        infos +=  f"\nData entrega: {self.data_entrega}"

        return infos
    
    def exibir_dados (self):
        infos = super().exibir_dados()

        if self.projeto != None:
             infos +=  f"\nProjeto: {self.projeto}"

        if self.data_entrega != None:
             infos +=  f"\nData entrega: {self.data_entrega}"

        return infos
    
    def definir_termino(self):
         hoje = datetime.now()
         self.data_realizacao = hoje.strftime("%d-%m-%Y")