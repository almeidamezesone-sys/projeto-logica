#importando bibliotecas e frameworks
import pandas as pd 
import os
from openpyxl import load_workbook

class Ocorrencias():
    """Classe responsável pelo registro de ocorrências e da criação de outra aba no arquivo principal"""

    #função de inicio da classe
    def __init__(self):
        self.pathArquivo = "funcionarios.xlsx"
        self.funcionario = {}
        self.calculosOcorrencia()
        self.salvarOcorrencias(self.funcionario)

    #função responsável por achar um funcionário já cadastrado e retornar o seu cargo.
    def acharFuncionario(self, nome):
        if not os.path.exists(self.pathArquivo):
            print("Arquivo de funcionários não encontrado.")
        df = pd.read_excel(self.pathArquivo)
        encontrado = df[df["nome"] == nome]
        if not encontrado.empty:
            funcionario = encontrado.iloc[0]  
            print("Funcionário encontrado:")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            """yn = input("Deseja prosseguir com ele? Y/N")
            if yn.lower() == "n":
                break"""
            self.funcionario = {
                "nome": funcionario["nome"],
                "cargo": funcionario["cargo"]
            } 
        else:
            print("Funcionário inexistente, cadastre-o primeiro.")

    def calculosOcorrencia(self):
        nome = str(input("Qual nome do funcionário?: "))
        if self.acharFuncionario(nome) != False:
            dias = int(input("Quantos dias afastados? "))

            if dias != 0:
                lesão = "Sim"
                tipo = "Acidente"
            else:
                lesão = input("Houve lesão?").lower()
                if lesão == "sim":  tipo = "Incidente"
                else: tipo = "Quase Acidente"


            data = str(input("Digite a data da ocorrencia: "))

            self.funcionario.update({
                "Dias afastados:":dias,
                "Lesão: ":lesão,
                "Tipo: ": tipo,
                "Data: ": data,
            })
            

    def salvarOcorrencias(self, funcionario):
        df_new = pd.DataFrame([funcionario])
        aba = "Ocorrências"

        if not os.path.exists(self.pathArquivo):
            # Arquivo não existe → criar e adicionar a aba
            with pd.ExcelWriter(self.pathArquivo, engine="openpyxl") as writer:
                df_new.to_excel(writer, sheet_name=aba, index=False)
            print("✅ Arquivo criado. Dados salvos com sucesso!")

        else:
            # Arquivo existe
            with pd.ExcelWriter(self.pathArquivo, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                try:
                    # Tenta ler a aba existente
                    df_existente = pd.read_excel(self.pathArquivo, sheet_name=aba)
                    df_atualizado = pd.concat([df_existente, df_new], ignore_index=True)
                except ValueError:
                    # Aba não existe → criar novo DataFrame
                    df_atualizado = df_new

                # Salva/atualiza a aba
                df_atualizado.to_excel(writer, sheet_name=aba, index=False)
            print(f"✅ Registro adicionado à aba '{aba}' com sucesso!")

