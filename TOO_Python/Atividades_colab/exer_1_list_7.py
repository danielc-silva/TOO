try:
    from datetime import datetime

    def validar_data_nascimento(data_str):
       
        formato_esperado = "%d/%m/%Y"
        
        try:
           
            data_nascimento = datetime.strptime(data_str, formato_esperado)
        except ValueError:
            raise ValueError("Formato de data inválido. Use DD/MM/AAAA.")

        if data_nascimento > datetime.now():
            raise ValueError("A data de nascimento não pode ser no futuro.")

        return data_nascimento
        # --- FIM DA LÓGICA INSERIDA ---

# --- Programa principal (mantido como no seu original) ---
    data_input = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    try:
        data_validada = validar_data_nascimento(data_input)
        print(f"Data de nascimento válida: {data_validada.strftime('%d de %B de %Y')}")

    except ValueError as e:
        print(f"Erro: {e}")

except Exception as e:
    # Mudei para 'Exception' para capturar qualquer erro inesperado.
    print(f"Ocorreu um erro: {e}")