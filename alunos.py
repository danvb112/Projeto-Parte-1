import helpers
# ALUNOS
alunos = []


def adicionar_aluno(nome, cpf):
    global alunos
    for indice,elemento in enumerate(alunos):
            if elemento[1] == cpf:
                    return False
    alunos.append([nome, cpf])
    return True
    
def apagar_aluno(cpf):
    global alunos
    for p , e in enumerate(alunos):
        if e[1] == cpf:
            del alunos[p]
            
            return True



def atualizar_aluno(cpf):
    global alunos
    for p , e in enumerate(alunos):
        if e[1] == cpf:
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo cpf: ")
            alunos[p][0] = novo_nome
            alunos[p][1] = novo_cpf
            return True
 
    
def ver_todos_alunos():
    global alunos
    print("\n--- Lista de todos os Alunos registrados ---")
    print("=" * 50)
    for p,e in enumerate(alunos):
            print("%d. Aluno(a): %s        CPF: %s"%((p+1), e[0], e[1]))


def grava_alunos():
    global alunos
    arquivo = open("alulos.txt", "w")
    for indice, elemento in enumerate(alunos):
        arquivo.write("Aluno(a): %s CPF: %s \n"%(elemento[0],elemento[1]))
    arquivo.close()
