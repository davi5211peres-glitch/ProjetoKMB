import random 
import time

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
 
def validar(nome, turma, curso):
    if nome.strip() == "" or curso.strip() == "":
        print("erro no nome ou na cidade encontrado")
        return False
    if not turma.isdigit():
        print("erro na idade foi encontrado")
        return False
    return True

def cadastro():
    print("iniciando cadastro de aluno")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    print("🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(delay)
    print("🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛")
    time.sleep(1)
    print("🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛")
    time.sleep(3)
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛")
    time.sleep(delay)
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")

    aluno = input("qual aluno você quer cadastrar: ")
    turma = input("qual a turma dele(a): ")
    curso = input("qual é o curso: ")

    if validar(aluno,turma,curso):
       alunos = [aluno,int(turma),curso]
       alunosC.append(alunos)
       print("usuario cadastrado com sucesso")
       return

def lista():
    if len(alunosC) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(alunosC):
            print(f"\nUsuário {i+1}:")
            print(f"Nome: {usuario[0]}")
            print(f"Idade: {usuario[1]}")
            print(f"Cidade: {usuario[2]}")

    return 

def notas():
    print


def menu():
    while True:
     print("bem vindo ao sistema de cadastramento aleatorio")
     print("1-cadastrar\n2-lista\n3-sair")

     escolha = input("qual sera sua escolha: ")

     if escolha == "1":
        cadastro()
    
     elif escolha == "2":
        lista()

     elif escolha == "3":
         print

    
     elif escolha == "4":
        print("saindo...")
        time.sleep(2)
        break
     else:
        print("escolha uma das opções acima\n")

menu()
