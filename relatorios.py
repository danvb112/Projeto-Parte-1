import turmas
import alunos
import disciplinas
import professores
 
def renderizar_ata_exercicio(turmas_lista):
    if len(turmas_lista) == 0:
        print("--- Não ha turmas registradas ---")
        return False
        
    print("\n--- De qual turma você quer a ata de exercicio? ---")
    turmas.listar()
    opcao = input("Digite o código da turma escolhida: ")
    for turma in turmas_lista:
        if turma["cod_turma"] == opcao:        
            print("""
            ===================================================
            Código da disciplina: {} Periodo: {} Turma: {}
            ===================================================
            Nome da disciplina: {}
            Professor: {}
            ===================================================
            """).format(turma["disciplina"]["codigo"], turma["periodo"],turma["nome_turma"], turma["disciplina"]["nome"], turma["professor"]["nome"])
            for turma in turmas_lista:
                print("""
                ---------------------------------
                Aluno(a): {}     CPF{}   Nota:____  Assinatura:____________    
                """).format(turma["alunos"]["nome"],turma["alunos"]["cpf"])

