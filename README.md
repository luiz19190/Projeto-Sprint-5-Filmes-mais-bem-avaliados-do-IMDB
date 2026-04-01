# 🎬 Dashboard de Análise de Dados: Top Filmes IMDB

Este projeto é um aplicativo web interativo desenvolvido para a **Sprint 5** do curso de DA da Tripleten. O objetivo é explorar as tendências do cinema mundial através de uma base de dados dos filmes mais bem avaliados do IMDB.

---

### 📝 Descrição do Projeto
O dashboard oferece uma visão analítica sobre a evolução da qualidade cinematográfica, popularidade de gêneros e o impacto financeiro de premiações como o Oscar. Ele permite que o usuário interaja com os dados através de filtros dinâmicos na barra lateral.

### 🚀 Funcionalidades Principais
* **Evolução Histórica (Fixo):** Um gráfico de linha que mostra a maior nota atingida no IMDB para cada ano, identificando os "anos de ouro" do cinema e variações ao logo de cada ano.
* **Distribuição de Notas:** Histograma interativo para analisar a concentração de avaliações dos filmes.
* **Relação Votos vs. Qualidade:** Gráfico de dispersão com escala logarítmica para visualizar se filmes populares são necessariamente os mais bem avaliados.
* **Top 15 Gêneros:** Ranking horizontal dos gêneros mais frequentes na lista de sucessos.
* **Análise do "Efeito Oscar":** Comparação entre a média de faturamento de filmes vencedores e não vencedores da Academia.

### 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem principal.
* **Pandas**: Manipulação e limpeza de dados.
* **Streamlit**: Criação da interface web e interatividade.
* **Plotly Express**: Geração de gráficos dinâmicos e responsivos.
* **Github**: onde ficou o repósitorio e foi tudo postado.

---

### 📂 Estrutura de Arquivos
* `app.py`: Código principal do dashboard.
* `data/`: Pasta contendo o dataset CSV.
* `notebooks/`: Notebooks Jupyter utilizados para a fase de exploração (EDA).
* `.streamlit/`: Configurações de servidor para o deploy no Render.