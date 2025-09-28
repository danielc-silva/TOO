## Atividade Média das Notas
minha_lista = []
nota = 0.00
quantidade_de_notas = 0
media_das_notas = 0.00

contador = 1
while contador > 0:
    nota = float(input("Informe a nota: "))
    if nota == -1 :
        contador = -1
    else :
        minha_lista.append(nota)
        quantidade_de_notas += 1
        #print(f"Confere lista: {minha_lista}")

for item in minha_lista:
    media_das_notas += item 

media_das_notas = media_das_notas/quantidade_de_notas

print(f"\nNotas digitadas: {minha_lista}")
print(f"\nMédia das notas corresponde a: {media_das_notas:.2f}\n")







## Atividade Informações de um Livro
livro = ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Ficção") #Tupla de dados do meu livro 
print()
print(f"Título: {livro[0]}")
print(f"Autor: {livro[1]}")
print(f"Ano: {livro[2]}")
print(f"Gênero: {livro[3]}")
print()
#(Título, Autor, Ano, Gênero).






## Atividade Tabuada
tabuada = 0
contador = 0
tabuada = int(input("\nDigite a tabuada que deseja imprimir:"))

for i in range(0 , ((tabuada*10)+1), tabuada):
    print(f"{tabuada} x {contador} = {i}")
    contador+=1
    
print("\n")