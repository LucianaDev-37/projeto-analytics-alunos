# 📊 Analytics de Alunos (Projeto de Ponta a Ponta)

Este projeto mostra como pegar dados brutos de alunos em uma planilha Excel, organizar tudo com Python, salvar em um banco de dados SQL e criar um painel interativo na web.

## 🛠️ Ferramentas Usadas
* **Python**: Linguagem principal do projeto.
* **Pandas**: Para ler, limpar e organizar os dados.
* **SQLite / SQL**: Para guardar os dados em um banco relacional e fazer consultas.
* **Streamlit**: Para construir a tela com gráficos e indicadores.
* **Git e GitHub**: Para controlar as versões e salvar o código com segurança.

## 📁 O que tem em cada pasta?
* `data/`: Guarda os arquivos do projeto (a planilha original, o arquivo limpo e o banco de dados).
* `src/tratamento.py`: Limpa a planilha Excel e arruma os nomes das colunas.
* `src/banco_dados.py`: Salva os dados limpos no banco SQLite e roda pesquisas em SQL.
* `src/app.py`: Cria a tela interativa com indicadores e gráficos.

## 🚀 Como Rodar o Projeto na Sua Máquina

1. Baixe o projeto:
```bash
git clone [https://github.com/LucianaDev-37/projeto-analytics-alunos.git](https://github.com/LucianaDev-37/projeto-analytics-alunos.git)

1-Entre na pasta do projeto:

cd projeto-analytics-alunos

2-Crie e ative o ambiente virtual:

python3 -m venv .venv
source .venv/bin/activate

3-Instale as bibliotecas necessárias:

pip install pandas openpyxl streamlit

4-Rode a limpeza dos dados e crie o banco de dados:

python src/tratamento.py
python src/banco_dados.py

5-Abra o painel no navegador:

streamlit run src/app.py