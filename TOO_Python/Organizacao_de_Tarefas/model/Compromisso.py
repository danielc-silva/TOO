from .Tarefa import Tarefa
from .Agendamento import Agendamento

class Compromisso (Agendamento, Tarefa):
    def __init__ (self, data_inicio=None, data_fim=None, atividade=None, nome=None, local=None, nome_tarefa=None, descricao=None, data_realizacao=None):
       
         Agendamento.__init__(self, data_inicio, data_fim, atividade, nome, local) # herdei de agendamento
         Tarefa.__init__(self, nome_tarefa, descricao, data_realizacao) # herdei os campos que tenho em Tarefa 


    def __str__ (self):
        infos = "\nCOMPROMISSO\n======================================"
        infos += Agendamento.__str__(self)
        infos += Tarefa.exibir_dados(self)
        infos += "\n======================================\n"

        return infos
    
    def exibir_dados(self):  
        infos = "\nCOMPROMISSO\n======================================"
        # como já estou usando os outros exibir dados e não tenho nada alem do que herdei
        # poderia usar apenas o __str__ pois não estou verificando nada no exibir dados
        infos += Agendamento.__str__(self)
        infos += Tarefa.exibir_dados(self)
        infos += "\n======================================\n"

        return infos

      
       