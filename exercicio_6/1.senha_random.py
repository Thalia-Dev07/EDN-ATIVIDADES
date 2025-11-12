import random
import string

def gerar_senha_aleatoria():
    """
    Gera uma senha aleatória com base no comprimento fornecido.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    print("--- Gerador de Senhas Aleatórias ---")

    while True:
        try:
            comprimento = int(input("Digite o número de caracteres desejado para a senha (mínimo 8): "))
            
            if comprimento < 8:
                print("O comprimento mínimo recomendado é 8. Tente novamente.")
                continue
            
            senha = ''.join(random.choices(caracteres, k=comprimento))
            
            print(f"\nSua senha aleatória gerada é: {senha}")
            break
            
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o comprimento.")

gerar_senha_aleatoria()