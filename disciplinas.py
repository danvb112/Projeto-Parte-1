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
    return True




def apagar(codigo):
        for i, disciplina_consulta in enumerate(disciplinas):
                if disciplina_consulta["codigo"] == codigo:
                        del disciplinas[i]
                        return True
        return False




def atualzar(codigo):
    for disciplina in disciplinas:
        if codigo == disciplina["codigo"]:
            disciplina["nome"] == input("Digite o novo nome: ")
            disciplina["codigo"] == input("Digite o novo código: ")
            return True
    return False
                        
                         

def listar():
        print("\n--- Lista com todas as disciplinas registradas ---")
        print("=" *50)
        for disciplina in disciplinas:
                print("Disciplina: {}      Código: {}".format(disciplina["nome"], disciplina["codigo"]))

def salvar():
        with open ("disciplinas.txt", "w") as arquivo:
                for chave, (nome, codigo) in disciplinas.items():
                        arquivo.write("Nome da disciplina: {}  codigo: {}".format(nome, codigo))
        



