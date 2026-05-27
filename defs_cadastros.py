import time
import mysql.connector
from mysql.connector import Error
from def_MYSQLxPYTHON import MYSQLxPYTHON
from def_loading import loading
from defs_validacoes import validation, validarProf

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

       print("\nprofessor cadastrado com sucesso")
       print("====================")
       time.sleep(3)
       return


def cadastro():
    conn = MYSQLxPYTHON()
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