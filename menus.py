import alunos, professores, disciplinas, turmas, relatorios, helpers
# --- MENU---

def home_menu():
    print("""

        --- MENU ---
        ==============================================
        --- Qual operação você deseja fazer? ---
        ==============================================

        1 - Alunos
        2 - Professores
        3 - Disciplinas
        4 - Turmas
        5 - Relatórios

        0 - Sair

        ==============================================    
  
    """)
    while True:
        opcao_menu = int(input("Digite a opção: "))

        if opcao_menu == 1:
            alunos_menu()
        if opcao_menu == 2:
            professores_menu()
        if opcao_menu == 3:
            disciplina_menu()
        if opcao_menu == 4:
            turma_menu()
        if opcao_menu == 0:
            exit()




def alunos_menu():
    print("""

        --- SISTEMA ACADEMICO / ALUNOS ---    
        ===============================================
        --- Escolha uma opção ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        
        0 - Sair

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            alunos.ver_todos_alunos()
            alunos_menu()
        if opcao == 2:
            nome = helpers.pede_nome()
            cpf = helpers.pede_cpf()
            if alunos.adicionar_aluno(nome, cpf) == True:
                print("--- Aluno cadastrado com sucesso! ---")
                alunos_menu()
            else:
                print("--- Aluno já adicionado ---")
                alunos_menu()
        if opcao == 3:
            cpf = helpers.pede_cpf()
            alunos.apagar_aluno(cpf)
            alunos_menu()
        if opcao == 4:
            cpf = helpers.pede_cpf()
            alunos.atualizar_aluno(cpf)
            alunos_menu()
        if opcao == 0:
            home_menu()
         


def professores_menu():
    print("""

        --- SISTEMA ACADEMICO / PROFESSORES ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        
        0 - Sair

        ==============================================
                
    """)
    while True:
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            nome = helpers.pede_nome()
            cpf = helpers.pede_cpf()
            departamento = helpers.pede_departamento()
            professores.mostrar_lista_professores()
        if opcao == 2:
            professores.adicionar_professor()
        if opcao == 3:
            professores.apagar_professor()
        if opcao == 4:
            professores.atualizar_professor()
        if opcao == 0:
            home_menu()


def disciplina_menu():
    print("""

        --- SISTEMA ACADEMICO / DISCIPLINA ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        
        0 - Sair

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            disciplinas.mostrar_disciplinas()
        if opcao == 2:
            disciplinas.nova_discilina()
        if opcao == 3:
            disciplinas.apagar_disciplina()
        if opcao == 4:
            disciplinas.atualzar_disciplina()
        if opcao == 0:
            home_menu()

def turma_menu():
    print("""

        --- SISTEMA ACADEMICO / TURMA ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Listar 
        2 - Adicionar
        3 - Deletar
        4 - Atualizar
        
        0 - Sair

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            turma.mostrar_turma()
        if opcao == 2:
            turma.nova_turma()
        if opcao == 3:
            turma.deletar_turma()
        if opcao == 4:
            turma.atualizar_turma()
        if opcao == 0:
            home_menu()

def relatorio_menu():
    print("""

        --- SISTEMA ACADEMICO / RELATÓRIO ---    
        ===============================================
        --- Escolha uma opção  ---
        ===============================================

        1 - Ata de exercício

        2 - Lista de turmas por professor
                Todas turmas/turmas por semestre
        3 - Lista de disciplinas por aluno
                Todas turmas/turmas por semestre 
        
        0 - Sair

        ==============================================
                
    """)

    # while True:
    #     opcao = int(input("Digite a opção: "))

    #     if opcao == 1:
    #         relatorios.ata_exercicio() 
    #     if opcao == 2:
    #         relatorios.lista_turmas_professor()
    #     if opcao == 3:
    #         relatorios.lista_disciplinas_alunos()
    #     if opcao == 0:
    #         home_menu()
    



def menu_atualizar_turma():
    print("""

        --- O que você deseja atualizar? ---
        ======================================

        1 - Informações da turma
        2 - Alunos da turma
        3 - Professor da Truma
        4 - Disciplina da Turma
            
        ===================================
    
    """)
