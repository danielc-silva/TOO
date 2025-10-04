from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina

try:
     D1_Calculo = Disciplina("Cálculo", "Ciência da Computação", 75, "Marcelo Lacortte" )
     #print (D1_Calculo)

     D2_Too = Disciplina("Tecnologia de Orientação à Obejetos", "Ciência da Computação", 45 , "Vanessa Lago" )
     #print(D2_Too)

     D3_Estrutura_I = Disciplina("Estrutura de Dados I", "Ciência da Computação", 75 , "Maikon Santos" )
     #print(D3_Estrutura_I)

     # TAREFA GENÉRICA SEM VINCULO COM DISCIPLINA
     T1_Generica = Tarefa ("Estudar TOO", "Aprender conceitos e orientação a objetos.", "07-10-2025")
     #print (T1_Generica)

     T1_Escolar = TarefaEscolar(
        "Introdução a herança",
        D2_Too,
        7,
        "Deve ser realizada no Colab",
        "21-10-2026",
        "12-08-2025",
    ) # aqui estou pondo uma data da entrega
      # quando recebe a data já marca como concluido, pois tem uma data de entrega
      # chamei no setter quando não está None então self.concluir_tarefa
     
     T2_Escolar = TarefaEscolar(
        "Introdução a Pilha e Fila",
        D3_Estrutura_I,
        6,
        "Deve ser realizada no notbook",
        "15-10-2027",
        #"05-12-2025",
    ) # nesse caso não vou mandar uma data de entrega
      # vai continuar no status [A FAZER]
     

     # Mostrando Objetos pelo metodo .exibir_dados
     # Criei um método exibir dados para Disciplina
     
     print("\n\n")

     print(D1_Calculo.exibir_dados())
     print(D2_Too.exibir_dados())
     print(D3_Estrutura_I.exibir_dados())

     print(T1_Generica.exibir_dados())
     print()

     print(T1_Escolar.exibir_dados())
     print(T2_Escolar.exibir_dados())

     print("\n\n Depois de Tudo Teste dnv skksks")

except Exception as e:
    print(f"ERRO: {e}")