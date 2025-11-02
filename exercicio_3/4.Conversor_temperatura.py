# 4- Conversor de Temperatura   
"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (C, F, K): ").upper()
destino = input("Informe a unidade de destino (C, F, K): ").upper()

if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura
elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura
elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura
else:
    print("Unidade inválida!")
    resultado = None

if resultado is not None:
    print("Temperatura convertida:", round(resultado, 2), destino)
