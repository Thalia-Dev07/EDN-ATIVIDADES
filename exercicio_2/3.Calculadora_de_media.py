# 3- Calculadora de Média Escolar 
"""
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

Nota 1: 7.5

Nota 2: 8.0

Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""

nota1 = 7.5
nota2 = 8
nota3 = 6.5

media = round((nota1 + nota2 + nota3)/3, 2)

print(f"Média Escolar")
print(f"Nota 1 do aluno: {nota1}")
print(f"Nota 2 do aluno: {nota2}")
print(f"Nota 3 do aluno: {nota3}")
print(f"Média: {media}")