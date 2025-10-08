from model.Agendamento import Agendamento
from model.Compromisso import Compromisso
from model.TarefaProfissional import TarefaProfissional
from model.TarefaPessoal import TarefaPessoal


try:
    Ag1 = Agendamento("12-08-2025","15-03-2026", "Consulta médica", "Joao Silva", "UBS Centro")
    print (Ag1.exibir_dados())

    Comp1 = Compromisso("12-08-2025", "15-03-2026", "Consulta médica", "Joao Silva", "UBS Centro", "Diagnosticar", "Torção no joelho esquerdo", "12-11-2025")
    print(Comp1.exibir_dados())

    TProf1 = TarefaProfissional("Projeto Inovação", "12-09-2029", "Responder formulário", "O formulário foi disponibilizado no site da prefeitura" , "15-07-2027" )
    print (TProf1.exibir_dados()) # vai constar CONCLUIDO pois mandei data de entrega ou realização

    TProf2 = TarefaProfissional("Projeto Renovação", None, "Enviar documentos", "Documentos estão em uma pasta em cima da mesa para ser digitalizados" , "15-07-2027" )
    print (TProf2.exibir_dados()) # não vai constar CONCLUIDO pois não mandei data de entrega ou realização

    TPss1 = TarefaPessoal("Compras", "Comprar Frutas e verduras", "Banana, maça, brócolis, repolho", "15-07-2027" )
    print (TPss1.exibir_dados()) 

    print("\n\n")




except Exception as e:
    print(f"ERRO: {e}")