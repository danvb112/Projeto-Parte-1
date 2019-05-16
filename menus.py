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
        opcao_menu = input("Digite a opção: ")
        
        if opcao_menu == "1":
            alunos_menu()
        if opcao_menu == "2":
            professores_menu()
        if opcao_menu == "3":
            disciplina_menu()
        if opcao_menu == "4":
            turma_menu()
        if opcao_menu == "5":
            relatorio_menu()
        if opcao_menu == "0":
            exit()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            home_menu()
            continue





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
        opcao = input("Digite a opção: ")
        
        if opcao == "1":
            alunos.listar()
            alunos_menu()
        if opcao == "2":
            nome = helpers.pede_nome()
            cpf = helpers.pede_cpf()
            if alunos.adicionar(nome, cpf) == True:
                print("\n--- Aluno cadastrado com sucesso! ---\n")
                alunos_menu()
            else:
                print("\n--- Aluno já adicionado ---")
                alunos_menu()
        if opcao == "3":
            cpf = helpers.pede_cpf()
            if alunos.apagar(cpf) == True:
                print("\n--- Aluno deletado ---\n")
            else:
                print("\n --- Aluno não cadastrado ---\n")
            alunos_menu()
        if opcao == "4":
            cpf = helpers.pede_cpf()
            if alunos.atualizar(cpf) == True:
                print("\n--- Aluno atualizado ---\n")  
            else:
                print("\n--- Aluno não cadastrado ---\n")
            alunos_menu()
        
        if opcao == "5":
            alunos.salvar()
            alunos_menu()
        if opcao == "0":
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            alunos_menu()
            continue
         


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
        opcao = input("Digite a opção: ")

        if opcao == "1":
            professores.listar()
            professores_menu()
        if opcao == "2":
            nome            = helpers.pede_nome()
            cpf             = helpers.pede_cpf()
            departamento    = helpers.pede_departamento()

            if professores.adicionar(nome,cpf, departamento):
                print("\n--- Professor adicionado com sucesso! ---\n")
                professores_menu()
            else:
                print('\n--- Professor já existe ---\n')
                professores_menu()
        if opcao == "3":
            cpf = helpers.pede_cpf()
            if professores.apagar(cpf):
                print("\n--- Professor deletado ---\n")
                professores_menu()
            else:
                print('\n--- Professor nao existente. ---\n')
                professores_menu()
        if opcao == "4":
            cpf             = helpers.pede_cpf()
            if professores.atualizar(cpf):
                print("\n--- Professor atualizado com sucesso ---")
                professores_menu()
            else:
                print("\n--- Professor não registrado ---")
                professores_menu()
                
        if opcao == "5":
            professores.salvar()
            professores_menu()
        if opcao == "0":
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            professores_menu()
            continue


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
        opcao = input("Digite a opção: ")

            
        if opcao == '1':
            disciplinas.listar()
            disciplina_menu()
        if opcao == '2':
            codigo = helpers.pede_codigo_disciplina()
            nome = helpers.pede_nome()
            if disciplinas.adicionar(nome, codigo):
                print("\n--- Disciplina cadastrada com sucesso ---\n")
                disciplina_menu()
            else:
                print("\n --- Disciplina já cadastrada! ---\n")
                disciplina_menu()
        if opcao == '3':
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.apagar(codigo):
                print("\n--- Disciplina deletada ---\n")
                disciplina_menu()
            else:
                print(("\n--- Disciplina não cadastrada ---\n"))
                disciplina_menu()
        if opcao == '4':
            codigo = helpers.pede_codigo_disciplina()
            if disciplinas.atualizar(codigo):
                print("\n--- Disciplina Atualizada ---\n")
                disciplina_menu()
            else:
                print("\n--- Disciplina não cadastrada ---\n")
                disciplina_menu()
        if opcao == '5':
            disciplinas.salvar()
            disciplina_menu()
        if opcao == '0':
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            disciplina_menu()
            continue
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
        opcao = input("Digite a opção: ")

        if opcao == '1':
            turmas.listar()
            turma_menu()
        if opcao == '2':
            print("\n--- Vamos adicionar as informações da turma ---\n")
            cod_turma = helpers.pede_codigo_turma()
            periodo = helpers.pede_periodo()
            nome_turma = input("Digite o nome da turma: ") 
            turmas.checar_cod_turma(cod_turma)
            print("\n--- Agora vamos adicionar a disciplina ---\n")
            print("\n--- Qual disciplina você deseja adicionar? --- \n")
            disciplinas.listar()
            cod_disciplina = helpers.pede_codigo_disciplina()    
            disciplina = turmas.checar_disciplina(cod_disciplina)
            if disciplina:
                print("\n--- Agora vamos adicionar o professor da turma ---\n")
                print("\n--- Qual professor você deseja adicionar? --- \n")
                professores.listar()
                cpf_professor = helpers.pede_cpf()
                professor = turmas.checar_professor(cpf_professor)
                if professor:
                    print("\n--- Agora vamos adicionar os alunos da turma ---\n")
                    lista_alunos = []
                    while True:
                        print("\n--- Digite 1 para adicionar ou 0 para finalizar ---")
                        opcao = input()
                       
                        if opcao == '0':
                            turmas.adicionar(cod_turma, nome_turma, periodo, disciplina, professor, lista_alunos)
                            print("\n--- Nova turma adicionada ---")
                            turma_menu()
                            break
                        if opcao == '1':
                            print("\n--- Qual aluno você deseja adicionar? --- \n")
                            alunos.listar()
                            cpf_aluno = helpers.pede_cpf()
                            novo_aluno = turmas.checar_aluno(cpf_aluno)
                            if novo_aluno:
                                lista_alunos.append(novo_aluno)
                                print("\n--- Aluno inserido na turma ---\n")
                                continue
                            else:
                                print("\n--- Aluno não cadastrado ---\n")
                                continue
                        else:
                            print("\n--- Opção inválida, por favor digite novamente ---")
                            continue 
                else:
                    print("\n--- Professor não encontrado ---\n")
                    turma_menu()
            else:
                print("\n --- Disciplina não encontrada ---\n")
                turma_menu()
                
        if opcao == '3':
            print("\n--- Qual turma você deseja apagar? ---\n")
            turmas.listar()
            cod_turma = helpers.pede_codigo_turma()
            if turmas.apagar(cod_turma):
                print("\n--- Turma deletada ---\n")
            else:
                print("\n--- Turma não encontrada ---\n")
            turma_menu()
        if opcao == '4':
            print("\n--- Qual turma você deseja atualizar? ---\n")
            turmas.listar()
            cod_turma = helpers.pede_codigo_turma()
            if turmas.checar_existencia_turma(cod_turma):
                menu_atualizar_turma(cod_turma)
            else:
                print("\n--- Turma inexistente ---\n") 
                turma_menu()  
        if opcao == '0':
            home_menu()
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            turma_menu()
            continue



