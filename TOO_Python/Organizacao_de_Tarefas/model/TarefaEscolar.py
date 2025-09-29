from .Tarefa import Tarefa
from datetime import date, time, datetime, timedelta

class TarefaEscolar(Tarefa):
    def __init__(
        self,
        nome_tarefa,
        disciplina,
        peso=0,
        descricao=None,
        data_realizacao=None,
        data_entrega=None,
    ):
        super().__init__(nome_tarefa, descricao, data_realizacao) # herdei os campos que tenho em Tarefa 
        # agr crio os campos que fazem parte apenas de TarefaEscolar
        self.disciplina = disciplina
        self.peso = peso
        self.data_entrega = data_entrega

    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self, nome_disciplina):
        self.__disciplina = nome_disciplina

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter #lembrando q setter deve ser feito depois do property
    def peso(self, peso_dis):
        if peso_dis >= 0:
            self.__peso = peso_dis
            return
        else:
            raise ValueError("O peso deve ser maior ou igual a zero.\n")
            
            
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
        except ValueError:
             #é a mesma logica q usei pra validar no Tarefa
             raise ValueError(f"ERRO: Data '{nova_data}' em formato inválido. Use DD-MM-YYYY.")

    def __str__(self):
        info_pai = super().__str__() #chamei o __str__ de Tarefa reaproveitei ele 
        
        info_escolar = (
            f"\nDisciplina: {self.disciplina}\n"
            f"Peso: {self.peso}\n"
            f"Data de Entrega: {self.data_entrega or 'Não definida'}\n"
             f"Data de Realização: {self.data_realizacao or 'Não definida'}"
        )
        
        return f"{info_pai}{info_escolar}"