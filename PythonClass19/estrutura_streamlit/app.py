from matplotlib.backend_bases import button_press_handler
import streamlit as st
import pandas as pd

st.title('Título da Aplicação')
st.header('Cabeçalho Secundário')
st.subheader('Subcabeçalho Terciário')
st.text('Este é um texto simples.')
st.markdown('**Este é um texto em negrito usando Markdown.**')

st.sidebar.title('Título na Barra Lateral')
st.sidebar.markdown('Texto na barra lateral.')

col1, col2 = st.columns(2)
col1.write('Este é o conteúdo da primeira coluna.')
col2.write('Este é o conteúdo da segunda coluna.')

if col1.button('Clique aqui'):
    col1.write('Botão clicado!')

if col2.checkbox('Marque-me'):
    col2.write('Caixa marcada!')

age = st.slider('Selecione sua idade', 0, 100, 20)
st.write(f'Sua idade é: {age}')

nome = st.text_input('Digite seu nome')
st.write(f'Seu nome é: {nome}')

data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)
st.table(df)

json_data = {'chave': 'valor', 'lista': [1, 2, 3]}
st.json(json_data)

number1 = st.number_input('Primeiro Número: ')
number2 = st.number_input('Segundo Número: ')

soma = st.button("Soma") 
sub = st.button("Subtração")
mult = st.button("Multiplicação")
div = st.button("Divisão")

operations = st.selectbox("Escolha a Operação", ("+", "-", "*", "/"))

if soma:
    result = (number1) + (number2)
    st.write("Resultado da Soma:", result)
elif sub:
    result = (number1) - (number2)
    st.write("Resultado da Subtração:", result)
elif mult:
    result = (number1) * (number2)
    st.write("Resultado da Multiplicação:", result)
elif div:
    if number2 == 0:
        st.write("Não é possível dividir por zero")
    else:
        result = (number1) / (number2)
        st.write("Resultado da Divisão:", result)

