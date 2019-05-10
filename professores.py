import helpers

# Professores
professores = {}


def adicionar(nome, cpf, departamento):
    for _, valor in professores.items():
        if cpf in valor:
            print('[ERROR] Professor já existe: {}, {}, {}'.format(nome, cpf, departamento))
            return False
    
    id_unico = cpf[:5]
    professores[id_unico] = [nome, cpf, departamento]
    return True


def apagar(cpf):
    for chave, (_, cpf_cadastrado, _) in professores.items():
        if cpf == cpf_cadastrado:
            del professores[chave]
            return True

    print('[WARNING] Professor nao existente.')
    return False
  

def atualizar(cpf_atual, nome_novo, cpf_novo, departamento_novo):
    for chave, (_, cpf_cadastrado, _) in professores.items():
        if cpf_atual == cpf_cadastrado:
            professores[chave] = [nome_novo, cpf_novo, departamento_novo]
            return True

    print('[WARNING] Professor nao existente.')
    return False
            

def listar():
    print("\n--- Lista de todos os professores registrados ---")
    print("=" * 50)
    for chave, (nome, cpf, dep) in professores.items():
        print("{}. Professor(a): {}       CPF: {} \n Departamento: {} \n ".format(chave, nome, cpf, dep))


def salvar():
    with open('professores.txt', 'w') as arquivo:
        for _, (nome, cpf, dep) in professores.items():
            arquivo.write("{},{},{} \n".format(nome, cpf, dep))    


def buscar(cpf):
    for chave, (_, cpf_cadastrado, _) in professores.items():
        if cpf == cpf_cadastrado:
            return chave
    
    return False


def retornar_professores_nome():
    nomes = []
    for _, (nome, _, _) in professores.items():
        nomes.append(nome)

    return nomes


def popular_professores_teste():
    teste1 = 'valberto 123456789 cin'.split()
    teste2 = 'daniel 987654321 ceagre'.split()
    teste3 = 'felipe 00000000 cesar'.split()
    teste4 = 'paulo 03912939 ccgs'.split()

    adicionar(teste1[0], teste1[1], teste1[2])
    adicionar(teste2[0], teste2[1], teste2[2])
    adicionar(teste3[0], teste3[1], teste3[2])
    adicionar(teste4[0], teste4[1], teste4[2])
              

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

        
