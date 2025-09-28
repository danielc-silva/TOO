from datetime import datetime, timedelta

def validar_DtHr_evento(data_hora_str):
    formato_esperado = "%d/%m/%Y %H:%M"
    try:
        data_hora_evento = datetime.strptime(data_hora_str, formato_esperado)
    except ValueError:
        raise ValueError("Formato de data inválido. Use DD/MM/AAAA HH:MM.")

    if data_hora_evento < datetime.now():
        raise ValueError("A data e hora do evento não podem estar no passado.")
    
    return data_hora_evento

def quanto_tempo_falta_para_o_evento(data_hora_evento):
    agora = datetime.now()
    diferenca = data_hora_evento - agora
    
    if diferenca.total_seconds() <= 0:
        print("\nO evento está no passado ou a acontecer agora.")
        return
    
    dias = diferenca.days
    horas = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60
    
    partes_da_mensagem = []
    
    if dias > 0:
        partes_da_mensagem.append(f"{dias} dia" if dias == 1 else f"{dias} dias")
    if horas > 0:
        partes_da_mensagem.append(f"{horas} hora" if horas == 1 else f"{horas} horas")
    if minutos > 0:
        partes_da_mensagem.append(f"{minutos} minuto" if minutos == 1 else f"{minutos} minutos")

    if not partes_da_mensagem:
        print("\nO evento é no próximo minuto!")
        return
    
    if len(partes_da_mensagem) == 1:
        tempo_restante_str = partes_da_mensagem[0]
    elif len(partes_da_mensagem) == 2:
        tempo_restante_str = " e ".join(partes_da_mensagem)
    else:
        primeiras_partes = ", ".join(partes_da_mensagem[:-1])
        ultima_parte = partes_da_mensagem[-1]
        tempo_restante_str = f"{primeiras_partes} e {ultima_parte}"
    
    print(f"Faltam {tempo_restante_str} para o evento.\n")

def agendar_evento():
    try:
        nome_evento = input("Digite o nome do evento: ")
        data_hora_str = input("Digite a data e hora do evento (DD/MM/AAAA HH:MM): ")

        data_validada = validar_DtHr_evento(data_hora_str)

        print(f"\nEvento '{nome_evento}' agendado com sucesso para {data_validada.strftime('%d de %B de %Y às %H:%M')}.")
        
        quanto_tempo_falta_para_o_evento(data_validada)

    except ValueError as e:
        print(f"Erro: {e}")


agendar_evento()