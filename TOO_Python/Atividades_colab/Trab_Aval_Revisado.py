##    Proposta 01 - Guerra nas Estrelas    ##

quantidade_mensagens = 0
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
posicoes_deslocar = 0
texto = ''
texto_criptografado = ''
lista_de_frases = []

print ("\nIniciando programa de criptografia !!! \n")

quantidade_mensagens = int(input())

for indice in range(quantidade_mensagens) :
    
    posicoes_deslocar = int(input()) 

    texto = input ()

    for letra in texto:

        if letra in alfabeto:
                nova_posicao = (alfabeto.find(letra) + posicoes_deslocar) % 26
                texto_criptografado += alfabeto[nova_posicao]
        elif letra == ' ':
                texto_criptografado += letra

    lista_de_frases.append(texto_criptografado)
    
    texto_criptografado = ''

print('\nSaída criptografada:\n')

for frase in lista_de_frases:
    print(frase)

print('\n')