import helpers
# Disciplinas
disciplinas = []

def nova_discilina():
    global disciplinas
    codigo = helpers.pede_codigo_disciplina()
    nomeDisciplina = helpers.pede_nome()
    for p,e in enumerate(disciplinas):
        if e[1] == codigo:
            print("\n --- Disciplina já cadastrada!---")
            del disciplinas[p]
    else:
        disciplinas.append([nomeDisciplina, codigo])


def apagar_disciplina():
    global disciplinas
    codigo = helpers.pede_codigo_disciplina()
    for p,e in enumerate(disciplinas):
        if e[1] == codigo:
            del disciplinas[p]
            print("\n--- Disciplina deletada ---")


def atualzar_disciplina():
    global disciplinas
    codigo = helpers.pede_codigo_disciplina()
    for p,e in enumerate(disciplinas):
        if e[1] == codigo:
            novoCodigo = input("Digite o código atualizado da disciplina: ")
            novoNome = input("Digite o nome atualizado da disciplina: ")
            disciplinas[p][0] = novoNome
            disciplinas[p][1] = novoCodigo
            print("\n--- Disciplina Atualizada ---")


def mostrar_disciplinas():
    global disciplinas
    print("\n--- Lista com todas as disciplinas registradas ---")
    print("=" *50)
    for p,e in enumerate(disciplinas):
        print("%d. Disciplina: %s      Código: %s" %((p+1),e[0], e[1]))

