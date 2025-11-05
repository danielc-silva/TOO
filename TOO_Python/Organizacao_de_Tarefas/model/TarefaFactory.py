from .TarefaEscolar import TarefaEscolar
from .TarefaGamer import TarefaGamer
from .TarefaPessoal import TarefaPessoal
from .TarefaProfissional import TarefaProfissional
from .StatusTarefa import StatusTarefa
from .TipoTarefaPessoal import TipoTarefaPessoal
from .DificuldadeJogo import DificuldadeJogo

class TarefaFactory ():
    @staticmethod
    def criar_tarefa(tipo_tarefa : str, **args):
        if tipo_tarefa == 'pessoal':
            return TarefaPessoal(
                tipo_relacionado = args.get('tipo_relacionado', None),
                nome_tarefa = args.get('nome_tarefa', None),
                descricao = args.get('descricao', None),
                data_realizacao = args.get('data_realizacao', None),
                status = args.get('status', None)
            )
        elif tipo_tarefa == 'profissional':
            return TarefaProfissional(
                projeto = args.get('projeto', None),
                data_entrega = args.get('data_entrega', None),
                nome_tarefa = args.get('nome_tarefa', None),
                descricao = args.get('descricao', None),
                data_realizacao = args.get('data_realizacao', None),
                status = args.get('status', None) 
            )
        elif tipo_tarefa == 'gamer':
            return TarefaGamer(
                titulo = args.get('titulo', None),
                tipo = args.get('tipo', None),
                descricao = args.get('descricao', None),
                data_realizacao = args.get('data_realizacao', None),
                jogo = args.get('jogo', None),
                status = args.get('status', None),
                dificuldade = args.get('dificuldade', None)
            )
        elif tipo_tarefa == 'escolar':
            return TarefaEscolar(
                nome_tarefa = args.get('nome_tarefa', None),
                obj_disciplina = args.get('obj_disciplina', None),
                peso = args.get('peso', None),
                descricao = args.get('descricao', None),
                data_realizacao = args.get('data_realizacao', None),
                data_entrega = args.get('data_entrega', None),
                status = args.get('status', None) 
            )
        else:
            raise f"Tipo de Tarefa inválida: {tipo_tarefa}"
