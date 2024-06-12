import streamlit as st
import pandas as pd
df = pd.read_csv('movies.csv')

st.write(df.head())

filtro = st.sidebar.selectbox('Selecione uma coluna para filtrar:', df.columns)

valores_unicos = df[filtro].unique()
valor = st.sidebar.selectbox('Selecione um valor para filtrar:', valores_unicos)

df_filtrado = df[df[filtro] == valor]
st.write(df_filtrado)
