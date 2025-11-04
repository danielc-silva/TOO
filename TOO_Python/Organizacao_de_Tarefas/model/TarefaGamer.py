from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from datetime import datetime
from .StatusTarefa import StatusTarefa
from .DificuldadeJogo import DificuldadeJogo

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None, jogo=None, status = StatusTarefa.A_FAZER, dificuldade = None):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao, status=status)
        self.tipo = tipo 
        self.jogo = jogo
        self.dificuldade = dificuldade

    @property
    def jogo(self):
        return self.__jogo
    
    @jogo.setter
    def jogo(self, nome_jogo):
         if nome_jogo:
             self.__jogo = nome_jogo.strip().title()
         else:
             self.__jogo = "Não informado"

    @property
    def tipo (self):
        return self.__tipo
    
    @tipo.setter
    def tipo (self, tipoo):
        if tipoo:
             self.__tipo = tipoo.strip().title()
        else:
             self.__tipo = "Não informado" # Ou "Geral", "Outros", etc.


    @property
    def dificuldade(self):
        return self.__dificuldade
    
    # [ isinstance ]-> função em Python que verifica se um objeto é uma instância de uma classe, tipo ou de uma tupla de classes
    # usar ele é uma otima forma de usar em OO pois respeira herança e tals
    # pra melhor entender, ler e pensar dessa forma fica mais claro
    # se a instância [tal] for do tipo TarefaGamer aí posso usar em um if como true e false

    @dificuldade.setter
    def dificuldade(self, nova_dificuldade):
        # testo e vejo se for none já digo q não foi definida
        if nova_dificuldade is None:
            self.__dificuldade = DificuldadeJogo.NAO_DEFINIDA
            return

        # utililso o isinstance para ver c tem o que foi posto no enum q criei
        if isinstance(nova_dificuldade, DificuldadeJogo):
            self.__dificuldade = nova_dificuldade
            return
        
        # utilizando novamente vejo se é uma string
        if isinstance(nova_dificuldade, str):
            try:
                # tento buscr pelo nome q nem FACIL
                self.__dificuldade = DificuldadeJogo[nova_dificuldade.upper()]
                return
            except KeyError:
                # não consegui lá em cima tento pela palavra normal Fácil
                try:
                    self.__dificuldade = DificuldadeJogo(nova_dificuldade)
                    return
                except ValueError:
                    # chegou até aqui e deu erro passo e emito a mensagem
                    pass

        # levantei um erro.
        raise ValueError(f"Dificuldade '{nova_dificuldade}' é inválida. Use um membro de DificuldadeJogo.")


    def definir_termino(self):
        hoje = datetime.now()
        self.data_realizacao = hoje.strftime("%d-%m-%Y")
        
    def exibir_dados(self):
        base = super().exibir_dados()
        txt_gamer = f"Dificuldade: {self.dificuldade.value}" 
        txt_gamer += f"\nTipo: {self.tipo}"
        txt_gamer += f"\nJogo: {self.jogo}"
        return f"{base}\n{txt_gamer}"
    
    def __str__(self):
       return f"{self.nome_T} [{self.status.value}] - {self.jogo} ({self.dificuldade.value})"