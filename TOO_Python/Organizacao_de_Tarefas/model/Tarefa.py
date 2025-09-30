from datetime import date, time, datetime, timedelta


class Tarefa:
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None):
        self.nome = nome_tarefa
        self.__concluido = False  # aqui tem os __ pois não temos um setter, e usamos concluido internamente com outra função
        self.descricao = descricao
        self.data_realizacao = data_realizacao

    @property  # sempre tem um retorno
    def data_realizacao(self):
        return self.__data_realizacao

    @data_realizacao.setter
    def data_realizacao(self, data):
    # Mantém a sua ótima verificação para None
        if data is None:
            self.__data_realizacao = None
            return
        try:
            # Tenta converter a data no formato com hífens
            temporario = datetime.strptime(data, "%d-%m-%Y")
            self.__data_realizacao = temporario.date()
        except ValueError:
             # Se falhar, AVISA o erro e LEVANTA uma nova exceção para parar o processo.
             # Isso força o 'except' do seu programa principal a ser acionado.
             # o try excpt captura erros que acontecem sozinhos já o raize ele cria um erro intencional
             raise ValueError(f"ERRO: Data '{data}' em formato inválido. Use DD-MM-YYYY.")

    @property
    def nome(self):
        return (
            self.__nome.upper()
        )  # aqui usamos __ então não precisamos usar no init,
           #pois aqui já faz isso, e se colocasse no init ia ignorar o que temos aqui

    @nome.setter
    def nome(self, nome_tarefa):
        self.__nome = nome_tarefa

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    ## outros métodos

    def concluir_tarefa(self):
        self.__concluido = True

    def exibir_dados(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        return f"Tarefa cadastrada: {self.nome} [{status}]"

    def __str__(self):
        status = "CONCLUIDA" if self.__concluido else "A FAZER"
        return f"Título: {self.nome} [{status}]\nData de Realização: {self.data_realizacao or 'Não definida'}"

    def __eq__(self, outro):
        if self.nome == outro.nome and self.data_realizacao == outro.data_realizacao:
            return True
        else:
            return False
