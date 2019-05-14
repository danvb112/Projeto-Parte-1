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

    alunos.sort(key=lambda x: x['nome'])
    
    return True
    
def apagar(cpf):
    for i, aluno in enumerate(alunos):
        if aluno["cpf"] == cpf:
            del alunos[i]
            return True
    return False


def atualizar(cpf_atual, nome_novo, cpf_novo):
    for aluno in alunos:
        if cpf_atual == aluno["cpf"]:
            aluno["nome"] = nome_novo
            aluno["cpf"] = cpf_novo
            return True
    return False
 
    
def listar():
    print("\n--- Lista de todos os Alunos registrados ---")
    print("=" * 50)
    for aluno in alunos:
        print("Aluno(a): {}       CPF: {}".format(aluno["nome"], aluno["cpf"]))


def salvar():
    with open ("alunos.txt", "w") as arquivo:
        for aluno in alunos:
            arquivo.write("Aluno(a): {}       CPF: {}\n".format(aluno["nome"], aluno["cpf"]))



if __name__ == "__main__":
    adicionar('Sandino Fofuxo', '07636338440')
    adicionar('Daniel Targoryen', '065498714687')

    listar()

    atualizar('07636338440', 'Sandino Barbixa', '07636338440')

    listar()

    salvar()
    
