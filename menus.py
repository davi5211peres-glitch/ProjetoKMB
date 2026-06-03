import random 
import time
import os
from MYSQLxPYTHON import *
from def_loading import *
from defs_validacoes import *
from defs_cadastros import *
from defs_listagens import *
from defs_deletar import *

delay = random.randint(1 , 2)
alunosC = []
profC = []
 
import mysql.connector
from mysql.connector import Error

#oi
#marca de presença

def adicionarNota():
   conn = conectar()
   cursor = conn.cursor()

   print("\naviso! para cadastrar uma nota deve haver pelo menos um aluno e um professor cadastrado")
   time.sleep(2)
   prosseguir = input("deseja prosseguir? (s/n): ")
   
   if prosseguir.lower() == "n":
      return menuProf()
   elif prosseguir.lower() == "s":
      cursor.execute("SELECT COUNT(*) FROM alunos")
      total_alunos = cursor.fetchone()[0]
      
      cursor.execute("SELECT COUNT(*) FROM professores")
      total_professores = cursor.fetchone()[0]

      if total_alunos == 0 or total_professores == 0:
         print("\nerro encontrado. não há alunos e/ou professores presentes")
         print(f"alunos cadastrados: {total_alunos} || professores cadastrados: {total_professores}")
         time.sleep(4)
         return menuProf()
      
      
      lista()
      time.sleep(2)
      
      try:
         selectAluno = int(input("\nqual o ID do aluno que deseja adicionar nota?: "))
      except ValueError:
         print("digite um ID válido")
         time.sleep(2)
         return menuProf()

      cursor.execute("SELECT id_aluno FROM alunos WHERE id_aluno = %s", (selectAluno,))
      if not cursor.fetchone():
         print("ID não existe")
         time.sleep(2)
         return menuProf()
      
      listaProf()
      time.sleep(2)

      try:
         selectProf = int(input("qual professor está atrelado a esta nota?: "))
      except ValueError:
         print("digite um ID válido")
         time.sleep(2)
         return menuProf()
      
      cursor.execute("SELECT id_professor FROM professores WHERE id_professor = %s", (selectProf,))
      if not cursor.fetchone():
         print("ID não existe")
         time.sleep(2)
         return menuProf()
      
      materia = input("\ndigite a matéria: ")

      if materia.strip() == "" or not materia.replace(" ", "").isalpha():
         print("erro no cadastro: campo vazio ou matéria inválida")
         time.sleep(2)
         return menuProf()
      
      try:
         nota = float(input("\ndigite a nota do aluno (ex: 8.5): "))
         if nota < 0 or nota > 10:
            print("nota deve ser entre 0 e 10.")
            time.sleep(2)
            return menuProf()
      except ValueError:
        print("digite um valor numérico para a nota.")
        time.sleep(2)
        return menuProf()
      
      try:
         sql = """
          INSERT INTO notas (notas, materia, fk_idaluno, fk_idprofessor)
          VALUES (%s, %s, %s, %s)
         """
         valores = (nota, materia, selectAluno, selectProf)

         cursor.execute(sql, valores)
         conn.commit()

         print("nota cadastrada")
         time.sleep(2)  
      except Error as e:
         print(f"erro no cadastro: {e}")
         time.sleep(5)
      finally:
         cursor.close()
         conn.close()

      return menuProf()


def menuProf():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n====================")
     print("bem vindo ao sistema")
     print("====================\n")

     print("1-mudar nota")
     print("2-ver a lista de alunos")
     print("3-ver a lista de professores")
     print("4-ver a lista de notas")
     print("5-adicionar nota")
     print("6-voltar para a tela de login")
     print("0-sair do sistema")

     escolha = input("qual sera sua escolha: ")

     if escolha == "1":
         print

     if escolha == "2":
         lista()

     elif escolha == "3":
         listaProf()
     
     elif escolha == "4":
        listaNotas()

     elif escolha == "5":
         adicionarNota()

     elif escolha == "6":
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
     print("====================\n")
     print("1-ver notas")
     print("2-ver materias")
     print("3-ver os professores")
     print("4-voltar para a tela de login")
     print("0-sair")

     escolha = input("qual sera sua escolha: ")

     if escolha == "2":
        materias()
    
     elif escolha == "3":
        listaProf()

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
         listaProf()
         deletarProfessor()

      elif escolha == "3":
         cadastro()

      elif escolha == "4":
         cadastroProfessor()

      elif escolha == "7":
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