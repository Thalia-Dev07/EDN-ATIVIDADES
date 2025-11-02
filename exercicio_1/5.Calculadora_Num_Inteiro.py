# 5- Calculadora de Número Inteiro
"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""

A = int(input("Digite um número para A: "))
B = int(input("Digite um número para B: "))
C = int(input("Digite um número para C: "))
D = int(input("Digite um número para D: "))

DIFERENCA = (A*B) - (C*D)

print(f"DIFERENCA = {DIFERENCA}")