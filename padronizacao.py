import pandas as pd
import sys
import os

# Garante que o diretório atual esteja no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações dos outros módulos
from leitura_consolidacao import ler_e_consolidar_planilhas
from limpeza import limpar_dados

# Função de padronização
def padronizar_colunas(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

# Execução completa
if __name__ == '__main__':
    df = ler_e_consolidar_planilhas()
    df = limpar_dados(df)
    df = padronizar_colunas(df)

    print("📋 Colunas padronizadas:")
    print(df.columns)
