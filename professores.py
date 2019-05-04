import helpers
# Professores
professor = []

def adicionar_professor(nome, cpf, departamento):        
        global professor
        for indice,elemento in enumerate(professor):
                if elemento[1] == cpf:
                return False
        professor.append([nome_professor, cpf_professor, departamento])
        return True

    


def apagar_professor():
    global professor
    cpf_professor = helpers.pede_cpf()
    for p,e in enumerate(professor):
        if e[1] == cpf_professor:
            del professor[p]
            print("\n--- Professor deletado ---")

def atualizar_professor():
    global professor
    print("\n--- Qual professor você deseja atualizar? ---")
    cpf_professor = helpers.pede_cpf()
    for p,e in enumerate(professor):
        if e[1] == cpf_professor:
            novo_nome = input("Digite o nome atualizado do professor: ")
            novo_cpf = input("Digite o cpf atualizado do professor: ")
            novo_departamento = input("Digite o departamento atualizado do professor: ")
            professor[p][0] = novo_nome
            professor[p][1] = novo_cpf
            professor[p][2] = novo_departamento
            print("\n--- Professor atualizado ---")



def mostrar_lista_professores():
    global professor
    print("\n--- Lista de todos os professores registrados ---")
    print("=" * 50)
    for p,e in enumerate(professor):
        print("%d. Professor(a): %s       CPF: %s \n Departamento: %s \n " %((p+1),e[0],e[1],e[2]))
