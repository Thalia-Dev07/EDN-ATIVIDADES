
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado na conta total e porcentagem.

    Parâmetros:
        valor_conta: O valor total da conta.
        porcentagem_gorjeta: A porcentagem desejada (ex: 10 para 10%).

    Retorna:
        O valor da gorjeta a ser adicionada.
    """
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

def programa_gorjeta():
    """Programa que coleta entradas e exibe o cálculo."""
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta desejada (ex: 15): "))
        
        if valor_conta < 0 or porcentagem < 0:
            print("Valores de conta e porcentagem não podem ser negativos.")
            return

        gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        
        valor_total = valor_conta + gorjeta

        print(f"\n--- Cálculo da Gorjeta ({porcentagem:.1f}%) ---")
        print(f"Valor da Gorjeta: R$ {gorjeta:.2f}")
        print(f"Valor Total a Pagar: R$ {valor_total:.2f}")

    except ValueError:
        print("Erro: Digite apenas valores numéricos válidos.")

programa_gorjeta()