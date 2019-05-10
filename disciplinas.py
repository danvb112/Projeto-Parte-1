import helpers
# Disciplinas
disciplinas = []

def nova_discilina(nome, codigo):
    global disciplinas
    for indice, elemento in enumerate(disciplinas):
            if elemento[1] == codigo:
                    return False
    disciplinas.append([nome,codigo])
    return True
        



def apagar_disciplina(codigo):
    global disciplinas
    for indice ,elemento in enumerate(disciplinas):
        if elemento[1] == codigo:
            del disciplinas[indice]
            return True


def atualzar_disciplina(codigo):
    global disciplinas
    for indice,elemento in enumerate(disciplinas):
        if elemento[1] == codigo:
            novoCodigo = input("Digite o código atualizado da disciplina: ")
            novoNome = input("Digite o nome atualizado da disciplina: ")
            disciplinas[indice][0] = novoNome
            disciplinas[indice][1] = novoCodigo
            return True


def mostrar_disciplinas():
    global disciplinas
    print("\n--- Lista com todas as disciplinas registradas ---")
    print("=" *50)
    for indice,elemento in enumerate(disciplinas):
        print("%d. Disciplina: %s      Código: %s" %((indice + 1),elemento[0], elemento[1]))

def grava_disciplinas():
        global disciplinas
        arquivo = open("Disciplinas.txt", "w")
        for indice, elemento in enumerate(disciplinas):
                arquivo.write("Nome da disciplina: %s  codigo: %s" %(elemento[0], elemento[1]))
        arquivo.close()



