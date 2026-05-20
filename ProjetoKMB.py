import random 
import time
import os
 
delay = random.randint(1 , 6)
alunosC = []
profC = []
 
import mysql.connector
from mysql.connector import Error
  
def MYSQLxPYTHON():
    try:
        conexão = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
            database = "escola",
        )
        return conexão
    except Error as e:
        print(f"Erro ao conectar ao MySQL:{e}")
        return None
 
def validar(nome, turma, curso, idade):
    if nome.strip() == "" or curso.strip() == "":
        print("erro no nome ou no curso encontrado")
        return False
    
    if not nome.isalpha() or not curso.isalpha():
        print("erro no nome ou no curso encontrado Ç")
        return False

    if not turma.isdigit() or not idade.isdigit():
        print("erro na turma foi encontrado")
        return False
    return True

def validarProf(professor, turmaP, idadeP, materia):
    if professor.strip() == "" or turmaP.strip() == "" or idadeP.strip() == "" or materia.strip() == "":
        print("erro encontrado")
        return False
    
    if not professor.isalpha():
        print("erro  encontrado")
        return False

    if not materia.isdigit():
        print("erro encontrado")
        return False

    if not turmaP.isdigit() or not idadeP.isdigit():
        print("erro encontrado")
        return False
    return True


def cadastroProfessor():
    conn = MYSQLxPYTHON()
    cursor = conn.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro de professor")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")

    professor = input("nome do professor: ")
    turmaP = input("qual a turma que ele da aula: ")
    idadeP = input("qual a idade: ")
    materia = input("qual é a materia que da aula: ")

    if validarProf(professor,turmaP,idadeP):
       profs = [professor,int(turmaP),int(idadeP),int(materia)]
       profC.append(profs)

       print("\nprofessor cadastrado com sucesso")
       time.sleep(3)
       return


def cadastro():
    conn = MYSQLxPYTHON()
    cursor = conn.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro de aluno")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")

    aluno = input("qual aluno você quer cadastrar: ")
    turma = input("qual a turma dele(a): ")
    curso = input("qual é o curso: ")
    idade = input("qual a idade: ")

    if validar(aluno,turma,curso,idade):
       alunos = [aluno,int(turma),curso,int(idade)]
       alunosC.append(alunos)

       print("\nusuario cadastrado com sucesso")
       time.sleep(3)
       return

def lista():
    if len(alunosC) == 0:
        print("Nenhum usuário cadastrado.")
        time.sleep(3)
    else:
        for i, alunos in enumerate(alunosC):
            print(f"\naluno {i+1}:")
            print(f"aluno: {alunos[0]}")
            print(f"turma: {alunos[1]}")
            print(f"curso: {alunos[2]}")
            print(f"idade: {alunos[3]}")
            time.sleep(3)

    return 

def listaProf():
    if len(profC) == 0:
        print("Nenhum usuário cadastrado.")
        time.sleep(3)
    else:
        for i, profs in enumerate(profC):
            print(f"\nprofessor {i+1}:")
            print(f"nome: {profs[0]}")
            print(f"turma que da aula: {profs[1]}")
            print(f"idade: {profs[3]}")
            time.sleep(3)

    return 

#oi
#oii

def notas():
    lista()
    selectAluno = input("qual aluno você gostaria de adicionar nota: ")
    if selectAluno not in alunosC:
     print("escolha um aluno existente")
     return


def menuProf():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n====================")
     print("bem vindo ao sistema")
     print("====================")
     print("\n2-ver a lista de alunos\n3-ver a lista de professores\n4-adicionar nota\n5-voltar para a tela de login\n0-sair do sistema")

     escolha = input("qual sera sua escolha: ")

     if escolha == "2":
         lista()

     elif escolha == "3":
         listaProf()
     
     elif escolha == "4":
         notas()

     elif escolha == "5":
        print("voltando...")
        time.sleep(2)
        login()

     elif escolha == "0":
        print("saindo...")
        time.sleep(2)
        break
     else:
        print("erro\n")

def materias():
   print

def menuAluno():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n====================")
     print("bem vindo ao sistema")
     print("====================")
     print("\n2-ver materias\n3-ver os professores\n4-voltar para a tela de login\n0-sair")

     escolha = input("qual sera sua escolha: ")

     if escolha == "2":
        materias()
    
     elif escolha == "4":
        print("\nvoltando...")
        time.sleep(2)
        login()

     elif escolha == "0":
        print("saindo...")
        time.sleep(2)
        break
     else:
        print("erro")

def menuSecretaria():
   while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n====================")
      print("bem vindo ao sistema")
      print("====================")
      print("\n1-deletar aluno do sistema\n2-deletar professor do sistema\n3-cadastrar aluno\n4-cadastrar professor\n5-voltar para a tela de login\n")

      escolha = input("\nqual sera sua escolha: ")

      if escolha == "1":
         print("oi")

      elif escolha == "2":
         print("oi2")

      elif escolha == "3":
        cadastro()

      elif escolha == "4":
         cadastroProfessor()

      elif escolha == "5":
        print("voltando...")
        time.sleep(2)
        login()

      else:
         print("erro\n")

def login():
  while True:  
   os.system('cls' if os.name == 'nt' else 'clear')
   print("=========================")
   print("==========LOGIN==========")
   print("=========================\n")

   usuario = input("usuario: ").lower()
   senha = input("senha: ")

   if usuario == "professor":
      menuProf()

   elif usuario == "secretaria":
      menuSecretaria()

   elif usuario == "aluno":
      menuAluno()

   else:
      print("usuario não encontrado")
      break

login()
