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

    texto = texto.lower()

    for letra in texto:

        if letra == ' ' :
                texto_criptografado += letra
        else:

            for posicao in range(26):

                if letra == alfabeto[posicao]:
                    nova_posicao = (posicao + posicoes_deslocar)
                    
                    if nova_posicao <= 25:
                         texto_criptografado += alfabeto[nova_posicao]
                    else:
                         while nova_posicao > 25:
                              nova_posicao = nova_posicao -26
                              
                         texto_criptografado += alfabeto[nova_posicao]

    lista_de_frases.append(texto_criptografado)
    
    texto_criptografado = ''

print('\nSaída criptografada:\n')

for frase in lista_de_frases:
    print(frase)

print('\n')