import pandas as pd
import sys
import os

# Garante que o diretório atual esteja no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from leitura_consolidacao import ler_e_consolidar_planilhas
from limpeza import limpar_dados
from padronizacao import padronizar_colunas


def salvar_arquivo(df, caminho_saida='output/resultado_consolidado.xlsx'):
    # Cria a pasta de saída, se não existir
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    # Salva o DataFrame no caminho especificado
    df.to_excel(caminho_saida, index=False)
    print(f"✅ Arquivo salvo em: {caminho_saida}")


if __name__ == '__main__':
    df = ler_e_consolidar_planilhas()
    df = limpar_dados(df)
    df = padronizar_colunas(df)

    salvar_arquivo(df)
