import requests

def consultar_cep():
    """
    Consulta o endereço a partir de um CEP usando a API ViaCEP.
    """
    print("--- Consultor de CEP (ViaCEP) ---")
    cep = input("Digite o CEP para consulta (somente números): ").strip()
    
    if not cep.isdigit() or len(cep) != 8:
        print("Erro: CEP inválido. Deve conter exatamente 8 dígitos numéricos.")
        return
        
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        if 'erro' in dados and dados['erro']:
            print(f"Erro: CEP {cep} não encontrado.")
            return

        print("\n--- Endereço Encontrado ---")
        print(f"CEP: {dados.get('cep', 'N/A')}")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade/UF: {dados.get('localidade', 'N/A')}/{dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException:
        print("Erro: Falha na conexão com a API ViaCEP.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

consultar_cep()