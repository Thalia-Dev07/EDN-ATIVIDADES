"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

"""

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  
    return idade_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
print(f"Sua idade aproximada em dias é: {calcular_idade_em_dias(ano_nascimento)} dias")