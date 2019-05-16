import helpers
# Disciplinas
# modelo_disciplinas = {
#         Nome:
#         Codigo:
# }
disciplinas = []

def adicionar(nome, codigo):
    disciplina = {}
    for disciplina_consulta in disciplinas:
            if disciplina_consulta["codigo"] == codigo:
                    return False
    disciplina["nome"] = nome
    disciplina["codigo"] = codigo
    disciplinas.append(disciplina)
    disciplinas.sort(key=lambda x: x['nome'])
    return True


def apagar(codigo):
        for i, disciplina_consulta in enumerate(disciplinas):
            if disciplina_consulta["codigo"] == codigo:
                    del disciplinas[i]
                    return True
        return False


def atualizar(codigo):
    for disciplina in disciplinas:
        if codigo == disciplina["codigo"]:
            disciplina["nome"] = input("Digite o nome atualizado: ")
            disciplina["codigo"] = input("Digite o codigo atualizado: ")
            return True
    return False
                     

def listar():
    print("\n--- Lista com todas as disciplinas registradas ---")
    print("=" *50)
    for disciplina in disciplinas:
        print("Disciplina: {}      Código: {}".format(disciplina["nome"], disciplina["codigo"]))


def salvar():
    with open ("disciplinas.txt", "w") as arquivo:
        for disciplina in disciplinas:
            arquivo.write("Disciplina: {}      Código: {}\n".format(disciplina["nome"], disciplina["codigo"]))
        


if __name__ == "__main__":
    adicionar('Introdução a Computação', '123')
    adicionar('Cálculo 1', '456')
    adicionar('Estrutura de Dados', '789')

    listar()

    atualizar('123', 'Introdução a Computação com Python', '123')
    atualizar('456', 'Matemática Discreta', '123')
    atualizar('1', 'Matemática Discreta', '123')

    listar()

    salvar()

