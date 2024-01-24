import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='escola',user='root', password='')

if conexao.is_connected():
    bd_info = conexao.get_server_info()
    print("-----------------------------------------------------------")
    print("Conectado ao banco de dados: ", bd_info)
    print("-----------------------------------------------------------")
    print("")

cursorConexao = conexao.cursor()

def criarTabela():
    print("----------------------------------------------------------------")
    print("Tabela sera criada com os seguintes colunas: NOME, IDADE E NOTA")
    nomeTabela = input("Insira um nome para a tabela: ")
    print("----------------------------------------------------------------")

    tabela = f"""CREATE TABLE {nomeTabela} (
    matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    idade INT NOT NULL,
    nota DECIMAL(2, 1) NOT NULL
    );"""

    cursorConexao.execute(tabela)
    conexao.commit()
    print("---------------------------------------")
    print("Nova Tabela criada com sucesso!")
    print("---------------------------------------")
    print("")


def buscarAluno(): 
    while True:
        print("-------------------------------------------------------")
        print("Insira as informações necessarias para buscar o aluno")
        buscar = input("Nome e sobrenome (ou '0' para sair): ")
        print("-------------------------------------------------------")
        
        consulta = """SELECT * FROM escola WHERE nome = %s"""
        cursorConexao.execute(consulta, (buscar,))
        aluno = cursorConexao.fetchone()

        if aluno:
            print("------------------------")
            print("Aluno encontrado:")
            print("Matrícula:", aluno[0])
            print("Nome:", aluno[1])
            print("Idade:", aluno[2])
            print("Nota:", aluno[3])
            print("------------------------")

        elif buscar == '0':
            break

        else:
            print("---------------------------------------")
            print("Nenhum aluno encontrado com esse nome.")
            print("---------------------------------------")
    print("")

def insertInfo():
    print("---------------------------------------")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Insira a nota do aluno: "))
    print("---------------------------------------")

    insertDados = """insert into escola (nome, idade, nota) values (%s,%s,%s)"""
    tabelaInfo = (nome, idade, nota)

    cursorConexao.execute(insertDados,tabelaInfo)
    conexao.commit()
    print("---------------------------------------")
    print("Cadastro criado com sucesso!")
    print("---------------------------------------")
    print("")

def atualizarCadastro():
    while True:
        print("---------------------------------------")
        print("Menu")
        print("1 - Modificar o nome do aluno")
        print("2 - Alterar a nota")
        print("3 - Alterar nota e nome do aluno")
        print("4 - Sair")
        print("---------------------------------------")

        print("---------------------------------------")
        select = input("Escolha umas das opções: ")
        print("---------------------------------------")

        if select == '1':# ALTERAR O NOME DO ALUNO
            print("-------------------------------------------------")
            matricula = int(input("Informe a matrícula do aluno: "))
            nome = input("Insira o nome do aluno: ")
            print("-------------------------------------------------")

            atualizarInfo = "UPDATE escola SET nome = %s WHERE matricula = %s"
            valores = (nome, matricula)

            cursorConexao.execute(atualizarInfo, valores)
            conexao.commit()
            
            if cursorConexao.rowcount > 0:
                print("---------------------------------------")
                print("Cadastro atualizado com sucesso!")
                print("---------------------------------------")
            else:
                print("---------------------------------------")
                print("Deu ruim tenta de novo!")
                print("---------------------------------------")
        
        elif select == '2':# ALTERAR A NOTA DO ALUNO
            print("--------------------------------------------------")
            matricula = int(input("Informe a matrícula do aluno: "))
            nova_nota = float(input("Insira a nova nota do aluno: "))
            print("--------------------------------------------------")

            atualizarInfo = "UPDATE escola SET nota = %s WHERE matricula = %s"
            valores = (nova_nota, matricula)

            cursorConexao.execute(atualizarInfo, valores)
            conexao.commit()
            
            if cursorConexao.rowcount > 0:
                print("---------------------------------------")
                print("Cadastro atualizado com sucesso!")
                print("---------------------------------------")
            else:
                print("---------------------------------------")
                print("Deu ruim tenta de novo!")
                print("---------------------------------------")
        
        elif select == 3:# ALTERAR NOTA E NOME DO ALUNO
            print("-------------------------------------------------")
            matricula = int(input("Informe a matrícula do aluno: "))
            nome = input("Insira o nome do aluno: ")
            nova_nota = float(input("Insira a nova nota do aluno: "))
            print("-------------------------------------------------")

            atualizarInfo = "UPDATE escola SET nome = %s, nota = %s WHERE matricula = %s"
            valores = (nome, nova_nota, matricula)

            cursorConexao.execute(atualizarInfo, valores)
            conexao.commit()
            
            if cursorConexao.rowcount > 0:
                print("---------------------------------------")
                print("Cadastro atualizado com sucesso!")
                print("---------------------------------------")
            else:
                print("---------------------------------------")
                print("Deu ruim tenta de novo!")
                print("---------------------------------------")

        else:
            break
    print("")

