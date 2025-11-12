from datetime import datetime ,timedelta 

def validar_data_nascimento(data_str): #aqui é uma função
        formato_esperado = "%d/%m/%Y"
        try:
            data_nascimento = datetime.strptime(data_str, formato_esperado)
        except ValueError:
            raise ValueError("Formato de data inválido. Use DD/MM/AAAA.")

        if data_nascimento > datetime.now(): #aqui confiro se a data de nascimento não é maior q a data atual
            raise ValueError("A data de nascimento não pode ser no futuro.")

        return data_nascimento #retorno a data de nascimento para onde foi chamada a função


def calcular_idade(data_nascimento):
     hoje_agr = datetime.now()

     # extração de ano mes dia
     ano_nascimento = data_nascimento.year
     mes_nascimento = data_nascimento.month
     dia_nascimento = data_nascimento.day
     ano_agr = hoje_agr.year
     mes_agr = hoje_agr.month
     dia_agr = hoje_agr.day

     idade = ano_agr - ano_nascimento #faço a contagem direta com os anos
     # depois verifico se já fez aniversario ou não

     if mes_agr <= mes_nascimento and dia_agr < dia_nascimento:
          idade -=1 
     
     return idade


data_input = input("Digite sua data de nascimento para calcular a idade (DD/MM/AAAA): ")

try:
    data_validada = validar_data_nascimento(data_input)
    idade = calcular_idade(data_validada)
    print(f"\nVocê tem {idade} anos.\n")
except ValueError as e:
    print(f"Erro: {e}")