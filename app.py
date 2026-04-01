import streamlit as st
import pandas as pd
import plotly.express as px

# Título e Cabeçalho
st.header('🎬 Dashboard de Análise de Filmes IMDB')
st.write('Explore os dados dos melhores filmes por ano e descubra tendências cinematográficas.')

# Lendo os dados
imdb = pd.read_csv('data/world_imdb_movies_top_movies_per_year.csv')
# Criando a coluna de gênero principal que testei no notebook
imdb['genre_principal'] = imdb['genre'].str.split(',').str[0]
# finanças
df_financeiro = imdb.dropna(subset=['budget', 'gross_world_wide'])

# Criando uma visualização da evolução da nota máxima do IMDB por ano para chamar atenção do usuário
st.subheader("📈 A Evolução da Qualidade Máxima")
# Agrupando por ano e pegando a nota máxima
notas_por_ano = imdb.groupby('year')['rating_imdb'].max().reset_index()

# Criando o gráfico de linha
fig_linha = px.line(notas_por_ano,
                    x="year",
                    y="rating_imdb",
                    title="Evolução da Maior Nota do IMDB por Ano",
                    markers=True,
                    labels={'rating_imdb': 'Nota Máxima', 'year': 'Ano'})

fig_linha.update_yaxes(range=[7, 10])

# (sem botão/checkbox)
st.plotly_chart(fig_linha, use_container_width=True)

st.divider()

# Criar caixas de seleção para o usuário escolher o gráfico
st.sidebar.header("Escolha os Gráficos")

build_histogram = st.sidebar.checkbox('Criar um histograma')
build_scatter = st.sidebar.checkbox('Criar um gráfico de dispersão')
show_genres = st.sidebar.checkbox('Top 15 Gêneros')
show_oscar = st.sidebar.checkbox('Impacto do Oscar no Faturamento')

# Histograma
if build_histogram:
    st.write('Exibindo a distribuição das notas dos filmes no IMDB')

    fig_hist = px.histogram(imdb, x="rating_imdb",
                            title="Distribuição das Notas IMDB",
                            color_discrete_sequence=['indianred'])

    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de Dispersão
if build_scatter:
    st.write('Relacionando o número de votos com a nota dos filmes')
    fig_scatter = px.scatter(imdb, x="vote", y="rating_imdb",
                             color="genre_principal",
                             hover_name="title",
                             log_x=True,  # alteração extra para melhorar a visualização dos dados
                             title="Popularidade (Votos) vs. Qualidade (Nota)")

    st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico de Gêneros (Horizontal)
if show_genres:
    st.subheader("Quais gêneros dominam o Top do IMDB?")
    top_generos = imdb['genre_principal'].value_counts().nlargest(
        15).reset_index()

    fig_gen = px.bar(top_generos,
                     y='genre_principal',
                     x='count',
                     title="Top 15 Gêneros Mais Frequentes",
                     labels={'count': 'Número de Filmes',
                             'genre_principal': 'Gênero'},
                     color='count',
                     color_continuous_scale='Viridis',
                     orientation='h')

    fig_gen.update_layout(
        yaxis={'categoryorder': 'total ascending'}, height=500)
    st.plotly_chart(fig_gen, use_container_width=True)


# Gráfico do Oscar (Faturamento)
if show_oscar:
    st.subheader("O 'Selo Oscar' aumenta o faturamento?")
    df_oscar_money = df_financeiro.groupby(
        'oscar')['gross_world_wide'].mean().reset_index()

    # Melhorando a legenda do gráfico
    df_oscar_money['oscar'] = df_oscar_money['oscar'].map({0: 'Não', 1: 'Sim'})

    fig_oscar = px.bar(df_oscar_money,
                       x='oscar',
                       y='gross_world_wide',
                       color='oscar',
                       title="Média de Faturamento Mundial: Com Oscar vs. Sem Oscar",
                       labels={
                           'gross_world_wide': 'Faturamento Médio ($)', 'oscar': 'Ganhou Oscar?'},
                       text_auto=True,
                       # Prata e Ouro!
                       color_discrete_map={'Não': '#C0C0C0', 'Sim': '#FFD700'})

    st.plotly_chart(fig_oscar, use_container_width=True)
