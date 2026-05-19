import random 
import time
import os

delay = random.randint(1 , 6)
alunosC = []

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
       return

def lista():
    if len(alunosC) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for i, alunos in enumerate(alunosC):
            print(f"\naluno {i+1}:")
            print(f"aluno: {alunos[0]}")
            print(f"turma: {alunos[1]}")
            print(f"curso: {alunos[2]}")
            print(f"idade: {alunos[3]}")

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
     print("\nbem vindo ao sistema do professor")
     print("1-cadastrar aluno\n2-ver a lista de alunos\n3-adicionar nota\n4-voltar para a tela de login\n0-sair do sistema")

     escolha = input("qual sera sua escolha: ")

     if escolha == "1":
         cadastro()
    
     elif escolha == "2":
         lista()

     elif escolha == "3":
         notas()

     elif escolha == "4":
        print("voltando...")
        time.sleep(2)
        login()

     elif escolha == "0":
        print("saindo...")
        time.sleep(2)
        break
     else:
        print("erro\n")

def menuAluno():
    while True:
     print("\nbem vindo ao sistema")
     print("1-se cadastrar\n2-ver materias\n3-voltar para a tela de login\n0-sair")

     escolha = input("qual sera sua escolha: ")

     if escolha == "1":
        cadastro()

     if escolha == "2":
        cadastro()
    
     elif escolha == "3":
        print("voltando...")
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
      print("\nbem vindo ao sistema")
      print("1-deletar aluno do sistema\n")

      escolha = input("qual sera sua escolha: ")

      if escolha == "1":
         print("oi")

      else:
         print("erro\n")

def login():
  while True:  
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
