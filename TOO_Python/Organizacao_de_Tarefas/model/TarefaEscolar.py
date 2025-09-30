from .Tarefa import Tarefa
from datetime import date, time, datetime, timedelta

class TarefaEscolar(Tarefa):
    def __init__(
        self,
        nome_tarefa,
        obj_disciplina,
        peso=0, 
        descricao=None,
        data_realizacao=None,
        data_entrega=None
    ):
        super().__init__(nome_tarefa, descricao, data_realizacao) # herdei os campos que tenho em Tarefa 
        # agr crio os campos que fazem parte apenas de TarefaEscolar
        self.obj_disciplina = obj_disciplina
        self.peso = peso
        self.data_entrega = data_entrega

    @property
    def obj_disciplina(self):
        return self.__obj_disciplina
    
    @obj_disciplina.setter
    def obj_disciplina(self, nome_disciplina):
        self.__obj_disciplina = nome_disciplina

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter #lembrando q setter deve ser feito depois do property
    def peso(self, peso_dis):
        try:
            peso_convertido = float(peso_dis) # tento converter para float, c der erro é pq provavelmente recebeu um "sete"
        except (ValueError, TypeError):
            raise ValueError("O peso deve ser um valor numérico.")
        
        if peso_convertido >= 0:
            self.__peso = peso_convertido
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
            self.concluir_tarefa() # recebi uma data q foi entregue então já marco como concluida

        except ValueError:
             #é a mesma logica q usei pra validar no Tarefa
             raise ValueError(f"ERRO: Data '{nova_data}' em formato inválido. Use DD-MM-YYYY.")

    def __str__(self):

        info_pai = super().__str__() #chamei o __str__ de Tarefa reaproveitei ele sobrescrevi
        
        info_escolar = (
            f"\nDisciplina: {self.obj_disciplina}"
            f"Peso: {self.peso}\n"
            f"Data de Entrega: {self.data_entrega or 'Não definida'}\n"
        )
        return f"{info_pai}{info_escolar}"
    

    def exibir_dados(self):
        Ex_Dados = super().exibir_dados()

        if self.obj_disciplina != None:
            Ex_Dados += f"\nDisciplina: {self.obj_disciplina}\n"

        if self.data_entrega != None:
            Ex_Dados += f"Entregue em: {self.data_entrega}\n"

        if self.peso != None:
            Ex_Dados += f"Peso: {self.peso}\n"


        return Ex_Dados 
        