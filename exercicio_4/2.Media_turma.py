"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve 
continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O 
programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

"""

soma_notas = 0
total_notas = 0

print("--- Calculadora de Média da Turma ---")
print("Digite as notas (0 a 10). Digite 'fim' para calcular a média.")

while True:
    entrada = input("Digite a nota: ").strip().lower()
        
    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
            
        if 0 <= nota <= 10:
            soma_notas += nota
            total_notas += 1
            print(f"Nota {nota} registrada.")
        else:
            print("Nota inválida: Deve estar entre 0 e 10.")
            continue

    except ValueError:
        print("Erro: Entrada inválida. Digite um número ou 'fim'.")
        continue

if total_notas > 0:
    media = soma_notas / total_notas
    print("\n--- Resultado ---")
    print(f"Total de notas registradas: {total_notas}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")