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