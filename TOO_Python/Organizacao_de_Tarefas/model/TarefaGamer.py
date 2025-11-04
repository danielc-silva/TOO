from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from datetime import datetime
from .StatusTarefa import StatusTarefa

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None, jogo=None, status = StatusTarefa.A_FAZER):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao, status=status)
        self.tipo = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.
        self.jogo = jogo

    @property
    def jogo(self):
        return self.__jogo
    
    @jogo.setter
    def jogo(self, nome_jogo):
         if nome_jogo:
             self.__jogo = nome_jogo.strip().title()
         else:
             self.__jogo = "Não informado"

    def definir_termino(self):
        hoje = datetime.now()
        self.data_realizacao = hoje.strftime("%d-%m-%Y")
        
    def exibir_dados(self):
        base = super().exibir_dados()
        txt_gamer = f"Tipo: {self.tipo}"
        txt_gamer += f"\nJogo: {self.jogo}"
        return f"{base}\n{txt_gamer}"
    