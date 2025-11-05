from model.TarefaGamer import TarefaGamer
from model.TarefaPessoal import TarefaPessoal

try:
    TarGamer = TarefaGamer("Jogar Minecraft","Lazer", "Lembrar de chamar os amigos", "12-06-2025", "Minecraft", None, "Difícil")
    TarPessoal = TarefaPessoal("Lazer", "Ir ao Shoping", "Fazer compras", "12-04-2024", 'CoNcLUidA')

    # Na tarefa gamer deixei status como None, então ele vai ficar como [A fazer], e dificuldade DIFICIL usando o Enun
    # Na tarefa pessoal já marquei como concluida usando o Enun com a data_realizacao que eu atribui
    # No definir_termino eu utilizei o [datetime.now() -> obtem data e hora atual do sistema]
    # dessa maneira [.concluir] atualiza para concluida e
    # chama [.definir_termino] que põe a data exata do termino da tarefa para data_realizacao

    print ("\n")
    print (TarGamer.exibir_dados())
    #TarPessoal.concluir()
    print (TarPessoal.exibir_dados())
    TarGamer.concluir()
    print ("\nAPÓS CONCLUIR TAREFA GAMER")
    print (TarGamer.exibir_dados())
    print ("\n")

except Exception as e:
    print(f"ERRO: {e}")