def removeAluno():
    print("------------------------------------------------")
    matricula = int(input("Informe a matricula do aluno: "))
    print("------------------------------------------------")

    while True:
        print("---------------------------------------")
        print("Menu")
        print("1 - DESEJA MESMO APAGAR O CADASTRO?")
        print("2 - Sair")
        print("---------------------------------------")

        print("------------------------------------------")
        select = input("Escolha uma das opções do menu: ")
        print("------------------------------------------")

        if select == '1':
            removerInfo = """DELETE FROM escola WHERE matricula = %s"""
            cursorConexao.execute(removerInfo, (matricula,))
            conexao.commit()
            print("---------------------------------------")
            print("Aluno removido com sucesso!")
            print("---------------------------------------")
            break

        else:
            break
    print("")

def listarAlunos():
    consultar = """select * from escola"""
    cursorConexao.execute(consultar)

    lista = cursorConexao.fetchall()

    for aluno in lista:
        print("------------------------")
        print("Matricula: ", aluno[0])
        print("Nome: ", aluno[1])
        print("Idade: ", aluno[2])
        print("Nota: ", aluno[3])
        print("------------------------")

    print("")
    cursorConexao.close()

def mediaEscola():
    consultar = """select * from escola"""
    cursorConexao.execute(consultar)

    notas = cursorConexao.fetchall()

    somaNotas = sum(contador[3] for contador in notas)
    quantidadeAlunos = len(notas)

    if quantidadeAlunos > 0:
        mediaNotas = somaNotas / quantidadeAlunos
        print("-----------------------------------------------")
        print(f"Média das notas da escola: {mediaNotas:.2f}")
        print("-----------------------------------------------")
    
    print("")
      
def idadeAlunos():
    print("-----------------------------------------------------------------")
    idade = int(input("Insira a idade mínima dos alunos a serem exibidos: "))
    print("-----------------------------------------------------------------")

    consultar = """SELECT * FROM escola WHERE idade >= %s"""
    cursorConexao.execute(consultar, (idade,))
    alunosFiltrados = cursorConexao.fetchall()

    for aluno in alunosFiltrados:
        print("------------------------")
        print("Nome: ", aluno[1])
        print("Idade: ", aluno[2])
        print("------------------------")
        
    cursorConexao.close()

    if not alunosFiltrados:
        print("---------------------------------------------------------------")
        print(f"Nenhum aluno encontrado com idade igual ou superior a {idade}")
        print("---------------------------------------------------------------")
    
    print("")


def alunosAprovados():
    consultar = """SELECT * FROM escola WHERE nota >= 6"""
    cursorConexao.execute(consultar)
    alunosFiltrados = cursorConexao.fetchall()

    if alunosFiltrados:
        print("------------------------")
        for aluno in alunosFiltrados:
            print("Nome: ", aluno[1])
            print("Nota: ", aluno[3])
            print("------------------------")
    else:
        print("---------------------------------------")
        print("Nenhum aluno aprovado!")
        print("---------------------------------------")
    print("")

def sair():
    conexao.close()
    print("---------------------------------------")
    print("Conexao Encerrada!")
    print("---------------------------------------")