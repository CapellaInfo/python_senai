import streamlit as st
import pandas as pd

df1 = pd.read_csv("vendas.csv")

# Seleção de intervalo de datas
st.sidebar.header('Filtro por Data')
data_inicio = pd.Timestamp(st.sidebar.date_input('Data Início', value=pd.to_datetime('2023-01-01')))
data_fim = pd.Timestamp(st.sidebar.date_input('Data Fim', value=pd.to_datetime('2023-12-31')))

df2 = df1[(pd.to_datetime(df1['data']) >= data_inicio) & (pd.to_datetime(df1['data']) <= data_fim)]

st.title('Dashboard de Vendas Interativo')
st.write(df2)






