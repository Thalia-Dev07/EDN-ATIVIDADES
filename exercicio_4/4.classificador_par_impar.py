"""
Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar 
solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar 
se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares 
inseridos.

"""

pares = 0
impares = 0

print("--- Classificador Par/Ímpar ---")
print("Digite números inteiros. Digite 'fim' para encerrar.")

while True:
    entrada = input("Digite um número: ").strip().lower()

    if entrada == 'fim':
        break

    try:
        numero = int(entrada)
            
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1

    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro ou 'fim'.")
        continue

print("\n--- Resultado Final ---")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")