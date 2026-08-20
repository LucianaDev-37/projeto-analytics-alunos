import streamlit as st
import pandas as pd
import sqlite3
import os

# Configuração da página do Streamlit
st.set_page_config(page_title="Dashboard de Alunos", layout="wide")

st.title("📊 Painel de Desempenho dos Alunos")
st.markdown("Consulta em tempo real ao banco de dados SQLite (`escola.db`)")

# Conectar ao banco SQLite
caminho_banco = os.path.join('data', 'escola.db')
conn = sqlite3.connect(caminho_banco)

# Ler os dados via SQL
query = "SELECT * FROM tb_avaliacoes"
df = pd.read_sql_query(query, conn)
conn.close()

# Métricas principais (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total de Alunos", len(df))
col2.metric("Média Geral da Turma", round(df['media_final'].mean(), 2))
col3.metric("Maior Média", df['media_final'].max())

st.divider()

# Exibir a Tabela de Dados do Banco
st.subheader("📋 Tabela de Avaliações")
st.dataframe(df, use_container_width=True)

# Gráfico de distribuição das classificações
st.subheader("📈 Distribuição por Classificação")
contagem_classificacao = df['classificacao'].value_counts()
st.bar_chart(contagem_classificacao)