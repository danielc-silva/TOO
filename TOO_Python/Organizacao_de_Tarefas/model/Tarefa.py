from datetime import date, time, datetime, timedelta
from abc import ABC, abstractmethod

#  não vou criar ua tarefa generica,
#  vou apenas usar as tarefas escolar pessoal, profissional, 
# no caso Tarefa será uma classe abstrata

class Tarefa (ABC):
    def __init__(self, nome_tarefa=None, descricao=None, data_realizacao=None):
        self.nome_T = nome_tarefa
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
    def nome_T(self):
        return (
            self.__nome_T
        )  
           #pois aqui já faz isso, e se colocasse no init ia ignorar o que temos aqui

    @nome_T.setter # quando o init chama o setter ele cria e define como atributo privado
    def nome_T(self, nome_tarefa):
        self.__nome_T = nome_tarefa 

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

    ## outros métodos

    def concluir_tarefa(self):
        self.__concluido = True


    @abstractmethod
    def exibir_dados(self):
        Ex_Dados = "\vTAREFA CADASTRADA:"
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        if self.nome_T != None:
            Ex_Dados += f"\nTítulo: {self.nome_T} [{status}]"

        if self.descricao != None:
            Ex_Dados += f"\nDescrição: {self.descricao}"

        if self.data_realizacao != None:
            Ex_Dados += f"\nData prevista: {self.data_realizacao or 'Não definida'}"

        return Ex_Dados


    def __str__(self): 
        status = "CONCLUIDA" if self.__concluido else "A FAZER"
        return f"\nTítulo: {self.nome_T} [{status}]\nData de Realização: {self.data_realizacao or 'Não definida'}"

    def __eq__(self, outro): # com esse consigo comparar se são iguais
        if self.nome_T == outro.nome_T and self.data_realizacao == outro.data_realizacao:
            return True
        else:
            return False
        
    # @abstractmethod
    #def teste_definir (self):
    #   pass 
    # nesse caso quando crio uma tarefa ele me obriga a criar um tese_definir