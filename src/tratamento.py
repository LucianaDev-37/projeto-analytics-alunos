import pandas as pd
import os

# 1. Indicando onde a planilha está salva (dentro da pasta data)
caminho_excel = os.path.join('data', 'classificacao-de-alunos.xlsx')

print("Carregando os dados da planilha...")
# 2. Ler a aba 'ALUNO' da planilha
df_raw = pd.read_excel(caminho_excel, sheet_name='ALUNO')

# 3. Remover linhas onde o nome do ALUNO está vazio (remove a linha do resumo final)
df_alunos = df_raw.dropna(subset=['ALUNO']).copy()

# 4. Mapear e renomear as colunas para o padrão do nosso banco de dados
colunas_manter = {
    'ALUNO': 'aluno_id',
    'EVA1': 'nota_eva1',
    'EVA2': 'nota_eva2',
    'EVA3': 'nota_eva3',
    'EVA4': 'nota_eva4',
    'MÉDIA': 'media_final',
    'CLASSIFICAÇÃO': 'classificacao'
}

# 5. Filtrar apenas as colunas acima e renomeá-las
df_limpo = df_alunos[list(colunas_manter.keys())].rename(columns=colunas_manter)

# 6. Exibir a tabela limpa no terminal
print("\n--- DADOS TRATADOS COM SUCESSO ---")
print(df_limpo)
# 7. Salvar os dados limpos em um arquivo CSV na pasta data/
caminho_saida = os.path.join('data', 'alunos_limpos.csv')
df_limpo.to_csv(caminho_saida, index=False, encoding='utf-8')

print(f"\nArquivo limpo salvo com sucesso em: {caminho_saida}")