import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv('vendas.csv')

df = load_data()

# df['data'] = pd.to_datetime(df['data']).dt.strftime('%d/%m/%Y')
st.title('Dashboard de Vendas Interativo')

# ---- BARRA LATERAL DE FILTROS -----
st.sidebar.header('Filtros')

filtro_1 = st.sidebar.selectbox('Selecione uma coluna para filtrar:', df.columns)
valores_unicos_1 = df[filtro_1].unique()
valor_1 = st.sidebar.selectbox(f'Selecione um valor para filtrar em {filtro_1}:', valores_unicos_1)

df_filtrado = df[df[filtro_1] == valor_1] # --- PRIMEIRO FILTRO ---

filtro_2 = st.sidebar.selectbox('Selecione uma coluna para filtrar:', df.columns.difference([filtro_1]))
valores_unicos_2 = df_filtrado[filtro_2].unique()
valor_2 = st.sidebar.selectbox(f'Selecione um valor para filtrar em {filtro_2}:', valores_unicos_2)

df_filtrado = df_filtrado[df_filtrado[filtro_2] == valor_2]  # -- SEGUNDO FILTRO ---

st.header('Visualização de Dados Filtrados')
st.write(df_filtrado)

if 'data' in df.columns:
    df['data'] = pd.to_datetime(df['data'])

# ---- ---- ---- ---- ---- ---- ---- 

# Seção de gráficos
st.header('Gráficos Interativos')

# Seleção do tipo de gráfico
tipo_grafico = st.selectbox('Selecione o tipo de gráfico', ['Barra', 'Linha', 'Dispersão', 'Histograma'])

# Função para criar gráficos
def criar_grafico(tipo):
    if tipo == 'Barra':
        fig = px.bar(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Linha':
        fig = px.line(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Dispersão':
        fig = px.scatter(df_filtrado, x='vendas', y='quantidade', color='categoria', title='Dispersão de Vendas e Quantidade')
    elif tipo == 'Histograma':
        fig = px.histogram(df_filtrado, x='vendas', color='categoria', title='Histograma de Vendas')
    st.plotly_chart(fig)

# Criar o gráfico selecionado
criar_grafico(tipo_grafico)

# Exibir as métricas
st.header('Métricas de Vendas')
st.metric('Total de Vendas', f'R$ {df_filtrado["vendas"].sum():,.2f}')
st.metric('Quantidade Total de Produtos Vendidos', int(df_filtrado['quantidade'].sum()))