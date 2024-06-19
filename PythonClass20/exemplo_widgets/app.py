import streamlit as st
import pandas as pd

df = pd.read_csv("vendas.csv")

# Seleção de intervalo de datas
st.sidebar.header('Filtro por Data')
data_inicio = pd.Timestamp(st.sidebar.date_input('Data Início', value=pd.to_datetime('2023-01-01')))
data_fim = pd.Timestamp(st.sidebar.date_input('Data Fim', value=pd.to_datetime('2023-12-31')))

df2 = df[(pd.to_datetime(df['data']) >= data_inicio) & (pd.to_datetime(df['data']) <= data_fim)]

st.title('Dashboard de Vendas Interativo')
st.write(df2)

# Slider para selecionar intervalo de valores de vendas
st.sidebar.header('Filtro por Vendas')
vendas_min, vendas_max = st.sidebar.slider('Vendas', float(0), float(1000), (float(df['vendas'].min()), float(df['vendas'].max())))


# Filtrar dados pelo intervalo de valores de vendas
df_filtrado2 = df[(df['vendas'] >= vendas_min) & (df['vendas'] <= vendas_max)]


st.write(df_filtrado2)







