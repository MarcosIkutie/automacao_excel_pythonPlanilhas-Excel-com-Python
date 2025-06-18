import os
import pandas as pd

CAMINHO_INPUT = 'input'

def ler_e_consolidar_planilhas():
    planilhas = []

    for arquivo in os.listdir(CAMINHO_INPUT):
        if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
            caminho_arquivo = os.path.join(CAMINHO_INPUT, arquivo)
            df = pd.read_excel(caminho_arquivo)
            planilhas.append(df)

    df_consolidado = pd.concat(planilhas, ignore_index=True)
    return df_consolidado

# Esse trecho abaixo é apenas para testes individuais
if __name__ == '__main__':
    df = ler_e_consolidar_planilhas()
    print("Prévia da consolidação:")
    print(df.head())
