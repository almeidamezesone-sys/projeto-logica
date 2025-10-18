from datetime import date, timedelta
import random as rd
import pandas as pd 
import os

Lista_Primeiro_nome = ["Ana", "Beatriz", "Carla", "Daniela", "Eduarda",
            "Fernanda", "Gabriela", "Isabela", "Juliana", "Karina",
            "Larissa", "Marta", "Natalia", "Olga", "Paula",
            "Quésia", "Rafaela", "Sandra", "Tatiane", "Ursula",
            "Vera", "Wanda", "Ximena", "Yasmin", "Zélia",
            "Amanda", "Bruna", "Catarina", "Diana", "Eliane",
            "Fabiola", "Gisele", "Helena", "Ivana", "Jéssica",
            "Karla", "Lúcia", "Marina", "Nicole", "Priscila",
            "Renata", "Sofia", "Thais", "Verônica", "Walquíria",
            "Xuxa", "Yara", "Zuleika", "Adriana", "Betina","André",
            "Bruno","Astrubal", "Carlos", "Daniel", "Eduardo",
            "Felipe", "Gabriel", "Henrique", "Igor", "João",
            "Kaio", "Lucas", "Marcelo", "Natan", "Otávio",
            "Paulo", "Quirino", "Rafael", "Sérgio", "Thiago",
            "Ulisses", "Vinícius", "Wesley", "Xander", "Yago",
            "Zé", "Alexandre", "Bruno", "Cláudio", "Diego",
            "Erick", "Fabiano", "Gustavo", "Hugo", "Ismael",
            "Jorge", "Kleber", "Leonardo", "Mário", "Nelson",
            "Ricardo", "Samuel", "Tiago", "Uéliton", "Vitor",
            "Wagner", "Xerxes", "Yuri", "Zico", "Adriano", "Cícero", "Cicinho",
            "Guilherme", "Lucas", "Luiz", "Pedro", "Fernando", "Cainã",
            "Hezequias"]

Lista_Segundo_nome = ["Souza", "Oliveira", "Silva", "Costa", "Almeida",
            "Pereira", "Rocha", "Santos", "Lima", "Martins",
            "Ferreira", "Rodrigues", "Dias", "Gomes", "Mendes",
            "Carvalho", "Alves", "Barbosa", "Pinto", "Torres",
            "Ribeiro", "Araújo", "Pires", "Nascimento", "Lopes",
            "Andrade", "Freitas", "Vieira", "Cardoso", "Campos",
            "Moraes", "Machado", "Ramos", "Monteiro", "Borges",
            "Castro", "Teixeira", "Matos", "Figueiredo", "Pacheco",
            "Martins", "Gonçalves", "Tavares", "Farias", "Lima",
            "Azevedo", "Ribeiro", "Melo", "Viana", "Sá",
            "Dantas", "Magalhães", "Telles", "Alvarenga", "Figueira",
            "Lima", "Macêdo", "Siqueira", "Carneiro", "Barata",
            "Xavier", "Pimentel", "Goulart", "Cavalcanti", "Barros",
            "Lins", "Saldanha", "Queiroz", "Zanetti", "Macedo",
            "Vilar", "César", "Monteiro", "Mendonça", "Campos",
            "Alencar", "Vieira", "Silveira", "Ferreira", "Ribeiro",
            "Pimentel", "Batalha", "Mota", "Costa", "Marques",
            "Cunha", "Siqueira", "Gomes", "Nunes", "Batista",
            "Lobo", "Araujo", "Severiano", "Peixoto", "Borges",
            "Tavares", "Mendes", "Machado", "Morais", "Castro",
            "Fontes", "Martins", "Barros", "Reis", "Lima",
            "Silva", "Vargas", "Ribeiro", "Lima", "Pereira", "Braga",
            "Diniz", "Braule", "Frota", "Lameu", "Barroso", "Dutra"]

Lista_dano = ["Sim", "Não"]

Lista_Funcao = ["Supervisor", "Fiscal", "Ag. Comercial"]

Lista_dias_afastados = [0,5,15]

def gerar_data_aleatoria():
    hoje = date.today()
    primeiro_dia = hoje.replace(day=1)
    delta = (hoje - primeiro_dia).days + 1
    dias_aleatorios = rd.randint(0, delta - 1)
    return primeiro_dia + timedelta(days=dias_aleatorios

def Funcionario():
    primeiro_nome = rd.choice(Lista_Primeiro_nome)
    segundo_nome = rd.choice(Lista_Segundo_nome)
    return f"{primeiro_nome } {segundo_nome} "

def Funcao():
    return rd.choice(Lista_Funcao)

def Dias_afastados():
    return rd.choice(Lista_dias_afastados)

def Teve_danos(dias):
    if dias == 0:
        return rd.choice(Lista_dano)
    else:
        return "sim"
    
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

def Gerador_funcionarios():
    nome = Funcionario()
    cargo = Funcao()
    dias = Dias_afastados()
    danos = Teve_danos(dias)
    ac_in_qa = Acidente(danos, dias)
    data_ocorrencia = gerar_data_aleatoria()

    return{
        "Nome: ": nome,
        "Função: ": cargo,
        "Dias afastados: ": dias,
        "teve danos: ": danos,
        "tipo de acidente: ": ac_in_qa,
        "Data ocorrência: ": data_ocorrencia
    }

if __name__ == "__main__":
    funcionarios = [Gerador_funcionarios() for _ in range(52)]
    
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
