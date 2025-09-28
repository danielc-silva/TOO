try:
    espaco = 0
    vogais = 0

    frase = input("Digite a frase:")
    frase = frase.strip()
    frase = frase.title()
    
    if '.' != frase[-1]:
        frase = frase + '.'
    
    lista_de_frase = frase.split()
    
    frase = ' '.join(lista_de_frase)

    for caracter in frase.lower():
        if ' ' == caracter :
            espaco +=1
        if caracter in 'aeiouáéíóúâêîôûãõ':
            vogais +=1
    
    print (f'\n{frase}')
    print (f'Quantidade de espaços: {espaco}')
    print (f'Quantas vogais: {vogais}')
    print (f'Quantidade de caracteres: {len(frase)}\n')

except ValueError as err:
    print (f"ERRO: {err}")

#ficou dizendo que tem um carcter a mais