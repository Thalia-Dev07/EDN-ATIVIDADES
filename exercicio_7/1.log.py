"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.

"""

import re
import statistics

def analisar_log(arquivo):
    tempos = []

    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            match = re.search(r'(\d+\.\d+)', linha)
            if match:
                tempos.append(float(match.group(1)))

    if not tempos:
        raise ValueError("Nenhum valor de tempo encontrado no arquivo.")

    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)

    return media, desvio_padrao


# Exemplo de uso
arquivo_log = "treinamento.log"  # nome do arquivo
media, desvio = analisar_log(arquivo_log)

print(f"Média dos tempos: {media:.4f} segundos")
print(f"Desvio padrão: {desvio:.4f} segundos")