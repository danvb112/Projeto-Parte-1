import helpers
# Professores
professor = []

def adicionar_professor(nome, cpf, departamento):        
        global professor
        for indice,elemento in enumerate(professor):
                if elemento[1] == cpf:
                        return False            
        professor.append([nome, cpf, departamento])
        return True

    


def apagar_professor(cpf):
    global professor
    for indice,elemento in enumerate(professor):
        if elemento[1] == cpf:
            del professor[indice]
            return True

def atualizar_professor(cpf):
    global professor
    for indice,elemento in enumerate(professor):
        if elemento[1] == cpf:
            novo_nome = input("Digite o nome atualizado do professor: ")
            novo_cpf = input("Digite o cpf atualizado do professor: ")
            novo_departamento = input("Digite o departamento atualizado do professor: ")
            professor[indice][0] = novo_nome
            professor[indice][1] = novo_cpf
            professor[indice][2] = novo_departamento
            return True
        else:
            return False



def mostrar_lista_professores():
    global professor
    print("\n--- Lista de todos os professores registrados ---")
    print("=" * 50)
    for p,e in enumerate(professor):
        print("%d. Professor(a): %s       CPF: %s \n Departamento: %s \n " %((p+1),e[0],e[1],e[2]))

def grava_professores():
        global professor
        arquivo = open("professores.txt", "w")
        for indice, elemento in enumerate(professor):
                arquivo.write("Professor: %s   CPF: %s \n Departamento: %s \n" %(elemento[0], elemento[1], elemento[2]))
        arquivo.close()

