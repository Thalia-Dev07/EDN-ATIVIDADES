"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter 
informações de uma pessoa, com campos nome, idade e cidade.

"""

import json

def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("Dados gravados com sucesso!")

def ler_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados


# Exemplo de uso
pessoa = {
    "nome": "Elizate",
    "idade": 36,
    "cidade": "Belém"
}

arquivo = "pessoa.json"

# Grava o JSON
escrever_json(arquivo, pessoa)

# Lê o JSON
dados_lidos = ler_json(arquivo)

print("Dados lidos do JSON:")
print(dados_lidos)