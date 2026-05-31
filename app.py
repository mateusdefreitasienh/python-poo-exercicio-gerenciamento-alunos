from aluno import Aluno

alunos = []

def menu_principal():
    msg = "========== GERENCIAMENTO DE ALUNOS ==========\n"
    msg += "C para cadastrar aluno: \n"
    msg += "M para exibir média e aprovação de cada aluno: \n"
    msg += "S para sair: \n"
    msg += "\nDigite a opção desejada: "
    
    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input("Digite o nome do aluno: ")
        n1 = int(input("Digite a primeira nota do aluno: "))
        n2 = int(input("Digite a segunda nota do aluno: "))
        aluno = Aluno(nome, n1, n2)
        alunos.append(aluno)
        
        print(f"\n Aluno Cadastrado!")
        for aluno in alunos:
            print(aluno)
    if opcao == "M":
        for aluno in alunos:
            print(aluno)
            print("Média: ", aluno.media())
            aluno.aprovado()
    if opcao == "S":
        exit()

while True:
    menu_principal()