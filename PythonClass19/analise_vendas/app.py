import streamlit as st
import pandas as pd

df = pd.read_csv('vendas.csv')

st.write(df)