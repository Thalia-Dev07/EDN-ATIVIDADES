"""
Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres 
e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida 
ou o usuário digite 'sair'.

"""

comprimento_min = 8

print("--- Verificador de senha forte ---")
print("A senha deve ter pelo menos 8 caracteres e um número. Digite 'sair' para encerrar.")

while True:
    senha = input("Digite sua senha: ").strip()

    if senha.lower() == 'sair':
        print("Verificação de senha encerrada.")
        break
        
    if len(senha) < comprimento_min:
        print(f"Senha fraca: Deve ter pelo menos {comprimento_min} caracteres.")
        continue

    if not any(c.isdigit() for c in senha):
        print("Senha fraca: Deve conter pelo menos um número.")
        continue

    print("\nSUCESSO! Senha forte e válida registrada.")
    break