def menu_atualizar_turma(cod_turma):
    print("""

        --- O que você deseja atualizar? ---
        ======================================

        1 - Informações da turma
        2 - Adicionar alunos na turma
        3 - Retirar alunos da turma

        0 - Voltar 
            
        ===================================
    
    """)

    while True:
        opcao = input("Digite a opção: ")
        

        if opcao == '0':
            turma_menu()
        
        if opcao == '1':
            nome_turma_novo = input("Digite o nome atualizado da turma: ")
            periodo_novo = input("Digite o periodo atualizado da turma: ")
            turmas.atualizar_informacoes(cod_turma, nome_turma_novo, periodo_novo)
            cod_disciplina_atualizado = input("Digite o codigo atualizado da disciplina: ")
            nome_atualizado_disciplina = input("Digite o nome atualizado da disciplina: ")
            turmas.atualizar_disciplina(cod_disciplina_atualizado, nome_atualizado_disciplina)
            cpf_atualizado_prof = input("Digite o cpf atualizado do professor: ")
            nome_atualizado_prof = input("Digite o nome atualizado do professor: ")
            departamento_atualizado = input("Digite o departamento do professor: ")
            turmas.atualizar_professor(cpf_atualizado_prof, nome_atualizado_prof, departamento_atualizado )
            print("\n--- Informações da turma atualizadas ---")
            menu_atualizar_turma(cod_turma)
        if opcao == '2':
            print("\n--- Agora vamos adicionar os alunos da turma ---")
            lista_alunos = []
            while True:
                print("\n--- Digite 1 para adicionar ou 0 para finalizar ---")
                opcao = input()
                       
                if opcao == '0':
                    turmas.adicionar_alunos(cod_turma, lista_alunos)
                    print("\n--- Todos os alunos adicionados com sucesso ---")
                    turma_menu()
                    break
                if opcao == '1':
                    print("\n--- Qual aluno você deseja adicionar? --- \n")
                    alunos.listar()
                    cpf_aluno = helpers.pede_cpf()
                    novo_aluno = turmas.checar_aluno(cpf_aluno)
                    if novo_aluno:
                        lista_alunos.append(novo_aluno)
                        print("\n--- Aluno inserido na turma ---\n")
                        continue
                    else:
                        print("\n--- Aluno não cadastrado ---\n")
                        continue
                else:
                    print("\n--- Opção inválida, por favor digite novamente ---\n")
                    continue

        if opcao == '3':
            while True:
                print("\n--- Digite 1 para retirar ou 0 para sair ---\n")
                opcao = input("Digite a opção: ")

                if opcao == '1':
                    print("\n--- Qual aluno você deseja retirar? --- \n")
                    turmas.listar_aluno_by_turma(cod_turma)
                    cpf_aluno = input("\nDigite o cpf do aluno a ser deletado: ")
                    if turmas.retirar_aluno(cod_turma, cpf_aluno):
                        print("\n--- Aluno retirado da turma ---\n")
                        continue
                    else:
                        print("\n--- Aluno não registrado na turma ---\n")
                        continue
                if opcao == '0':
                    menu_atualizar_turma(cod_turma)
                    break
                else:
                    print("\n--- Opção inválido por favor digite novamente ---\n")
                    continue
                
        else:
            print("\n--- Opção inválido por favor digite novamente ---\n")
            menu_atualizar_turma(cod_turma)
            continue

        
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
        opcao = input("Digite a opção: ")
        if opcao == '1':
            relatorios.renderizar_ata_exercicio(turmas.turmas)
            relatorio_menu()
        if opcao == '2':
            print("--- De qual professor voce deseja ver as turmas? ---\n")
            professores.listar()
            cpf_prof = helpers.pede_cpf()
            turmas.listar_by_professor(cpf_prof)
            relatorio_menu()
        if opcao == '3':
            print("--- De qual aluno voce deseja ver as disciplinas? ---\n")
            alunos.listar()
            cpf_aluno = helpers.pede_cpf()
            turmas.listar_by_aluno(cpf_aluno)
            relatorio_menu()
        if opcao == '0':
            home_menu()
        else:
            print("\n--- Opção inválida por favor digite novamente! ---\n")
            continue
