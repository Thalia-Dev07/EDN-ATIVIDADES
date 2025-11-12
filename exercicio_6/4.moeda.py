import requests
from datetime import datetime

def consultar_cotacao():
    """
    Consulta a cotação de uma moeda em relação ao Real (BRL) usando a AwesomeAPI.
    """
    print("--- Consultor de Cotação de Moeda ---")
    moeda = input("Digite o código da moeda (Ex: USD, EUR, GBP): ").strip().upper()

    par_moeda = f"{moeda}BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        
        if par_moeda not in dados:
            print(f"Erro: Cotação para {moeda}/BRL não encontrada ou código inválido.")
            return

        cotacao = dados[par_moeda]
        
        timestamp = int(cotacao['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print(f"\n--- Cotação {cotacao['name']} ---")
        print(f"Compra (Valor Atual): R$ {float(cotacao['bid']):.4f}")
        print(f"Máximo (Últimas 24h): R$ {float(cotacao['high']):.4f}")
        print(f"Mínimo (Últimas 24h): R$ {float(cotacao['low']):.4f}")
        print(f"Última Atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print(f"Erro: Falha na conexão com a API de cotação.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")

consultar_cotacao()