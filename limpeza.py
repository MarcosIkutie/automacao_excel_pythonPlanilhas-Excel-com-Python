import pandas as pd

def limpar_dados(df):
    # Remove linhas completamente vazias
    df = df.dropna(how='all')

    # Remove duplicatas
    df = df.drop_duplicates()

    return df

# Teste isolado
if __name__ == '__main__':
    from leitura_consolidacao import ler_e_consolidar_planilhas

    df = ler_e_consolidar_planilhas()
    df_limpo = limpar_dados(df)

    print("✅ Dados limpos:")
    print(df_limpo.head())
