import time
import mysql.connector
from mysql.connector import Error
from MYSQLxPYTHON import *
from def_loading import *
from defs_validacoes import *
from defs_listagens import *

def cadastroProfessor():
    conn = conectar()
    cursor = conn.cursor()

    loading()

    professor = input("| nome do professor: ")
    idadeP = input("| qual a idade: ")
    materia = input("| qual é a materia que da aula: ")
    curso = input("| qual é o curso que ele da aula: ")

    sql = "INSERT INTO professores (nome, idade, materia, curso) VALUES (%s, %s, %s, %s)"

    try:
        if validarProf(professor,idadeP,materia,curso):
            cursor.execute(sql, (professor,idadeP,materia,curso))
            conn.commit()
            print("\n| professor cadastrado com sucesso")
            print("| ====================")
            time.sleep(3)
            return
    except Error as e:
        print(f"erro no cadastro: {e}")
        time.sleep(3)
        return
    finally:
        cursor.close()
        conn.close()


def cadastroAluno():
    conn = conectar()
    cursor = conn.cursor()

    loading()

    nome = input("| qual aluno você quer cadastrar: ")
    idade = input("| qual a idade: ")

    listaCursos()
    id_curso = input("| qual é o ID do curso: ").lower()

    cursor.execute("SELECT id_curso FROM cursos WHERE id_curso = %s", (id_curso,))
    if not cursor.fetchone():
       print("ID não existe")
       time.sleep(2)
       return

    sql = "INSERT INTO alunos (nome, idade, fk_idcurso) VALUES (%s, %s, %s)"

    try:
        if validation(nome,idade,id_curso):
            cursor.execute(sql, (nome,idade,id_curso))
            conn.commit()
            print("\n| aluno cadastrado com sucesso")
            time.sleep(3)
            return
    except Error as e:
        print(f"erro no cadastro: {e}")
        time.sleep(3)
        return
    finally:
       cursor.close()
       conn.close()

def adicionarNota():
   conn = conectar()
   cursor = conn.cursor()

   print("\n| aviso! para cadastrar uma nota deve haver pelo menos um aluno e um professor cadastrado")
   time.sleep(2)
   prosseguir = input("| deseja prosseguir? (s/n): ")
   
   if prosseguir.lower() != "s" or prosseguir.lower() != "n":
      print("| digite apenas s ou n")
      time.sleep(2)
      return

   if prosseguir.lower() == "n":
      return
   elif prosseguir.lower() == "s":
      cursor.execute("SELECT COUNT(*) FROM alunos")
      total_alunos = cursor.fetchone()[0]
      
      cursor.execute("SELECT COUNT(*) FROM professores")
      total_professores = cursor.fetchone()[0]

      if total_alunos == 0 or total_professores == 0:
         print("\n| erro encontrado. não há alunos e/ou professores presentes")
         print(f"| alunos cadastrados: {total_alunos} || professores cadastrados: {total_professores}")
         time.sleep(4)
         return
      
      listaAluno()
      time.sleep(2)
      
      try:
         selectAluno = int(input("\n| qual o ID do aluno que deseja adicionar nota?: "))
      except ValueError:
         print("| digite um ID válido")
         time.sleep(2)
         return

      cursor.execute("SELECT id_aluno FROM alunos WHERE id_aluno = %s", (selectAluno,))
      if not cursor.fetchone():
         print("| ID não existe")
         time.sleep(2)
         return
      
      materia = input("\n| digite a matéria: ")

      if materia.strip() == "" or not materia.replace(" ", "").isalpha():
         print("| erro no cadastro: campo vazio ou matéria inválida")
         time.sleep(2)
         return
      
      try:
         nota = float(input("\n| digite a nota do aluno (ex: 8.5): "))
         if nota < 0 or nota > 10:
            print("| nota deve ser entre 0 e 10.")
            time.sleep(2)
            return 
      except ValueError:
        print("| digite um valor numérico para a nota.")
        time.sleep(2)
        return
      
      try:
         sql = """
          INSERT INTO notas (notas, materia, fk_idaluno)
          VALUES (%s, %s, %s)
         """
         valores = (nota, materia, selectAluno)

         cursor.execute(sql, valores)
         conn.commit()

         print("| nota cadastrada")
         time.sleep(2)  
      except Error as e:
         print(f"| erro no cadastro: {e}")
         time.sleep(5)
      finally:
         cursor.close()
         conn.close()

      return
