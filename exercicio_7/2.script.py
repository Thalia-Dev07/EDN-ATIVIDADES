"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, 
como colunas Nome, Idade e Cidade.

"""

import csv

def escrever_csv(nome_arquivo):
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 28, "Belém"],
        ["Carlos", 35, "Marabá"],
        ["Mariana", 22, "Santarém"]
    ]

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

escrever_csv("pessoas.csv") # Exemplo de uso