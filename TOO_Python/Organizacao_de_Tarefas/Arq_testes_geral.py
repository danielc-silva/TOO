from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar

try:
    t1 = Tarefa("Aula TOO", "teste", "19-09-2025")
    print(t1.exibir_dados())  # mostrando apenas a tarefa criada

    t1.concluir_tarefa()  # conclui a tarefa chamando concluir tarefa

    print(t1.exibir_dados())  # mostrei depois de ter marcada como concluida

    t2 = Tarefa("Fazer compras", "teste", "19-09-2025")

    print(t2.exibir_dados())

    t3 = Tarefa("Academia", "tenta", "27-07-2025")
    print(t3.exibir_dados())

    # nesse caso o if compara todos os dados para retornar se são iguais ou não
    if t2 == t3:
        print("Tarefas iguais.")
    else:
        print("Tarefas diferentes.")

    print() #o print já dá um \n automaticamente

    t4 = TarefaEscolar(
        "Introdução a herança",
        "TOO",
        7.5,
        "Deve ser realizada no notbook",
        "21-10-2025",
        "12-10-2026",
    )

    #t4.concluir_tarefa()
    print ("Mostrando com o método __str__\n")
    print(t4)  # mostra de acordo com a função __str__ mostrando todos os campos independente se None ou não
    print ("Mostrando com o método exibir_dados() \n")
    print(t4.exibir_dados()) # mostra de acordo com o exibir dados quando não tem valor ele não mostra o campo

    # ao executa esse cód vai dar erro, pois estou tentando criar algo com uma classe abstrata

except Exception as e:
    print(f"ERRO: {e}")
