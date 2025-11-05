from model.TarefaFactory import TarefaFactory
from model.TipoTarefaPessoal import TipoTarefaPessoal
from model.StatusTarefa import StatusTarefa
from model.Disciplina import Disciplina


TPess = TarefaFactory.criar_tarefa(
    tipo_tarefa = "pessoal",
      tipo_relacionado = "SAUDE",
        nome_tarefa = "Consulta",
          descricao = "As 19 horas",
            data_realizacao = None,
              status = None)

TProf = TarefaFactory.criar_tarefa(
                tipo_tarefa = 'profissional',
                projeto = 'Site Empres',
                data_entrega = '12-12-2025',
                nome_tarefa = 'Projeto',
                descricao = 'Adicionar alguma coisa...',
                data_realizacao = None,
                status = None)

TGamer = TarefaFactory.criar_tarefa (
    tipo_tarefa = "gamer",
    titulo = 'Jogar Minecraft',
    tipo = 'Lazer',
    descricao = 'Chamar os amigos ...',
    data_realizacao = '12-12-2025',
    jogo = 'Minecraft',
    status = None,
    dificuldade = 'Dificil'
)

TOO = Disciplina('TOO', 'CC', 1200,'Vanessa')

TEscolar = TarefaFactory.criar_tarefa ( 
    tipo_tarefa = 'escolar',
    nome_tarefa = 'Exercicios EAD',
    obj_disciplina = TOO,
    peso = '5',
    descricao = 'Realizar no codeblocks',
    data_realizacao = '12-12-2025',
    data_entrega = '12-12-2025',
    status = 'concluida'
)



print ("\n")
print(TPess.exibir_dados())

print(TEscolar.exibir_dados())

print(TProf.exibir_dados())

print(TGamer.exibir_dados())
print ("\n")

