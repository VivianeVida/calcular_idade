# Programa de Cálculo de Idade

Este programa em Python solicita ao usuário seu nome completo e ano de nascimento, e calcula a idade do usuário em anos, meses, dias, horas e minutos. Além disso, informa quantos dias faltam para o próximo aniversário.

## Funcionalidades

- Solicita o nome completo do usuário.
- Solicita o ano, mês e dia de nascimento do usuário.
- Calcula a idade em anos, meses, dias, horas e minutos.
- Informa quantos dias faltam para o próximo aniversário.
- Valida as entradas para garantir que o ano de nascimento esteja entre 1922 e o ano anterior ao atual.
- Trata entradas inválidas e solicita novas entradas até que valores válidos sejam fornecidos.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Copie o código abaixo e cole em um arquivo Python (por exemplo, `calcular_idade.py`).
3. Execute o arquivo Python.

```python
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


       ## Requisitos
          Python 3.x

       ## Contribuições
          Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

       ##Licença
       Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

