alunos = []
professor = []
lista_disciplinas = []

#Listas das Turmas

informacoes_da_turma = []
disciplina_turma = []
professor_turma = []
turma_alunos = []
alunos_turma_p = []



# ---FUNÇÕES INPUT---


def pede_nome():
    return (input("Digite o nome: "))
def pede_cpf():
    return (input("Digite o cpf: "))
def pede_departamento():
    return (input("Digite o nome do departamento: "))
def pede_codigo_disciplina():
    return(input("Digite o código da disciplina: "))
def pede_codigo_turma():
    return(input("Digite o código da turma: "))
def pede_periodo():
    return(input("Digite o periodo: "))

# --- MENU---

def menu1():
    print("""

--- MENU ---
==============================================
--- Qual operação você deseja fazer? ---
==============================================

1 - Adicionar
2 - Deletar
3 - Atualizar
4 - Mostrar

==============================================    
  
    """)



def menu2():
    print("""

--- MENU ---    
===============================================
--- Onde você deseja operar? ---
===============================================

1 - Alunos
2 - Professores
3 - Disciplinas
4 - Turmas

==============================================
         
    """)


def menu_atualizar_turma():
    print("""

--- O que você deseja atualizar?
===================================

1 - Informações da turma
2 - Alunos da turma
3 - Professor da Truma
4 - Disciplina da Turma
    
===================================
    
    """)


# ALUNOS

def adicionar_aluno():
    global alunos
    nome_aluno = pede_nome()
    cpf_aluno = pede_cpf()
    for p,e in enumerate(alunos):
        if e[1] == cpf_aluno:
            print("\n --- Aluno já cadastrado!---")
            del alunos[p]
    else:
        alunos.append([nome_aluno, cpf_aluno])


    
def apagar_aluno():
    global alunos
    cpf_aluno = pede_cpf()
    for p , e in enumerate(alunos):
        if e[1] == cpf_aluno:
            del alunos[p]
            print("\n--- Aluno deletado ---")



def atualizar_aluno():
    global alunos
    cpf_aluno = pede_cpf()
    for p , e in enumerate(alunos):
        if e[1].lower() == cpf_aluno:
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo cpf: ")
            alunos[p][0] = novo_nome
            alunos[p][1] = novo_cpf
            print("\n--- Aluno atualizado ---")   
    
def ver_todos_alunos():
    global alunos
    print("\n--- Lista de todos os Alunos registrados ---")
    print("=" * 50)
    for p,e in enumerate(alunos):
            print("%d. Aluno(a): %s        CPF: %s"%((p+1), e[0], e[1]))


# Professores

def adicionar_professor():
    global professor
    nome_professor = pede_nome()
    cpf_professor = pede_cpf()
    departamento = pede_departamento()
    for p,e in enumerate(professor):
        if e[1] == cpf_professor:
            print("\n --- Professor já cadastrado!---")
            del professor[p]
    else:
        professor.append([nome_professor, cpf_professor, departamento])


def apagar_professor():
    global professor
    cpf_professor = pede_cpf()
    for p,e in enumerate(professor):
        if e[1] == cpf_professor:
            del professor[p]
            print("\n--- Professor deletado ---")

def atualizar_professor():
    global professor
    print("\n--- Qual professor você deseja atualizar? ---")
    cpf_professor = pede_cpf()
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


# Disciplinas

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


# Turmas 

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







while True:
    menu1()

    opcao_menu = int(input("Digite a opção: "))

    if opcao_menu == (""):
        continue
    
    if opcao_menu == 1:
        menu2()
        opcao2 = int(input("Digite a opçao: "))

        if opcao2 == "":
            continue
        if opcao2 == 1:
            adicionar_aluno()
        if opcao2 == 2:
            adicionar_professor()
        if opcao2 == 3:
            nova_discilina()
        if opcao2 == 4:
            nova_turma()
    
    if opcao_menu == 2:
        menu2()
        opcao2 = int(input("Digite a opção: "))
        if opcao2 == "":
            continue
        if opcao2 == 1:
            apagar_aluno()
        if opcao2 == 2:
            apagar_professor()
        if opcao2 == 3:
            apagar_disciplina()
        if opcao2 == 4:
            deletar_turma()
    
    
    if opcao_menu == 3:
        menu2()
        opcao2 = int(input("Digite a opção: "))
        if opcao2 == "":
            continue

        if opcao2 == 1:
            atualizar_aluno()
        if opcao2 == 2:
            atualizar_professor()
        if opcao2 == 3:
            atualzar_disciplina()
        if opcao2 == 4:
            atualizar_turma()
    
    
    if opcao_menu == 4:
        menu2()
        opcao2 = int(input("Digite a opção: "))
        if opcao2 == "":
            continue

        if opcao2 == 1:
            ver_todos_alunos()
        if opcao2 == 2:
            mostrar_lista_professores()
        if opcao2 == 3:
            mostrar_lista_disciplinas()
        if opcao2 == 4:
            print(informacoes_da_turma)
            print(disciplina_turma)
            print(professor_turma)
            print(turma_alunos)





                    

            


                


            




    


   
    
    


            
    
    

    





    





        









   
