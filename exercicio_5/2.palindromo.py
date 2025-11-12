"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, 
ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""

def verifica_palindromo():
    palavra_original = input("Digite uma palavra ou frase: ").lower().replace(" ", "")

    palavra_invertida = palavra_original[::-1]

    if palavra_original == palavra_invertida:
        print(f"A palavra/frase '{palavra_original}' É um palíndromo.")
    else:
        print(f"A palavra/frase '{palavra_original}' não é um palíndromo.")
        print(f"(Lida ao contrário: {palavra_invertida})")