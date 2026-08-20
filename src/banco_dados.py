import pandas as pd
import sqlite3
import os

# 1. Indicando os caminhos dos arquivos
caminho_csv = os.path.join('data', 'alunos_limpos.csv')
caminho_banco = os.path.join('data', 'escola.db')

print("Lendo o arquivo CSV limpo...")
df_alunos = pd.read_csv(caminho_csv)

# 2. Conectando ao banco de dados SQLite
# (Se o arquivo escola.db não existir, ele é criado automaticamente)
conn = sqlite3.connect(caminho_banco)

# 3. Carregando os dados do Pandas para uma tabela SQL chamada 'tb_avaliacoes'
df_alunos.to_sql('tb_avaliacoes', conn, if_exists='replace', index=False)

print("Tabela 'tb_avaliacoes' criada com sucesso no banco SQLite!")

# 4. Executando uma consulta SQL para testar (alunos com média >= 7.0)
query_sql = "SELECT aluno_id, media_final, classificacao FROM tb_avaliacoes WHERE media_final >= 7.0"
df_aprovados = pd.read_sql_query(query_sql, conn)

print("\n--- RESULTADO DA CONSULTA SQL (Aprovados com Média >= 7.0) ---")
print(df_aprovados)

# 5. Fechando a conexão
conn.close()