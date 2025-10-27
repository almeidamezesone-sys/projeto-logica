#importando bibliotecas e frameworks
import pandas as pd 
import os
from openpyxl import load_workbook
import streamlit as st


#classe Funcionárias
class Funcionarios():
    """Classe responsável pelo cadastro dos funcionários e criação do arquivo principal. """

    #função inicial da classe
    def __init__(self):
        self.pathArquivo = "funcionarios.xlsx"
        
    #função que gera o funcionário apartir do seu nome e cargo, salva-o em um dicionário e chama a função salvarFuncionário
    def Gerador_funcionarios(self,):        
        # Inicializa as variáveis no session_state se não existirem
        # Cria os widgets ligados ao session_state
        nome = st.text_input("Digite seu nome:", key="nome_input")
        cargo = st.text_input("Digite seu cargo:", key="cargo_input")
        funcionario = [{"nome": nome, "cargo": cargo}]
        if st.button("Cadastrar"):
            self.salvarFuncionarios(funcionario)
    
    def salvarFuncionarios(self, funcionario):
        df_new = pd.DataFrame(funcionario)
        aba = "Funcionários"
        if not os.path.exists(self.pathArquivo):
            with pd.ExcelWriter(self.pathArquivo, engine="openpyxl") as writer:
                df_new.to_excel(writer, sheet_name=aba, index=False)
            st.write("✅ Arquivo criado. Dados salvos com sucesso!")
        else:
            with pd.ExcelWriter(self.pathArquivo, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                try:
                    df_existente = pd.read_excel(self.pathArquivo, sheet_name=aba)
                    df_atualizado = pd.concat([df_existente, df_new], ignore_index=True)
                except ValueError:
                    df_atualizado = df_new

                df_atualizado.to_excel(writer, sheet_name=aba, index=False)
            st.write(f"✅ Registro adicionado à aba '{aba}' com sucesso!")
