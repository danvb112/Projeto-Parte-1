# Turmas 
informacoes_da_turma = []
disciplina_turma = []
professor_turma = []
turma_alunos = []
alunos_turma_p = []

def nova_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    global alunos_turma_p
    print("\n--- Vamos adicionar as informações da turma ---")
    codigo_da_turma = pede_codigo_turma()
    periodo = pede_periodo()
    nome_turma = input("Digite o nome da turma: ")
    informacoes_da_turma.append([codigo_da_turma, periodo, nome_turma ])
    print("\n--- Agora vamos adicionar a disciplina ---")
    codigo_disciplina = pede_codigo_disciplina()
    for p,e in enumerate(lista_disciplinas):
        if e[1] == codigo_disciplina:
            disciplina_turma.append([e[0],e[1]])
    print("\n--- Agora vamos adicionar o professor da turma ---")
    cpf_professor = pede_cpf()
    for p,e in enumerate(professor):
        if e[1] == cpf_professor:
            professor_turma.append([e[0],e[1]])
    print("\n--- Agora vamos adicionar os alunos da turma ---")
    while True:
        print("\n--- Digite 1 para adicionar ou 0 para sair ---")
        opcao = int(input())
        if opcao == 0:
            break
            turma_alunos.append(alunos_turma_p)
            print("\n--- Nova turma adicionada ---")
        elif opcao == 1:
            cpf_aluno = pede_cpf()
            for p,e in enumerate(alunos):
                if e[1] == cpf_aluno:
                    alunos_turma_p.append(p)



            


def deletar_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    codigo_da_turma = pede_codigo_turma()
    for p,e in enumerate(informacoes_da_turma):
        if e[0] == codigo_da_turma:
            del informacoes_da_turma[p]
            del disciplina_turma[p]
            del professor_turma[p]
            del turma_alunos[p]
        else:
            print("--- Turma não encontrada ---")

def atualizar_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    global alunos_turma_p
    codigo_turma = pede_codigo_turma()
    for p,e in enumerate(informacoes_da_turma):
        if e[0] == codigo_turma:
            menu_atualizar_turma()

            opçao = int(input("Digite a opção: "))

            if opçao == 1:
                novo_codigo_turma = pede_codigo_turma()
                novo_periodo = pede_periodo()
                novo_nome_turma = input("Digite o novo nome da turma: ")
                informacoes_da_turma[p][0] = novo_codigo_turma
                informacoes_da_turma[p][1] = novo_periodo
                informacoes_da_turma[p][2] = novo_nome_turma
                print("\n--- Informações da turma atualizadas ---")
            
            if opçao == 2:
                cpf_aluno = pede_cpf()
                for p,e in enumerate(alunos_turma_p):
                    if e[1] == cpf_aluno:
                        novo_nome = input("Digite o nome atualizado do aluno: ")
                        novo_cpf = pede_cpf()
                        alunos_turma_p[p][e][0] = novo_nome
                        alunos_turma_p[p][e][1] = novo_cpf
                turma_alunos[p] = alunos_turma_p
                print("\n--- Aluno Atualizado ---")
            
            if opçao == 3:
                cpf_professor = pede_cpf()
                for p,e in enumerate(professor_turma):
                    if e[1] == cpf_professor:
                        novo_professor = pede_nome()
                        novo_cpf = pede_cpf()
                        professor_turma[p][0] = novo_professor
                        professor_turma[p][1] = novo_cpf
                        print("\n--- Professor Atualizado ---")
            
            if opçao == 4:
                codigo_disciplina = pede_codigo_disciplina()
                for p,e in enumerate(disciplina_turma):
                    if e[1] == codigo_disciplina:
                        novo_nome_disciplina = pede_nome()
                        novo_codigo_disciplina = pede_codigo_disciplina()
                        disciplina_turma[e][0] = novo_nome_disciplina
                        disciplina_turma[e][1] = novo_codigo_disciplina
                        print("\n--- Disciplina Atualizada ---")

def mostrar_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    global alunos_turma_p
    consuta = int(input("Qual turma você deseja ver?:  "))
    for p,e in enumerate(informacoes_da_turma):
        if p == consuta:
            for p,e in enumerate(informacoes_da_turma):
                codigo_da_turma = e[0]
                periodo = e[1]
                nome_turma = e[2]
            for p,e in enumerate(disciplina_turma):
                nome_disciplina = e[0]
                codigo_disciplina = e[1]
            for p,e in enumerate(professor_turma):
                nome_professor = e[0]
                cpf_professor = e[1]
        
     

    print("""
------------------------------------------
| código da Disciplina | Período | Turma |
| %s                   | %s      | %s    |
------------------------------------------
| Nome da disciplina                     |
| %s                                     |
------------------------------------------
| Professor(es)                          |
| %s                                     |
------------------------------------------
    
    """ %(codigo_disciplina, periodo, nome_turma, nome_disciplina, nome_professor))
