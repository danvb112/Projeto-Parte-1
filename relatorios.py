import turmas
import arquivos

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
            """.format(turma["disciplina"]["codigo"], turma["periodo"],turma["nome_turma"], turma["disciplina"]["nome"], turma["professor"]["nome"]))
            for aluno in turma['alunos']:
                print("""
                    ---------------------------------
                    Aluno(a): {}     CPF{}   Nota:____  Assinatura:____________    
                    """.format(aluno["nome"],aluno["cpf"]))


if __name__ == "__main__":
    arquivos.carregar_dados()
    renderizar_ata_exercicio(turmas.turmas)