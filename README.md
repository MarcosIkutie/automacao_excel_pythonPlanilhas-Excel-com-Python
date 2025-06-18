# automacao_excel_python
# Projeto Automação: Consolidação e Limpeza de Planilhas Excel

## Descrição

Este projeto automatiza a consolidação, limpeza e padronização de dados extraídos de múltiplas planilhas Excel, utilizando Python e bibliotecas como `pandas`.

## Estrutura do Projeto

- `input/` - Pasta onde as planilhas Excel devem ser colocadas para serem processadas.
- `output/` - Pasta onde o arquivo final consolidado será salvo.
- `leitura_consolidacao.py` - Script para ler e consolidar os arquivos Excel.
- `limpeza.py` - Funções para limpeza dos dados (remoção de duplicatas e linhas vazias).
- `padronizacao.py` - Padronização dos nomes das colunas.
- `salvar_resultado.py` - Script principal que integra todas as etapas e salva o resultado final.

## Como Usar

1. Coloque suas planilhas Excel dentro da pasta `input/`.
2. Execute o script principal:

```bash
python salvar_resultado.py

