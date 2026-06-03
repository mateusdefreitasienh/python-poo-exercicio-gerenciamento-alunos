from aluno import Aluno
from utils import *

alunos = []

def menu_principal():
    msg = "\n========== GERENCIAMENTO DE ALUNOS ==========\n"
    msg += "C para cadastrar aluno: \n"
    msg += "M para exibir média e aprovação de cada aluno: \n"
    msg += "S para sair: \n"
    msg += "\nDigite a opção desejada: "
    
    opcao = input(msg).upper()
    
    if opcao == "C":
        nome = input_nome("Digite o nome completo do aluno: ")
        n1 = input_nota("Digite a primeira nota do aluno: ")
        n2 = input_nota("Digite a segunda nota do aluno: ")
        aluno = Aluno(nome, n1, n2)
        alunos.append(aluno)
        
        print(f"\nAluno Cadastrado!")
        for aluno in alunos:
            print(aluno)
    if opcao == "M":
        if len(alunos) > 0:
            for aluno in alunos:
                print("\n", aluno)
                print("Média: ", aluno.media())
                aluno.aprovado()
        else:
            print("\nNenhum aluno cadastrado!")
            return
    if opcao == "S":
        exit()

while True:
    menu_principal()