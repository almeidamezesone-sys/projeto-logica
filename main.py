funcionarios = {
    'vini': {
        'cargo': "gerente",
        'dias':3
    },
}
on = True

def cadastroFuncionarios():
    nome = input("\nNome: ")
    cargo = input("Cargo: ")
    funcionarios.update({nome:{'cargo':cargo, 'dias':0}})


def cadastroOcorencias():
    name = input("\nNome: ")
    days = input("Dias afastados:")
    if name in funcionarios:
        funcionarios[name].update({'dias':days})
    else: print("Funcionário não cadastrado")

def relatorios():
    total = 0
    acidentes = 0
    for i in funcionarios:
        dias = funcionarios[i]['dias']
        total += int(dias)
        if dias != 0:
            acidentes += 1
        print(f"o funcionario {i}, {funcionarios[i]['cargo']}, se afastou por {dias} dias")
    print(f"\nO total de acidentes foi de {acidentes} e o total de dias afastado foi: {total}")

while on:
    option = input("1 - Cadastrar funcionários\n2 - Cadastrar ocorrencias\n3 - Criar relatórios \n")
    match option:
        case "1":
            cadastroFuncionarios()
        case "2":
            cadastroOcorencias()
        case "3":
            relatorios()
        case _:
            print("teste")
