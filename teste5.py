import random 
import time
import os
from MYSQLxPYTHON import *
from def_loading import *
from defs_validacoes import *
from defs_cadastros import *
 
<<<<<<< HEAD
import random 
import time
import os
delay = random.randint(1, 6)
alunosC = []
profC = []
 
import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
)

cursor = conn.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS escola;
    """)

cursor.execute("USE escola")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        curso VARCHAR(50) NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id_professor INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        materia VARCHAR(50) NOT NULL,
        curso VARCHAR(200) NOT NULL
    );
""")

def conectar():
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

def cadastroProfessor():
    conn = conectar()
    cursor = conn.cursor()

    loading()

    professor = input("nome do professor: ")
    turmaP = input("qual a turma que ele da aula: ")
    idadeP = input("qual a idade: ")
    materia = input("qual é a materia que da aula: ")

    if validarProf(professor,turmaP,idadeP,materia):
       profs = [professor,int(turmaP),int(idadeP),materia]

       print("\nprofessor cadastrado com sucesso")
       print("====================")
       time.sleep(3)
       return


def cadastro():
    conn = conectar()
    cursor = conn.cursor()

    loading()

    sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"

    nome = input("qual aluno você quer cadastrar: ")
    idade = input("qual a idade: ")
    curso = input("qual é o curso: ")

    try:
        if validation(nome,idade,curso):
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
    print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛")
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("iniciando cadastro")
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============")


def validation(nome,idade,curso):
    if nome.strip() == "":
        print("erro encontrado (1)")
        time.sleep(3)
        return False
    
    if curso.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False
    
    if not idade.isdigit():
        print("erro encontrado (3)")
        time.sleep(3)
        return False

    if not nome.replace(" ", "").isalpha():
        print("erro encontrado (4)")
        time.sleep(3)
        return False
    
    if not curso.replace(" ", "").isalpha():
       print("erro encontrado (5)")
       time.sleep(3)
       return False
    
    return True
 
def validarProf(professor, turmaP, idadeP, materia):
  
    if professor.strip() == "":
       print("erro encontrado (1)")
       time.sleep(3)
       return
 
    if turmaP.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False 
    
    if idadeP.strip() == "":
       print("erro encontrado (3)")
       time.sleep(3)
       return False
    
    if materia.strip() == "":
       print("erro encontrado (4)")
       time.sleep(3)
       return False
    
    if not professor.isalpha():
        print("erro encontrado (5)")
        time.sleep(3)
        return False

    if not materia.isalpha():
        print("erro encontrado (6)")
        time.sleep(3)
        return False

    if not turmaP.isdigit() or not idadeP.isdigit():
        print("erro encontrado (7)")
        time.sleep(3)
        return False
    return True

def validation(nome,idade,curso):
    if nome.strip() == "":
        print("erro encontrado (1)")
        time.sleep(3)
        return False
    
    if curso.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False
    
    if not idade.isdigit():
        print("erro encontrado (3)")
        time.sleep(3)
        return False

    if not nome.replace(" ", "").isalpha():
        print("erro encontrado (4)")
        time.sleep(3)
        return False
    
    if not curso.replace(" ", "").isalpha():
       print("erro encontrado (5)")
       time.sleep(3)
       return False
    
    return True
 


=======
delay = random.randint(1 , 2)
alunosC = []
profC = []
  
import mysql.connector
from mysql.connector import Error

>>>>>>> 548f6ea3411296bf62feec4ab5f0b1b77785bf82
def lista():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    resultados = cursor.fetchall()

    if not resultados:
       print("nenhum aluno cadastrado")
       time.sleep(3)
       return

    for aluno in resultados:
       print(f"ID: {aluno[0]} || Nome: {aluno[1]} || Idade: {aluno[2]} || Curso: {aluno[3]}*")

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
#marca de presença

def notas():
    lista()
    selectAluno = input("qual aluno você gostaria de adicionar nota: ")
    if selectAluno not in alunosC:
     print("escolha um aluno existente")
     return

def deletarAluno():
   conn = conectar()
   cursor = conn.cursor()

   id_deletar = input("digite o ID do aluno: ")

   if not id_deletar.isdigit():
      print("digite um ID válido")
      time.sleep(3)
      return

   try:
      cursor.execute("DELETE FROM alunos WHERE id_aluno = %s",(id_deletar,))
      conn.commit()

      if cursor.rowcount > 0:
         print("aluno deletado")
         time.sleep(3)
         return
      else:
         print("nenhum aluno com esse ID")
         time.sleep(3)
         return
   except Error as e:
      print(f"erro ao deletar aluno: {e}")
      time.sleep(10)
      return
   finally:
      cursor.close()
      conn.close()

def menuProf():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n====================")
     print("bem vindo ao sistema")
     print("====================\n")

     print("1-mudar nota")
     print("2-ver a lista de alunos")
     print("3-ver a lista de professores")
     print("4-adicionar nota")
     print("5-voltar para a tela de login")
     print("0-sair do sistema")

     escolha = input("qual sera sua escolha: ")

     if escolha == "1":
         print

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
<<<<<<< HEAD
        print("erro\n")
=======
        os.system('cls' if os.name == 'nt' else 'clear')
        print("erro\n")
        time.sleep(2)
>>>>>>> 548f6ea3411296bf62feec4ab5f0b1b77785bf82

def materias():
   print

def menuAluno():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n====================")
     print("bem vindo ao sistema")
     print("====================\n")
     print("1-")
     print("2-ver materias")
     print("3-ver os professores")
     print("4-voltar para a tela de login")
     print("0-sair")

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
<<<<<<< HEAD
        print("erro")
=======
        os.system('cls' if os.name == 'nt' else 'clear')
        print("erro\n")
        time.sleep(2)
>>>>>>> 548f6ea3411296bf62feec4ab5f0b1b77785bf82

def menuSecretaria():
   while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n====================")
      print("bem vindo ao sistema")
      print("====================\n")
      print("1-deletar aluno do sistema")
      print("2-deletar professor do sistema")
      print("3-cadastrar aluno")
      print("4-cadastrar professor")
      print("5-fazer alteração na conta do aluno")
      print("6-fazer alteração na conta do professor")
      print("7-voltar para a tela de login")

      escolha = input("\nqual sera sua escolha: ")

      if escolha == "1":
         lista()
         deletarAluno()

      elif escolha == "2":
         print("oi2")

      elif escolha == "3":
         cadastro()

      elif escolha == "4":
         cadastroProfessor()

      elif escolha == "7":
        print("voltando...")
        time.sleep(2)
        login()

      else:
<<<<<<< HEAD
         print("erro\n")
=======
        os.system('cls' if os.name == 'nt' else 'clear')
        print("erro\n")
        time.sleep(2)
>>>>>>> 548f6ea3411296bf62feec4ab5f0b1b77785bf82

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

<<<<<<< HEAD
login()
=======
login()
>>>>>>> 548f6ea3411296bf62feec4ab5f0b1b77785bf82
