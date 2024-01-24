from bancodados import insertInfo
from bancodados import listarAlunos
from bancodados import removeAluno
from bancodados import atualizarCadastro
from bancodados import buscarAluno
from bancodados import mediaEscola
from bancodados import idadeAlunos
from bancodados import alunosAprovados
from bancodados import criarTabela
from bancodados import sair

while True:
    
    print("------------------ Menu ---------------")
    print("1 - Buscar")
    print("2 - Cadastrar tabela")
    print("3 - Cadastrar aluno")
    print("4 - Apagar cadastro")
    print("5 - Alunos matriculados")
    print("6 - Atualizar cadastro")
    print("7 - Calcular media da escola")
    print("8 - Filtro de alunos por idade")
    print("9 - Alunos aprovados")
    print("0 - Sair")

    print("---------------------------------------")
    select = input("Escolha uma opção do menu: ")
    print("---------------------------------------")

    if select == '1':# BUSCAR
        print("")
        buscarAluno()

    elif select == '2':# CADATRAR TABELA
        print("")
        print("Criar nova tabela em banco de dados")
        criarTabela()

    elif select == '3':# CADASTRO ALUNO
        print("")
        print("Cadastro de aluno. Insira as informações abaixo")
        insertInfo()

    elif select == '4':#APAGAR CADASTRO
        print("")
        print("Para desmatricular um aluno informe seu numero de matricula!")
        removeAluno()
        
    elif select == '5':# LISTAR TODOS OS ALUNOS MATRICULADOS NA TABELA
        print("")
        print("LISTA DE ALUNOS MATRICULADOS NA ESCOLA")
        listarAlunos()

    elif select == '6':# ATUALIZAR CADASTRO
        print("")
        print("Atualização de cadastro. Insira as novas informações abaixo")
        atualizarCadastro()

    elif select == '7':# CALCULAR MEDIA DA ESCOLA
        print("")
        mediaEscola()

    elif select == '8':# IRA FILTRAR ALUNOS POR UMA IDADE ESCOLHIDA
        print("")
        print("Insira qual idade minima que deve ser exibida")
        idadeAlunos()

    elif select == '9':# IRA MOSTRAR APENAS OS ALUNOS APROVADOS, NOTAS ACIMA DE 6
        print("")
        print("Lista de alunos APROVADOS!")
        alunosAprovados()
    
    elif select == '0':#SAIR E PARA O PROGRAMA
        print("")
        print("Ate logo, volte sempre!")
        sair()
        break

    else: # CASO O USUARIO ESCOLHA UMA OPCAO QUE NAO EXISTE
        print("")
        print("Opção inválida. Por favor, escolha uma opção válida")
        print("")
        
    

 