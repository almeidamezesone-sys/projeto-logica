import streamlit as st
from funcionariosSt import Funcionarios

# Inicializa a classe
if "callFunc" not in st.session_state:
    st.session_state.callFunc = Funcionarios()

# Flag para mostrar ou não os inputs
if "mostrar_func" not in st.session_state:
    st.session_state.mostrar_func = False

st.title("Registro de Ocorrências")

# Botão ativa a flag
if st.button("Cadastrar Funcionários"):
    st.session_state.mostrar_func = True

# Chama a função da classe **somente se a flag estiver ativa**
if st.session_state.mostrar_func:
    st.session_state.callFunc.Gerador_funcionarios()
