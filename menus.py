import alunos
import professores
import disciplinas
import turmas
import relatorios
import helpers

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

        if opcao_menu > 4 or opcao_menu < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue

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
        5 - Gravar informações
        
        0 - Voltar

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao > 5 or opcao < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue


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
            if alunos.apagar_aluno(cpf) -- True:
                print("\n--- Aluno deletado ---")
            else:
                print("\n --- Aluno não cadastrado ---")
            alunos_menu()
        if opcao == 4:
            cpf = helpers.pede_cpf()
            if alunos.atualizar_aluno(cpf) == True:
                print("\n--- Aluno atualizado ---")  
            else:
                print("--- Aluno não cadastrado ---")
            alunos_menu()
        
        if opcao == 5:
            alunos.grava_alunos()
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
        5 - Gravar informações
        
        0 - Voltar

        ==============================================
                
    """)
    while True:
        opcao = int(input("Digite a opção: "))
        
        if opcao > 5 or opcao < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue

        if opcao == 1:
            professores.listar()
            professores_menu()
        if opcao == 2:
            nome            = helpers.pede_nome()
            cpf             = helpers.pede_cpf()
            departamento    = helpers.pede_departamento()

            if professores.adicionar(nome,cpf, departamento):
                print("--- Professor adicionado com sucesso! ---")
                professores_menu()
            else:
                print("--- Professor já registrado ---")
                professores_menu()
        if opcao == 3:
            cpf = helpers.pede_cpf()
            if professores.apagar(cpf):
                print("\n--- Professor deletado ---")
            else:
                print("--- Professor Não registrado ---")
            professores_menu()
        if opcao == 4:
            cpf             = helpers.pede_cpf()
            if professores.buscar(cpf):
                nome            = helpers.pede_nome()
                cpf_novo        = helpers.pede_cpf()
                departamento    = helpers.pede_departamento()

                professores.atualizar(cpf, nome, cpf_novo, departamento) 
                print("--- Professor atualizado com sucesso ---")
                professores_menu()
            else:
                print("--- Professor não registrado ---")
                professores_menu()
            
        if opcao == 5:
            professores.salvar()
            professores_menu()
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
        5 - Gravar informações
        0 - Voltar

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao > 5 or opcao < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue

        if opcao == 1:
            disciplinas.mostrar_disciplinas()
            disciplina_menu()
        if opcao == 2:
            codigo = helpers.pede_codigo_disciplina()
            nome = helpers.pede_nome()
            if disciplinas.nova_discilina(nome, codigo) == False:
                print("\n --- Disciplina já cadastrada!---")
            else:
                print("--- Disciplina cadastrada com sucesso ---")
            disciplina_menu()
        if opcao == 3:
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.apagar_disciplina(codigo) == True:
                print("\n--- Disciplina deletada ---")
            else:
                print(("--- Disciplina não cadastrada ---"))
            disciplina_menu()
        if opcao == 4:
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.atualzar_disciplina(codigo) == True:
                print("\n--- Disciplina Atualizada ---")
            else:
                print("--- Disciplina não cadastrada ---")
            disciplina_menu()
        if opcao == 5:
            disciplinas.grava_disciplinas()
            disciplina_menu()
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
        
        0 - Voltar

        ==============================================
                
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao > 4 or opcao < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue

        if opcao == 1:
            turmas.mostrar_turma()
            turma_menu()
        if opcao == 2:
            print("\n--- Vamos adicionar as informações da turma ---")
            codigo_da_turma = helpers.pede_codigo_turma()
            periodo = helpers.pede_periodo()
            nome_turma = input("Digite o nome da turma: ")
            print("\n--- Agora vamos adicionar a disciplina ---")
            codigo_disciplina = helpers.pede_codigo_disciplina()
            print("\n--- Agora vamos adicionar o professor da turma ---")
            cpf_professor = helpers.pede_cpf()
            print("\n--- Agora vamos adicionar os alunos da turma ---")
            
            turmas.nova_turma(nome_turma,codigo_da_turma, periodo, codigo_disciplina, cpf_professor)
            
            while True:
                print("\n--- Digite 1 para adicionar ou 0 para finalizar ---")
                opcao = int(input())
                if opcao == 0:
                    for indice, elemento in enumerate(turmas.alunos_cpf_temp):
                        turmas.turma_alunos.append(elemento)
                    break
                elif opcao == 1:
                    cpf_aluno = helpers.pede_cpf()
                    if turmas.adicionar_aluno_nova_turma(cpf_aluno) == True:
                        print("--- Aluno adicionado ---")
                    else:
                        print("--- Aluno inexistente ---")
   
            print("\n--- Nova turma adicionada ---")
            print(turmas.informacoes_da_turma)
            print(turmas.disciplina_turma)
            print(turmas.professor_turma)
            print(turmas.turma_alunos)
            turma_menu()
        if opcao == 3:
            codigo_da_turma = helpers.pede_codigo_turma()
            if turmas.deletar_turma(codigo_da_turma) == True:
                print("--- Turma deletada ---")
            else:
                print("--- Turma não encontrada ---")
            turma_menu()
        if opcao == 4:
            turmas.mostrar_turma()
            codigo = helpers.pede_codigo_turma()
            if turmas.verificacao_turma(codigo) == True:
                menu_atualizar_turma(codigo)
            else:
                print("--- Turma inexistente ---")    
        if opcao == 0:
            home_menu()







def menu_atualizar_turma(codigo):
    print("""

        --- O que você deseja atualizar? ---
        ======================================

        1 - Informações da turma
        2 - Alunos da turma
        3 - Professor da Truma
        4 - Disciplina da Turma

        0 - Voltar 
            
        ===================================
    
    """)

    while True:
        opcao = int(input("Digite a opção: "))

        if opcao > 4 or opcao < 0:
            print("--- Opção inválido por favor digite novamente ---")
            continue

        if opcao == 0:
            turma_menu()
        
        elif opcao == 1:
            periodo = helpers.pede_periodo()
            nome_turma = input("Digite o novo nome da turma: ")
            turmas.atualizar_informacoes_turma(codigo, periodo, nome_turma)
            print("\n--- Informações da turma atualizadas ---")
            menu_atualizar_turma()
        elif opcao == 2:
            print("--- Você deseja adicoinar ou retirar um aluno da turma? (1- adicionar 2 - retirar 0 - voltar) ---")
            while True:
                opcao = int(input("Digite a opção: "))

                if opcao == 1:
                    cpf_aluno = helpers.pede_cpf()
                    for indice,elemento in enumerate(alunos.alunos):
                        if elemento[1] == cpf_aluno:
                            turmas.adicionar_aluno_turma(cpf_aluno, codigo)
                        else:
                            print("--- Aluno Não encontrado ---")
                if opcao == 2:
                    cpf_aluno = helpers.pede_cpf()
                    




            

            turmas.atualizar_alunos_turma()
        elif opcao == 3:
            turmas.atualizar_professor_turma()
        elif opcao == 4:
            turmas.atualizar_disciplina_turma()
        








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
        
        0 - Voltar

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
    