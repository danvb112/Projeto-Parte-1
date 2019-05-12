import json
import alunos
import professores
import disciplinas
import turmas

def carregar_alunos():
    with open('./database/alunos.json', 'r') as f:
        alunosParsed = json.load(f)
        alunos.alunos = alunosParsed


def carregar_professores():
    with open('./database/professores.json', 'r') as f:
        professoresParsed = json.load(f)
        professores.professores = professoresParsed

def carregar_disciplinas():
    with open('./database/disciplinas.json', 'r') as f:
        disciplinasParsed = json.load(f)
        disciplinas.disciplinas = disciplinasParsed


def carregar_turmas():
    with open('./database/turmas.json', 'r') as f:
        turmasParsed = json.load(f)
        turmas.turmas = turmasParsed
    
def carregar_dados():
    carregar_alunos()
    carregar_professores()
    carregar_disciplinas()
    carregar_turmas()