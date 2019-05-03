def adicionar_aluno():
    global alunos
    nome_aluno = pede_nome()
    cpf_aluno = pede_cpf()
    for p,e in enumerate(alunos):
        if e[1] == cpf_aluno:
            print("\n --- Aluno já cadastrado!---")
            del alunos[p]
    else:
        alunos.append([nome_aluno, cpf_aluno])


    
def apagar_aluno():
    global alunos
    cpf_aluno = pede_cpf()
    for p , e in enumerate(alunos):
        if e[1] == cpf_aluno:
            del alunos[p]
            print("\n--- Aluno deletado ---")



def atualizar_aluno():
    global alunos
    cpf_aluno = pede_cpf()
    for p , e in enumerate(alunos):
        if e[1].lower() == cpf_aluno:
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo cpf: ")
            alunos[p][0] = novo_nome
            alunos[p][1] = novo_cpf
            print("\n--- Aluno atualizado ---")   
    
def ver_todos_alunos():
    global alunos
    print("\n--- Lista de todos os Alunos registrados ---")
    print("=" * 50)
    for p,e in enumerate(alunos):
            print("%d. Aluno(a): %s        CPF: %s"%((p+1), e[0], e[1]))
