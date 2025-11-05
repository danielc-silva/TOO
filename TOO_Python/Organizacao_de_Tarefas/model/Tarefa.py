from datetime import date, time, datetime, timedelta
from abc import ABC, abstractmethod
from .StatusTarefa import StatusTarefa

#  não vou criar ua tarefa generica,
#  vou apenas usar as tarefas escolar pessoal, profissional, 
# no caso Tarefa será uma classe abstrata

class Tarefa (ABC):
    def __init__(self, nome_tarefa=None, descricao=None, data_realizacao=None, status = None ):
        self.nome_T = nome_tarefa
        # vou comentar e usar um enun
        # self.__concluido = False  # aqui tem os __ pois não temos um setter, e usamos concluido internamente com outra função
        self.descricao = descricao
        self.data_realizacao = data_realizacao
        self.status = status

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

    @property
    def status (self):
        return self.__status

    @status.setter
    def status(self, statuss):
        # testo e vejo se for none já digo q não foi definida
        if statuss is None:
            self.__status = StatusTarefa.A_FAZER
            return

        # utililso o isinstance para ver c tem o que foi posto no enum q criei
        if isinstance(statuss, StatusTarefa):
            self.__status = statuss
            return
        
        # utilizando novamente vejo se é uma string
        if isinstance(statuss, str):
            try:
                # tento buscr pelo nome q nem FACIL
                self.__status = StatusTarefa[statuss.upper()]
                return
            except KeyError:
                # não consegui lá em cima tento pela palavra normal Fácil
                try:
                    self.__status = StatusTarefa(statuss)
                    return
                except ValueError:
                    # chegou até aqui e deu erro passo e emito a mensagem
                    pass

        # levantei um erro.
        raise ValueError(f"Status: '{statuss}' é inválido. Use um membro de StatusTarefa.")

    ## outros métodos

    #def concluir_tarefa(self):
        #self.__concluido = True
        #self.status = StatusTarefa.CONCLUIDA

    @abstractmethod
    def exibir_dados(self):
        Ex_Dados = "\nTAREFA CADASTRADA:"
        #status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        if self.nome_T != None:
            Ex_Dados += f"\nTítulo: {self.nome_T} [{self.status.value}]" 

        if self.descricao != None:
            Ex_Dados += f"\nDescrição: {self.descricao}"

        if self.data_realizacao != None:
            Ex_Dados += f"\nData prevista: {self.data_realizacao or 'Não definida'}"

        return Ex_Dados

    def __str__(self):
        return f"{self.__nome_T} [{self.status.value}]"

    def __eq__(self, outro): # com esse consigo comparar se são iguais
        if self.nome_T == outro.nome_T and self.data_realizacao == outro.data_realizacao:
            return True
        else:
            return False
        
    def concluir(self):
        #self.__concluido = True
        self.status = StatusTarefa.CONCLUIDA   
        self.definir_termino() 
    
    def iniciarTarefa(self):
        self.status = StatusTarefa.EM_ANDAMENTO

    @abstractmethod
    def definir_termino(self):
        pass
        
    # @abstractmethod
    #def teste_definir (self):
    #   pass 
    # nesse caso quando crio uma tarefa ele me obriga a criar um teste_definir