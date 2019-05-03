def nova_discilina():
    global lista_disciplinas
    codigo = pede_codigo_disciplina()
    nomeDisciplina = pede_nome()
    for p,e in enumerate(lista_disciplinas):
        if e[1] == codigo:
            print("\n --- Disciplina já cadastrada!---")
            del lista_disciplinas[p]
    else:
        lista_disciplinas.append([nomeDisciplina, codigo])


def apagar_disciplina():
    global lista_disciplinas
    codigo = pede_codigo_disciplina()
    for p,e in enumerate(lista_disciplinas):
        if e[1] == codigo:
            del lista_disciplinas[p]
            print("\n--- Disciplina deletada ---")


def atualzar_disciplina():
    global lista_disciplinas
    codigo = pede_codigo_disciplina()
    for p,e in enumerate(lista_disciplinas):
        if e[1] == codigo:
            novoCodigo = input("Digite o código atualizado da disciplina: ")
            novoNome = input("Digite o nome atualizado da disciplina: ")
            lista_disciplinas[p][0] = novoNome
            lista_disciplinas[p][1] = novoCodigo
            print("\n--- Disciplina Atualizada ---")


def mostrar_lista_disciplinas():
    global lista_disciplinas
    print("\n--- Lista com todas as disciplinas registradas ---")
    print("=" *50)
    for p,e in enumerate(lista_disciplinas):
        print("%d. Disciplina: %s      Código: %s" %((p+1),e[0], e[1]))
