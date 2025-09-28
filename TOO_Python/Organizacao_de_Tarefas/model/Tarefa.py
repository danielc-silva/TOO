from datetime import date, time, datetime, timedelta


class Tarefa:
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None):
        self.__nome = nome_tarefa
        self.__concluido = False
        self.__descricao = descricao
        self.__data_realizacao = data_realizacao

    @property  # sempre tem um retorno
    def data_realizacao(self):
        return self.__data_realizacao

    @data_realizacao.setter
    def data_realizacao(self, data):
        if data is None:
            self.__data_realizacao = None
            return # Sai da função aqui
        try:
            self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
        except ValueError as e:
            print(f"ERRO: Data em formato inválido. Use DD-MM-YYYY. ({e})")

    @property
    def nome(self):
        return self.__nome.upper()

    @nome.setter
    def nome(self, nome_tarefa):
        self.__nome = nome_tarefa

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    def concluir_tarefa(self):
        self.__concluido = True

    def exibir_dados(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        return f"Tarefa cadastrada: {self.nome} [{status}]"
    
    def __str__(self):
        status = "CONCLUIDA" if self.__concluido else "A FAZER"
        return f"Tarefa: {self.nome} [{status}]"

    def __eq__(self, outro):
        if self.nome == outro.nome and self.data_realizacao == outro.data_realizacao:
            return True
        else:
            return False
