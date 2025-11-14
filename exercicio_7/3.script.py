"""
Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

"""

import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)

ler_csv("pessoas.csv") # Exemplo de uso