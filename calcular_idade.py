from datetime import datetime, timedelta

def calcular_idade():
    ano_atual = datetime.now().year
    data_atual = datetime.now()
    
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            ano_nascimento = int(input(f"Digite seu ano de nascimento (entre 1922 e {ano_atual - 1}): "))
            mes_nascimento = int(input("Digite seu mês de nascimento (1-12): "))
            dia_nascimento = int(input("Digite seu dia de nascimento (1-31): "))
            
            data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
            
            if 1922 <= ano_nascimento <= ano_atual - 1:
                idade_anos = ano_atual - ano_nascimento
                idade_meses = (data_atual.year - data_nascimento.year) * 12 + data_atual.month - data_nascimento.month
                idade_dias = (data_atual - data_nascimento).days
                idade_horas = idade_dias * 24
                idade_minutos = idade_horas * 60
                
                proximo_aniversario = datetime(ano_atual, mes_nascimento, dia_nascimento)
                if proximo_aniversario < data_atual:
                    proximo_aniversario = datetime(ano_atual + 1, mes_nascimento, dia_nascimento)
                
                dias_para_aniversario = (proximo_aniversario - data_atual).days
                
                print(f"{nome}, você completou ou completará {idade_anos} anos em {ano_atual}.")
                print(f"Idade em meses: {idade_meses}")
                print(f"Idade em dias: {idade_dias}")
                print(f"Idade em horas: {idade_horas}")
                print(f"Idade em minutos: {idade_minutos}")
                print(f"Faltam {dias_para_aniversario} dias para o seu próximo aniversário.")
                break
            else:
                print(f"Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o ano de nascimento.")

calcular_idade()
