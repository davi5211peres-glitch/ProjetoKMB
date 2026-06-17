import random 
import time
import os
from MYSQLxPYTHON import *
from def_loading import *
from defs_validacoes import *
from defs_cadastros import *
from defs_listagens import *
from defs_deletar import *
from def_atualizacoes import *

delay = random.randint(1 , 2)
alunosC = []
profC = []
 
import mysql.connector
from mysql.connector import Error

#oi
#marca de presença


def menuProf():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n|====================")
     print("|𝙱𝙴𝙼 𝚅𝙸𝙽𝙳𝙾 𝙰𝙾 𝚂𝙸𝚂𝚃𝙴𝙼𝙰")
     print("|====================")

     print("| 1 - mudar nota")
     print("| 2 - ver a lista de alunos")
     print("| 3 - ver a lista de professores")
     print("| 4 - ver a lista de notas")
     print("| 5 - ver a lista de matérias")
     print("| 6 - adicionar nota")
     print("| 7 - voltar para a tela de login")
     print("| 0 - sair do sistema")

     escolha = input("|   - qual sera sua escolha: ")

     if escolha == "1":
         mudarNota()

     if escolha == "2":
         listaAluno()

     elif escolha == "3":
         listaProf()
     
     elif escolha == "4":
        listaNotas()

     elif escolha == "5":
        listaMaterias()

     elif escolha == "6":
         adicionarNota()

     elif escolha == "7":
        print("| voltando...")
        time.sleep(2)
        login()

     elif escolha == "0":
        print("| saindo...")
        time.sleep(2)
        break
     else:
        print("| erro\n")
        time.sleep(2)


def menuAluno():
    while True:
     os.system('cls' if os.name == 'nt' else 'clear')
     print("\n|====================")
     print("|𝙱𝙴𝙼 𝚅𝙸𝙽𝙳𝙾 𝙰𝙾 𝚂𝙸𝚂𝚃𝙴𝙼𝙰")
     print("|====================\n")
     print("| 1 - ver notas")
     print("| 2 - ver materias")
     print("| 3 - ver os professores")
     print("| 4 - voltar para a tela de login")
     print("| 0 - sair")

     escolha = input("|   - qual sera sua escolha: ")

     if escolha == "1":
        listaNotas()

     if escolha == "2":
        listaMaterias()
    
     elif escolha == "3":
        listaProf()

     elif escolha == "4":
        print("\n| voltando...")
        time.sleep(2)
        login()

     elif escolha == "0":
        print("| saindo...")
        time.sleep(2)
        break
     else:
        print("| erro")
        time.sleep(2)

def menuSecretaria():
   while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n|====================")
      print("|𝙱𝙴𝙼 𝚅𝙸𝙽𝙳𝙾 𝙰𝙾 𝚂𝙸𝚂𝚃𝙴𝙼𝙰")
      print("|====================\n")
      print("| 1 - deletar aluno do sistema")
      print("| 2 - deletar professor do sistema")
      print("| 3 - cadastrar aluno")
      print("| 4 - cadastrar professor")
      print("| 5 - fazer alteração na conta do aluno")
      print("| 6 - fazer alteração na conta do professor")
      print("| 0 - voltar para a tela de login")

      escolha = input("\nqual sera sua escolha: ")

      if escolha == "1":
         listaAluno()
         deletarAluno()

      elif escolha == "2":
         listaProf()
         deletarProfessor()

      elif escolha == "3":
         cadastroAluno()

      elif escolha == "4":
         cadastroProfessor()

      elif escolha == "5":
         mudarAluno()

      elif escolha == "6":
         mudarProf()

      elif escolha == "0":
        print("| voltando...")
        time.sleep(2)
        login()

      else:
         print("| erro\n")
         time.sleep(2)

def login():
  while True:  
   os.system('cls' if os.name == 'nt' else 'clear')
   print("|=========================")
   print("|==========LOGIN==========")
   print("|=========================")

   usuario = input("| usuario: ").lower()
   senha = input("| senha: ")

   if usuario == "professor":
      menuProf()

   elif usuario == "secretaria":
      menuSecretaria()

   elif usuario == "aluno":
      menuAluno()

   else:
      print("| usuario não encontrado")
      time.sleep(2)
      continue
   
   break