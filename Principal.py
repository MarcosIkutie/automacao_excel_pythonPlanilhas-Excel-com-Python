from leitura_consolidacao import ler_e_consolidar_planilhas
from limpeza import limpar_dados
from padronizacao import padronizar_colunas
import os

CAMINHO_OUTPUT = 'output/consolidado.xlsx'
os.makedirs('output', exist_ok=True)

def salvar_arquivo(df, caminho_saida):
    df.to_excel(caminho_saida, index=False)
    print(f"✅ Arquivo final salvo em: {caminho_saida}")

if __name__ == '__main__':
    df = ler_e_consolidar_planilhas()
    df = limpar_dados(df)
    df = padronizar_colunas(df)
    salvar_arquivo(df, CAMINHO_OUTPUT)
