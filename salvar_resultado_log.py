import pandas as pd
import sys
import os
import logging

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Garante que o diretório atual esteja no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from leitura_consolidacao import ler_e_consolidar_planilhas
from limpeza import limpar_dados
from padronizacao import padronizar_colunas

def salvar_arquivo(df, caminho_saida='output/resultado_consolidado.xlsx'):
    try:
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        df.to_excel(caminho_saida, index=False)
        logging.info(f"Arquivo salvo em: {caminho_saida}")
    except Exception as e:
        logging.error(f"Erro ao salvar arquivo: {e}")
        raise

if __name__ == '__main__':
    logging.info("Iniciando processo de consolidação e limpeza")
    df = ler_e_consolidar_planilhas()
    logging.info(f"Planilhas consolidadas: {len(df)} linhas")

    df = limpar_dados(df)
    logging.info(f"Dados limpos: {len(df)} linhas restantes")

    df = padronizar_colunas(df)
    logging.info(f"Colunas padronizadas: {list(df.columns)}")

    salvar_arquivo(df)
    logging.info("Processo finalizado com sucesso")
