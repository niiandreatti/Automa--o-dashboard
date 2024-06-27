%%writefile app.py
import streamlit as st
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Definindo o título e estilo da página
st.title('Bem-vindo')
st.markdown('<hr>', unsafe_allow_html=True)  # Linha horizontal para separação visual

# Seção de descrição
st.header('Descrição do Aplicativo')
st.write("""
Este é um aplicativo Streamlit que simula visualizar gráficos. Aqui você pode
carregar um arquivo CSV O para visualizar gráficos.
""")
st.markdown('<br>', unsafe_allow_html=True)  # Espaço em branco

# Upload de arquivo e visualização dos gráficos
file = st.file_uploader("Suba seu arquivo CSV aqui", type=['csv'])

if file:
    if file.type == 'text/csv':
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='latin1')

        # Verificar se o DataFrame não está vazio antes de plotar os gráficos
        if not df.empty:
            st.markdown('<hr>', unsafe_allow_html=True)  # Linha horizontal para separação visual
            st.header('Visualização de Dados')
            st.subheader('Gráfico de Vendas por Mês')
            st.line_chart(df.set_index('mês'))
            st.subheader('Gráfico de Vendas por Mês')
            st.bar_chart(df.set_index('mês'))
        else:
            st.warning('O arquivo CSV está vazio ou não contém dados válidos.')

    else:
        st.error('Formato de arquivo não suportado. Por favor, envie um arquivo CSV.')

# Rodapé da landing page
st.markdown('<hr>', unsafe_allow_html=True)  # Linha horizontal para separação visual
st.markdown("""
*Este aplicativo foi desenvolvido utilizando Streamlit e Python.*
*Para mais informações ou sugestões, entre em contato conosco.*
*© 2024 Seu Nome ou Empresa. Todos os direitos reservados.*
""")
