from .Tarefa import Tarefa

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao)
        self.tipo_relacionado = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.

    def exibir_dados (self):
        infos = super().exibir_dados()
        if self.tipo_relacionado != None:
             infos +=  f"\nTipo: {self.tipo_relacionado}"
        
        return infos