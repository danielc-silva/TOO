tabuada = 0
contador = 0
tabuada = int(input("\nDigite a tabuada que deseja imprimir:"))

for i in range(0 , ((tabuada*10)+1), tabuada):
    print(f"{contador} x {tabuada} = {i}")
    contador+=1
    
print("\n")