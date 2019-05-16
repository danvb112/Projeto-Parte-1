import alunos
import professores
import disciplinas
import arquivos
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

def checar_existencia_turma(cod_turma):
    for turma in turmas:
        if cod_turma == turma["cod_turma"]:
            return True
        else:
            return False


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
    return True



def apagar(cod_turma):
    for i, turma in enumerate(turmas):
        if cod_turma == turma["cod_turma"]:
            del turmas[i]
            return True
        else:
            return False

    

def adicionar_alunos(codigo_da_turma, alunos_novos):
    for turma in turmas:
        if codigo_da_turma == turma['cod_turma']:
            for aluno in alunos_novos:
                if aluno not in turma['alunos']:
                    turma['alunos'].append(aluno)


def retirar_aluno(cod_turma,cpf_aluno):
    for turma in turmas:
        if cod_turma == turma["cod_turma"]:
            for i, aluno in enumerate(turma["alunos"]):
                if aluno["cpf"] == cpf_aluno:
                    del turma["alunos"][i]
                    return True
    return False

                   
def atualizar_informacoes(codigo_da_turma, nome_turma_novo, periodo_novo):
    for turma in turmas:
        if codigo_da_turma == turma['cod_turma']:
            turma["nome_turma"] = nome_turma_novo
            turma["periodo"] = periodo_novo
            return True
    return False

def atualizar_disciplina(cod_disciplina_atualizado, nome_atualizado_disciplina):
    for turma in turmas:
        turma["disciplina"]["codigo"] = cod_disciplina_atualizado 
        turma["disciplina"]["nome"] = nome_atualizado_disciplina
        return True  

def atualizar_professor(cpf_atualizado_prof, nome_atualizado_prof, departamento_atualizado):
    for turma in turmas:
        turma["professor"]["nome"] = nome_atualizado_prof
        turma["professor"]["cpf"] = cpf_atualizado_prof
        turma["professor"]["departamento"] = departamento_atualizado
        return True

def apagar_aluno(cod_turma, cpf):
    for turma in turmas:
        if cod_turma == turma['cod_turma']:
            for i, aluno in enumerate(turma['alunos']):
                if aluno['cpf'] == cpf:
                    del turma['alunos'][i]

def listar():
    print("--- Lista de todas as turmas registradas ---")
    print("=" *60)
    for turma in turmas:
        print("Codigo: {} Periodo: {} Turma: {}".format(turma["cod_turma"], turma["periodo"], turma["nome_turma"]))


def listar_by_professor(cpf):
    for turma in turmas:
        if turma['professor']['cpf'] == cpf:
            print("""
==================================
Professor: {}
==================================
Codigo da turma: {}
Periodo: {}
Disciplina: {}
==================================

""".format(turma['professor']['nome'], turma['cod_turma'], turma['periodo'], turma['disciplina']['nome']))


def listar_by_aluno(cpf):
    for turma in turmas:
        for aluno in turma['alunos']:
            if aluno['cpf'] == cpf:
                print("""
===========================
Aluno(a): {}
Disciplina: {}            
""".format(aluno['nome'], turma['disciplina']['nome']))


def listar_aluno_by_turma(cod_turma):
    for turma in turmas:
        if turma['cod_turma'] == cod_turma:
            print("""
Todos os aluno na turma
=======================
""")
            for aluno in turma['alunos']:
                print("""
Aluno(a): {} CPF: {}
""".format(aluno["nome"], aluno["cpf"]))


if __name__ == "__main__":
    arquivos.carregar_dados()
    
    alunos_add = [
        {'nome': 'Aluno1', 'cpf': '123'},
        {'nome': 'Aluno2', 'cpf': '1234'},
        {'nome': 'Aluno3', 'cpf': '45'},
        {'nome': 'Aluno4', 'cpf': '2'},
    ]

    adicionar('123', 'CC', '1', disciplinas.disciplinas[0], professores.professores[0], alunos.alunos)
    adicionar('45', 'CC', '1', disciplinas.disciplinas[1], professores.professores[1], alunos.alunos)
    adicionar_alunos('123', alunos_add)

    listar()

    # listar_by_professor('123456')
    # listar_by_aluno('07636338440')
   


    
