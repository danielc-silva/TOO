from model.TarefaPessoal import TarefaPessoal
from model.TarefaProfissional import TarefaProfissional
from model.TarefaGamer import TarefaGamer
from datetime import datetime 

tPess = TarefaPessoal("Ir a feira")

#tPess.concluir()

#print(t.exibir_dados())

tPro = TarefaProfissional("Preencher as planilhas", "07-10-2025" , "Mini Curso de CC",) 

#tPro.concluir()

#print(t.exibir_dados())

a = TarefaGamer(titulo="Projeto Teste")

#print(a.exibir_dados())

a.exibir_dados()

lista_de_tarefas = [tPess, tPro, a]

print ("\n\n")

for tee in lista_de_tarefas:
    print(tee)
    print(tee.exibir_dados())

print ("\n\n")