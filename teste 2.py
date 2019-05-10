lista_disciplinas = []

def pede_nome():
    return (input("Digite o nome: "))
def pede_cpf():
    return (input("Digite o cpf (Somente números): "))
def pede_departamento():
    return (input("Digite o nome do departamento: "))
def pede_codigo_disciplina():
    return(input("Digite o código da disciplina: "))
def pede_codigo_turma():
    return(input("Digite o código da turma: "))
def pede_periodo():
    return(input("Digite o periodo: "))


lista1 = [["Daniel", "112"]]
lista2 = [["Lucas", "29"]]
lista3 = [["Sandino", "492"]]

for p,e in enumerate(lista1):
    nome1 = e[0]
    numero1 = e[1]
for p,e in enumerate(lista2):
    nome2 = e[0]
    numero2 = e[1]
for p,e in enumerate(lista3):
    nome3 = e[0]
    numero3 = e[1]
print(nome1)
print(numero1)
print(nome2)
print(numero2)
print(nome3)
print(numero3)




