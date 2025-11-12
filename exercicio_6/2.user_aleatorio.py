import requests

def gerar_perfil_aleatorio():
    """
    Busca e exibe um perfil de usuário aleatório da Random User Generator API.
    """
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 

        dados = resposta.json()
        
        usuario = dados['results'][0] 
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("\n--- Perfil de Usuário Aleatório Gerado ---")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"\nErro ao conectar com a API: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

gerar_perfil_aleatorio()