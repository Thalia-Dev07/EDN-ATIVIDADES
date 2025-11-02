# 1- Conversor de Moeda
"""
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

"""

valor_reais = 100
taxa_dolar = 5.6
taxa_euro = 6.6

valor_dolar = round(valor_reais / taxa_dolar, 2) 
valor_euro = round(valor_reais / taxa_euro, 2)

print(f"{valor_reais} reais convertido em dólar: $ {valor_dolar}")
print(f"{valor_reais} reais convertido em euro: € {valor_euro}")



