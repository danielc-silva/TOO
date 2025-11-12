texto = ''
vogais = 0
vogais1 = 'aeiou'

texto = input("\nDigite o texto para contagem de vogais:")
texto = texto.lower()

for i in texto :
    if i in vogais1:
        vogais +=1

print(f"O número de vogais no texto é:{vogais}")

print()
