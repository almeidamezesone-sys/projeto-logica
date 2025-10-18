from datetime import date, timedelta
import random as rd
import pandas as pd 
import os

def Acidente(dano, dias):
    if dias > 0:
        return "Acidente"
    else:
        return Incidente_quase_acidente(dano)
        
def Incidente_quase_acidente(dano):
    if dano == "Não":
        return "Quase acidente"
    else:
        return "Incidente"
    
def Teve_danos(dias):
    if dias == 0:
        return str(input("teve lesão? "))
    else:
        return "sim"

def Gerador_funcionarios():
    nome = str(input("Digite seu nome: "))
    cargo = str(input("Digite seu cargo: "))
    dias = int(input("Digite o numero de dias afastados: "))
    danos = Teve_danos(dias)
    ac_in_qa = Acidente(danos, dias)
    data_ocorrencia = str(input("Digite a data da ocorrencia: "))

    return{
        "Nome: ": nome,
        "Função: ": cargo,
        "Dias afastados: ": dias,
        "teve danos: ": danos,
        "tipo de acidente: ": ac_in_qa,
        "Data ocorrência: ": data_ocorrencia
    }
  
if __name__ == "__main__":
    while True:
        funcionarios = [Gerador_funcionarios()]
        
        print(f"{'Nome':<20} {'Função':<20} {'Dias afastados':<19} {'Teve danos':<19} {'Tipo de acidente':<19} {'Data ocorrência'}")
        print("-" * 90)

        for f in funcionarios:
            print(f"{f['Nome: ']:<20} {f['Função: ']:<20} {f['Dias afastados: ']:<20} {f['teve danos: ']:<19} {f['tipo de acidente: ']:<19} {f['Data ocorrência: ']}")

        print("-" * 90)

        print("\nArquivo 'funcionarios.xlsx' salvo com sucesso!")

        df_novo = pd.DataFrame(funcionarios)
        caminho_arquivo = "funcionarios.xlsx"

        try:
            if os.path.exists(caminho_arquivo):
                df_existente = pd.read_excel(caminho_arquivo)
                df_final = pd.concat([df_existente, df_novo], ignore_index=True)
                print(f"\n✅ Arquivo existente encontrado. Foram adicionados {len(df_novo)} novos registros.")
            else:
                df_final = df_novo
                print(f"\n🆕 Arquivo novo criado com {len(df_novo)} registros.")

            df_final.to_excel(caminho_arquivo, index=False)
            print(f"💾 Dados salvos em '{caminho_arquivo}' com sucesso!")

        except PermissionError:
            print("❌ Erro: O arquivo está aberto no Excel. Feche-o e tente novamente.")
        except FileNotFoundError:
            print("❌ Erro: Caminho do arquivo não encontrado.")
        except Exception as e:
            print(f"⚠️ Ocorreu um erro inesperado: {e}")
