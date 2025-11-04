from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from datetime import date, time, datetime, timedelta
from .TipoTarefaPessoal import TipoTarefaPessoal

class TarefaPessoal(Tarefa):
    def __init__(self, tipo_relacionado = None, nome_tarefa = None, descricao=None, data_realizacao=None, status = StatusTarefa.A_FAZER):
        super().__init__(nome_tarefa, descricao, data_realizacao, status) # herdei os campos que tenho em Tarefa 
        self.tipo_relacionado = tipo_relacionado

    @property
    def tipo_relacionado(self):
        return self.__tipo_relacionado
    
    @tipo_relacionado.setter
    def tipo_relacionado(self, TipTar):
        # testo e vejo se for none já digo q não foi definida
        if TipTar is None:
            self.__tipo_relacionado = TipoTarefaPessoal.OUTROS
            return

        # utililso o isinstance para ver c tem o que foi posto no enum q criei
        if isinstance(TipTar, TipoTarefaPessoal):
            self.__tipo_relacionado = TipTar
            return
        
        # utilizando novamente vejo se é uma string
        if isinstance(TipTar, str):
            try:
                # tento buscr pelo nome q nem FACIL
                self.__tipo_relacionado = TipoTarefaPessoal[TipTar.upper()]
                return
            except KeyError:
                # não consegui lá em cima tento pela palavra normal Fácil
                try:
                    self.__tipo_relacionado = TipoTarefaPessoal(TipTar)
                    return
                except ValueError:
                    # chegou até aqui e deu erro passo e emito a mensagem
                    pass

        # levantei um erro.
        raise ValueError(f"Tipo de tarefa: '{TipTar}' é inválido. Use um membro de TipoTarefaPessoal.")

    
    def __str__ (self):
        infos = super().exibir_dados()
        infos +=  f"\nTipo: {self.tipo_relacionado}"
        return infos
    
    def exibir_dados (self):
        infos = super().exibir_dados()
        infos +=  f"\nTipo: {self.tipo_relacionado.value}"
        return infos
    
    def definir_termino(self):
         hoje = datetime.now()
         self.data_realizacao = hoje.strftime("%d-%m-%Y")