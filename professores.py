import helpers

# Professores
# modelo = {
#     nome:
#     cpf: 
#     departamento: 
# }

professores = []


def adicionar(nome, cpf, departamento):
    professor = {}
    for professor_consulta in professores:
        if cpf == professor_consulta["cpf"]:
            return False
    professor["nome"] = nome
    professor["cpf"] = cpf
    professor["departamento"] = departamento
    print(professor)
    professores.append(professor)
    alunos.sort(key=lambda x: x['nome'])
    return True


def apagar(cpf):
    for i, professor in enumerate(professores):
        if professor["cpf"] == cpf:
            del professores[i]
            return True
    return False

def buscar_professor(cpf):
    for professor in professores:
        if professor["cpf"] == cpf:
            return True
    return False


def atualizar(cpf_atual, nome_novo, cpf_novo, departamento_novo):
    for professor in professores:
        if professor["cpf"] == cpf:
            professor["nome"] = nome_novo
            professor["cpf"] = cpf_novo
            professor["departamento"] = departamento_novo
            return True
    return False
        

def listar():
    print("\n--- Lista de todos os professores registrados ---")
    print("=" * 50)
    for professor in professores:
        print("Professor(a): {}       CPF: {} \n Departamento: {} \n ".format(professor["nome"], professor["cpf"], professor["departamento"]))


def salvar():
    with open('professores.txt', 'w') as arquivo:
        for professor in professores:
            arquivo.write("Professor(a): {}       CPF: {} \n Departamento: {} \n ".format(professor["nome"], professor["cpf"], professor["departamento"])) 


if __name__ == '__main__':
    teste1 = 'valberto 123456789 cin'.split()
    teste2 = 'daniel 987654321 ceagre'.split()
    teste3 = 'felipe 00000000 cesar'.split()
    teste4 = 'paulo 03912939 ccgs'.split()

    adicionar(teste1[0], teste1[1], teste1[2])
    adicionar(teste2[0], teste2[1], teste2[2])
    adicionar(teste3[0], teste3[1], teste3[2])
    adicionar(teste4[0], teste4[1], teste4[2])
    adicionar(teste1[0], teste1[1], teste1[2])
    
    listar()

    atualizar('00000000', 'emanoel', '14725839', 'cesar')
    
    listar()

    apagar('14725839')

    listar()

    salvar()

        
