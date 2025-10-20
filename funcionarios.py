#importando bibliotecas e frameworks
import pandas as pd 
import os
from openpyxl import load_workbook


#classe Funcionárias
class Funcionarios():
    """Classe responsável pelo cadastro dos funcionários e criação do arquivo principal. """

    #função inicial da classe
    def __init__(self):
        self.pathArquivo = "funcionarios.xlsx"
        self.Gerador_funcionarios()
        
    #função que gera o funcionário apartir do seu nome e cargo, salva-o em um dicionário e chama a função salvarFuncionário
    def Gerador_funcionarios(self,):
        nome = str(input("\nDigite seu nome: "))
        cargo = str(input("Digite seu cargo: "))
        funcionario = [{"nome": nome, "cargo": cargo}]
        self.salvarFuncionarios(funcionario)
        
    #cria o arquivo principal e salva o funcionário que foi passado anteriormente
    """def salvarFuncionarios(self,funcionario):
        df_novo = pd.DataFrame(funcionario)
        #testa a existência do arquivo principal, retornando erros e exceções
        try:
            if os.path.exists(self.pathArquivo):
                df_existente = pd.read_excel(self.pathArquivo)
                df_final = pd.concat([df_existente, df_novo], ignore_index=True)
                print(f"\n✅ Arquivo existente encontrado. Foram adicionados {len(df_novo)} novos registros.")
            else:
                df_final = df_novo
                print(f"\n🆕 Arquivo novo criado com {len(df_novo)} registros.")
            df_final.to_excel(self.pathArquivo, sheet_name="Funcionários", index=False)
            print(f"💾 Dados salvos em '{self.pathArquivo}' com sucesso!")
        except PermissionError:
            print("❌ Erro: O arquivo está aberto no Excel. Feche-o e tente novamente.")
        except FileNotFoundError:
            print("❌ Erro: Caminho do arquivo não encontrado.")
        except Exception as e:
            print(f"⚠️ Ocorreu um erro inesperado: {e}")
"""

    def salvarFuncionarios(self, funcionario):
        df_new = pd.DataFrame(funcionario)
        aba = "Funcionários"

        if not os.path.exists(self.pathArquivo):
            # Arquivo não existe → criar e adicionar a aba
            with pd.ExcelWriter(self.pathArquivo, engine="openpyxl") as writer:
                df_new.to_excel(writer, sheet_name=aba, index=False)
            print("✅ Arquivo criado. Dados salvos com sucesso!")
        else:
            with pd.ExcelWriter(self.pathArquivo, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                try:
                    df_existente = pd.read_excel(self.pathArquivo, sheet_name=aba)
                    df_atualizado = pd.concat([df_existente, df_new], ignore_index=True)
                except ValueError:
                    df_atualizado = df_new

                df_atualizado.to_excel(writer, sheet_name=aba, index=False)
            print(f"✅ Registro adicionado à aba '{aba}' com sucesso!")
