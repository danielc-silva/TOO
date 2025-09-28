from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar

try:
    t1 = Tarefa("Aula TOO", "teste", "19-09-2025")
    print(t1.exibir_dados())

    t1.concluir_tarefa()
    print(t1.exibir_dados())

    t2 = Tarefa("Fazer compras", "teste", "19-09-2025")
    print(t2.exibir_dados())

    print(t2.exibir_dados())

    t3 = Tarefa("Fazer compras", "teste", "19-09-2025")
    print(t2.exibir_dados())

    if t2 == t3:
        print("Tarefas iguais.")
    else:
        print("Tarefas diferentes.")

    print("\n")

    t4 = TarefaEscolar(
        "Introdução a herança",
        "TOO",
        "5",
        "Deve ser realizada no notbook",
        "21/09/2025",
        "12/05/2026",
    )
    print(t4)
    # print(t4.exibir_dados())

    print("\n")

except Exception as e:
    print(f"ERRO: {e}")
