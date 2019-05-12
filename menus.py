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

        if opcao_menu > 5 or opcao_menu < 0:
            print("\n--- Opção inválido por favor digite novamente ---")
            continue

        if opcao_menu == 1:
            alunos_menu()
        if opcao_menu == 2:
            professores_menu()
        if opcao_menu == 3:
            disciplina_menu()
        if opcao_menu == 4:
            turma_menu()
        if opcao_menu == 5:
            relatorio_menu()
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
            print("\n--- Opção inválido por favor digite novamente ---")
            continue


        if opcao == 1:
            alunos.listar()
            alunos_menu()
        if opcao == 2:
            nome = helpers.pede_nome()
            cpf = helpers.pede_cpf()
            if alunos.adicionar(nome, cpf) == True:
                print("\n--- Aluno cadastrado com sucesso! ---")
                alunos_menu()
            else:
                print("\n--- Aluno já adicionado ---")
                alunos_menu()
        if opcao == 3:
            cpf = helpers.pede_cpf()
            if alunos.apagar(cpf) == True:
                print("\n--- Aluno deletado ---")
            else:
                print("\n --- Aluno não cadastrado ---")
            alunos_menu()
        if opcao == 4:
            cpf = helpers.pede_cpf()
            if alunos.atualizar(cpf) == True:
                print("\n--- Aluno atualizado ---")  
            else:
                print("\n--- Aluno não cadastrado ---")
            alunos_menu()
        
        if opcao == 5:
            alunos.salvar()
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
            print("\n--- Opção inválido por favor digite novamente ---")
            continue

        if opcao == 1:
            professores.listar()
            professores_menu()
        if opcao == 2:
            nome            = helpers.pede_nome()
            cpf             = helpers.pede_cpf()
            departamento    = helpers.pede_departamento()

            if professores.adicionar(nome,cpf, departamento):
                print("\n--- Professor adicionado com sucesso! ---")
                professores_menu()
            else:
                print('\n--- [ERROR] Professor já existe ---')
                professores_menu()
        if opcao == 3:
            cpf = helpers.pede_cpf()
            if professores.apagar(cpf):
                print("\n--- Professor deletado ---")
                professores_menu()
            else:
                print('[WARNING] Professor nao existente.')
                professores_menu()
        if opcao == 4:
            cpf             = helpers.pede_cpf()
            if professores.atualizar(cpf):
                print("\n--- Professor atualizado com sucesso ---")
                professores_menu()
            else:
                print("\n--- Professor não registrado ---")
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
            print("\n--- Opção inválido por favor digite novamente ---")
            continue
            
        if opcao == 1:
            disciplinas.listar()
            disciplina_menu()
        if opcao == 2:
            codigo = helpers.pede_codigo_disciplina()
            nome = helpers.pede_nome()
            if disciplinas.adicionar(nome, codigo):
                print("\n--- Disciplina cadastrada com sucesso ---")
                disciplina_menu()
            else:
                print("\n --- Disciplina já cadastrada!---")
                disciplina_menu()
        if opcao == 3:
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.apagar(codigo):
                print("\n--- Disciplina deletada ---")
                disciplina_menu()
            else:
                print(("\n--- Disciplina não cadastrada ---"))
                disciplina_menu()
        if opcao == 4:
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.atualzar(codigo):
                print("\n--- Disciplina Atualizada ---")
                disciplina_menu()
            else:
                print("\n--- Disciplina não cadastrada ---")
                disciplina_menu()
        if opcao == 5:
            disciplinas.salvar()
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
            turmas.listar()
            turma_menu()
        if opcao == 2:
            print("\n--- Vamos adicionar as informações da turma ---")
            cod_turma = helpers.pede_codigo_turma()
            periodo = helpers.pede_periodo()
            nome_turma = input("Digite o nome da turma: ") 
            turmas.checar_cod_turma(cod_turma)
            print("\n--- Agora vamos adicionar a disciplina ---")
            print("\n--- Qual disciplina você deseja adicionar? --- \n")
            disciplinas.listar()
            cod_disciplina = helpers.pede_codigo_disciplina()    
            disciplina = turmas.checar_disciplina(cod_disciplina)
            if disciplina:
                print("\n--- Agora vamos adicionar o professor da turma ---")
                print("\n--- Qual professor você deseja adicionar? --- \n")
                professores.listar()
                cpf_professor = helpers.pede_cpf()
                professor = turmas.checar_professor(cpf_professor)
                if professor:
                    print("\n--- Agora vamos adicionar os alunos da turma ---")
                    lista_alunos = []
                    while True:
                        print("\n--- Digite 1 para adicionar ou 0 para finalizar ---")
                        opcao = int(input())

                        if opcao < 0 and opcao > 1:
                            print("\n--- Opção inválida, pr favor digite novamente ---")
                            continue                        
                        elif opcao == 0:
                            turmas.adicionar(cod_turma, nome_turma, periodo, disciplina, professor, lista_alunos)
                            print("\n--- Nova turma adicionada ---")
                            turma_menu()
                            break
                        elif opcao == 1:
                            print("\n--- Qual aluno você deseja adicionar? --- \n")
                            alunos.listar()
                            cpf_aluno = helpers.pede_cpf()
                            novo_aluno = turmas.checar_aluno(cpf_aluno)
                            if novo_aluno:
                                lista_alunos.append(novo_aluno)

                                print("\n--- Aluno inserido na turma ---")
                                continue
                            else:
                                print("\n--- Aluno não cadastrado ---")
                                continue
                else:
                    print("\n--- Professor não encontrado ---")
                    turma_menu()
            else:
                print("\n --- Disciplina não encontrada ---")
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

    while True:
        opcao = int(input("Digite a opção: "))
        if opcao == 1:
            relatorios.renderizar_ata_exercicio(turmas.turmas)
            relatorio_menu()
        if opcao == 2:
            relatorios.lista_turmas_professor()
            relatorio_menu()
        if opcao == 3:
            relatorios.lista_disciplinas_alunos()
            relatorio_menu()
        if opcao == 0:
            home_menu()
    