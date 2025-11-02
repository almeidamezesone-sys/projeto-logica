#importando classes do projeto
from ocorrencias import *
from funcionarios import *
from relatorios import *

#iniciando loop principal
on = True
while on:

    #menu inicial
    print("\n-- MENU --\n")
    option = input("1 - Cadastrar funcionários\n2 - Cadastrar ocorrencias\n3 - Criar relatórios \n4 - Fechar\n\n")

    #chama de classes diferentes a depender da escolha do usuário
    match option:
        case "1":
            Funcionarios()
        case "2":
            Ocorrencias()
        case "3":
            Relatorios()
        case "4":
            break
        case _:
            print("teste")
