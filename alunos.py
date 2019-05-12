import helpers
import json
# ALUNOS
# aluno = {
#     nome:
#     cpf: 
# }

alunos = []


def adicionar(nome, cpf):
    aluno = {}
    for aluno_consulta in alunos:
        if aluno_consulta["cpf"] == cpf:
            return False
    aluno["cpf"] = cpf
    aluno["nome"] = nome
    alunos.append(aluno)
    
    return True
    
def apagar(cpf):
    for i, aluno in enumerate(alunos):
        if aluno["cpf"] == cpf:
            del alunos[i]
            return True
    return False


def atualizar(cpf):
    for aluno in alunos:
        if cpf == aluno["cpf"]:
            aluno["cpf"] = input("Novo CPF: ")
            aluno["nome"] = input("Novo nome: ")
            return True
    return False
 
    
def listar():
    print("\n--- Lista de todos os Alunos registrados ---")
    print("=" * 50)
    for aluno in alunos:
        print("Aluno(a): {}       CPF: {}".format(aluno["nome"], aluno["cpf"]))


def salvar():
    with open ("alunos.txt", "w") as arquivo:
        for chave, (nome,cpf) in alunos.items():
            arquivo.write("Aluno(a): {} CPF: {} \n".format(nome,cpf))





