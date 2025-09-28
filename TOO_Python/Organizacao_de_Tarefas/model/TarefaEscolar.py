from .Tarefa import Tarefa

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
        super().__init__(nome_tarefa, descricao, data_realizacao)
        
        self.__disciplina = disciplina
        self.__peso = peso
        self.__data_entrega = data_entrega

    @property
    def disciplina(self):
        return self.__disciplina

    @property
    def peso(self):
        return self.__peso

    @property
    def data_entrega(self):
        return self.__data_entrega
        
    @data_entrega.setter
    def data_entrega(self, nova_data):
        self.__data_entrega = nova_data

    def __str__(self):
        info_pai = super().__str__()
        
        info_escolar = (
            f"\nDisciplina: {self.disciplina}\n"
            f"Peso: {self.peso}\n"
            f"Data de Entrega: {self.data_entrega or 'Não definida'}"
        )
        
        return f"{info_pai}{info_escolar}"