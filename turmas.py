import helpers
import alunos
import professores
import disciplinas
import menus
# Turmas 
# modelo_turma = {
#     cod_turma:
#     periodo:
#     nome_turma:
#     disciplina:
#     professor:
#     alunos:[{
#         nome:
#         cpf:
#     }]
#     }
turmas = []



def checar_disciplina(codigo_disciplina):
    for disciplina in disciplinas.disciplinas:
        if codigo_disciplina == disciplina["codigo"]:
            return disciplina
    return False

def checar_professor(cpf_professor):
    for professor in professores.professores:
        if cpf_professor == professor["cpf"]:
            return professor
    return False

def checar_aluno(cpf_aluno):
    for aluno in alunos.alunos:
        if cpf_aluno == aluno["cpf"]:
            return aluno
    return False

def checar_cod_turma(cod_turma):
    if len(turmas) == 0:
        return True
    for turma_consulta in turmas:
        if turma_consulta["cod_turma"] == cod_turma:
            return False







def adicionar(codigo_da_turma, nome_turma, periodo, disciplina, professor, alunos):
    turma = {}
    turma["cod_turma"] = codigo_da_turma
    turma["periodo"] = periodo
    turma["nome_turma"] = nome_turma
    turma["disciplina"] = disciplina
    turma["professor"] = professor
    turma["alunos"] = alunos
    turmas.append(turma)
    print(turmas)
    return True

def listar():
    print("--- Lista de todas as turmas registradas ---")
    print("=" *60)
    for turma in turmas:
        print("Codigo: {} Periodo: {} Turma: {}".format(turma["cod_turma"], turma["periodo"], turma["nome_turma"]))



def nova_turma(nome_turma,codigo_da_turma, periodo, codigo_disciplina, cpf_professor):
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos

    informacoes_da_turma.append([codigo_da_turma, periodo, nome_turma ])
    
    for indice,elemento in enumerate(disciplinas.disciplinas):
        if elemento[1] != codigo_disciplina:
            return False
        else:
            disciplina_turma.append(elemento)
            return True
        
    for indice,elemento in enumerate(professores.professor):
        if elemento[1] != cpf_professor:
            return False
        else:
            professor_turma.append(elemento)
            return True
    return True



def deletar_turma(codigo_da_turma):
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    for indice,elemento in enumerate(informacoes_da_turma):
        if elemento[0] == codigo_da_turma:
            del informacoes_da_turma[indice]
            del disciplina_turma[indice]
            del professor_turma[indice]
            del turma_alunos[indice]
            return True
        else:
            return False


def verificacao_turma(codigo):
    for indice,elemento in enumerate(informacoes_da_turma):
        if elemento [0] == codigo:
            return True 
        else:
            return False


def adicionar_aluno_turma(cpf_aluno,codigo_da_turma):
    indice_turma = None
    aluno = []
    for indice, elemento in enumerate(informacoes_da_turma):
        if elemento[0] == codigo_turma:
            indice_turma = indice
            break
    for indice, elemento in enumerate(alunos.alunos):
        if elemento[1] == cpf_aluno:
            aluno[0] = elemento[0]
            aluno[1] = cpf_aluno
            break
    turma_alunos[indice_turma].append(aluno)

#def deletar_aluno_turma():
def atualizar_informacoes_turma(codigo, periodo, nome_turma):
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos
    for indice,elemento in enumerate(informacoes_da_turma):
        if elemento [0] == codigo:
            informacoes_da_turma[indice][0] = codigo
            informacoes_da_turma[indice][1] = periodo
            informacoes_da_turma[indice][2] = nome_turma
            return True 
        else:
            return False


def atualizar_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    global turma_alunos

    for indice,elemento in enumerate(informacoes_da_turma):
        if elemento[0] == codigo_turma:
            menus.menu_atualizar_turma()
            

            opçao = int(input("Digite a opção: "))

            #if opçao == 1:
                
            
            if opçao == 2:
                cpf_aluno = helpers.pede_cpf()
                for indice,elemento in enumerate(alunos_cpf):
                    if elemento[1] == cpf_aluno:
                        novo_nome = input("Digite o nome atualizado do aluno: ")
                        novo_cpf = helpers.pede_cpf()
                        alunos_cpf[indice][elemento][0] = novo_nome
                        alunos_cpf[indice][elemento][1] = novo_cpf
                turma_alunos[p] = alunos_cpf
                print("\n--- Aluno Atualizado ---")
            
            if opçao == 3:
                cpf_professor = helpers.pede_cpf()
                for indice,elemento in enumerate(professor_turma):
                    if elemento[1] == cpf_professor:
                        novo_professor = helpers.pede_nome()
                        novo_cpf = helpers.pede_cpf()
                        professor_turma[indice][0] = novo_professor
                        professor_turma[indice][1] = novo_cpf
                        print("\n--- Professor Atualizado ---")
            
            if opçao == 4:
                codigo_disciplina = helpers.pede_codigo_disciplina()
                for p,e in enumerate(disciplina_turma):
                    if e[1] == codigo_disciplina:
                        novo_nome_disciplina = helpers.pede_nome()
                        novo_codigo_disciplina = helpers.pede_codigo_disciplina()
                        disciplina_turma[e][0] = novo_nome_disciplina
                        disciplina_turma[e][1] = novo_codigo_disciplina
                        print("\n--- Disciplina Atualizada ---")
        return True


def mostrar_turma():
    global informacoes_da_turma
    global disciplina_turma
    global professor_turma
    if len(informacoes_da_turma) == 0:
        print("--- Não há turmas registradas ---")
        return 
    print("\n--- Lista com todas as turmas registradas ---")
    print("=" *50)
    for turma in informacoes_da_turma:
        print("\n Codigo: %s Nome: %s periodo: %s" %(turma[0],turma[2], turma[1]))
        


if __name__ == "__main__":
    adicionar('123', '1', '000')
    professores.popular_professores_teste()
    
    adicionar_professor('123', '12345')
    
    # alunos_turma = ['0123', '102300', '1020129']
    # for cpf in alunos_turma:
    #     adicionar_aluno('123', alunos.buscar_nome(cpf))


    
