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
 
def validar(nome,idade,curso):
    if nome.strip() == "" or curso.strip() == "":
        print("erro no nome ou no curso encontrado")
        return False
    
    if not idade.isdigit():
        print("erro na idade foi encontrado")
        return False

    if not nome.replace(" ", "").isalpha() or not curso.replace(" ", "").isalpha():
        print("erro no nome ou no curso encontrado")
        return False
    return True

def validarProf(professor, turmaP, idadeP, materia):

    if professor.strip() == "":
       print("erro encontrado (1)")

    if turmaP.strip() == "":
       print("erro encontrado (2)")
       return False
    
    if idadeP.strip() == "":
       print("erro encontrado (3)")
       return False
    
    if materia.strip() == "":
       print("erro encontrado (4)")
       return False
    
    if not professor.isalpha():
        print("erro  encontrado (5)")
        return False

    if not materia.isalpha():
        print("erro encontrado (6)")
        return False

    if not turmaP.isdigit() or not idadeP.isdigit():
        print("erro encontrado (7)")
        return False
    return True

def loading():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================")

def cadastroProfessor():
    conn = MYSQLxPYTHON()
    cursor = conn.cursor()

    loading()

    professor = input("nome do professor: ")
    turmaP = input("qual a turma que ele da aula: ")
    idadeP = input("qual a idade: ")
    materia = input("qual é a materia que da aula: ")

    if validarProf(professor,turmaP,idadeP,materia):
       profs = [professor,int(turmaP),int(idadeP),materia]
       profC.append(profs)

       print("\nprofessor cadastrado com sucesso")
       print("====================")
       time.sleep(3)
       return


def cadastro(nome,idade,curso):
    conn = MYSQLxPYTHON()
    cursor = conn.cursor()

    loading()

    sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"

    try:
        if validar(nome,idade,curso):
            cursor.execute(sql, (nome,idade,curso))
            conn.commit()
            print("\nusuario cadastrado com sucesso")
            time.sleep(3)
            return
    except Error as e:
        print(f"erro no cadastro: {e}")
        time.sleep(3)
        return
    finally:
       cursor.close()
       conn.close()

def lista():
    conn = MYSQLxPYTHON()
    cursor = conn.cursor()

    sql = "SELECT * FROM alunos"

    cursor.execute(sql)
    resultados = cursor.fetchall()

    if not resultados:
       print("nenhum aluno cadastrado")
       time.sleep(3)
       return

    for aluno in resultados:
       print(f"ID: {aluno[0]} || Nome: {aluno[1]} || Idade: {aluno[2]} || Curso: {aluno[3]}")
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
            print(f"idade: {profs[2]}")
            print(f"materia: {profs[3]}")
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

def deletarAluno(id_deletar):
   conn = MYSQLxPYTHON()
   if conn is None: return

   cursor = conn.cursor()
   sql = "DELETE FROM alunos WHERE id_aluno = %s"

   try:
      cursor.execute(sql, (id_deletar,))
      conn.commit()

      if cursor.rowcount > 0:
         print("aluno deletado")
      else:
         print("nenhum aluno com esse ID")
   except Error as e:
      print(f"erro ao deletar aluno: {e}")
   finally:
      cursor.close()
      conn.close()

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
         lista()
         id_deletar = input("digite o ID do aluno: ")
         if id_deletar.isdigit():
            deletarAluno(int(id_deletar))
         else:
            print("digite um ID válido")

      elif escolha == "2":
         print("oi2")

      elif escolha == "3":
         nome = input("qual aluno você quer cadastrar: ")
         idade = input("qual a idade: ")
         curso = input("qual é o curso: ")
         if idade.isdigit():
            cadastro(nome,idade,curso)
         else:
            print("idade precisa ser número")

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
