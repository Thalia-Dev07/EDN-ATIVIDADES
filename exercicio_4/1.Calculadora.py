while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            
            resultado = None

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError 
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

        except ValueError as e:
            if "Operação inválida" in str(e):
                print(f"Erro: {e}. Por favor, use +, -, * ou /.")
            else:
                print("Erro de entrada: Digite apenas números válidos.")
            continue
        
        except ZeroDivisionError:
            print("Erro de operação: Não é possível dividir por zero.")
            continue
        
        except Exception:
            print("Ocorreu um erro inesperado. Tente novamente.")
            continue
        
        print(f"\nResultado de {num1} {operacao} {num2} = {resultado}")
        break