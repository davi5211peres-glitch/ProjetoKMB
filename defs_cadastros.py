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

    listaMaterias()
    id_materia = input("| qual é o ID da materia que da aula: ")

    cursor.execute("SELECT id_materia FROM materias WHERE id_materia = %s", (id_materia,))
    if not cursor.fetchone():
       print("ID não existe")
       time.sleep(2)
       return

    sql = "INSERT INTO professores (nome, idade, fk_idmateria) VALUES (%s, %s, %s)"

    try:
        if validarProf(professor,idadeP,id_materia):
            cursor.execute(sql, (professor,idadeP,id_materia))
            conn.commit()
            print("\n| 𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁 𝙲𝙰𝙳𝙰𝚂𝚃𝚁𝙰𝙳𝙾 𝙲𝙾𝙼 𝚂𝚄𝙲𝙴𝚂𝚂𝙾")
            print("| ====================")
            time.sleep(3)
            return
    except Error as e:
        print(f"| erro no cadastro: {e}")
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

    listaTurmas()
    id_turma = input("| qual é o ID da turma: ").lower()

    cursor.execute("SELECT id_curso FROM cursos WHERE id_curso = %s", (id_curso,))
    if not cursor.fetchone():
       print("| ID não existe")
       time.sleep(2)
       return

    cursor.execute("SELECT id_turma FROM turmas WHERE id_turma = %s", (id_turma,))
    if not cursor.fetchone():
       print("| ID não existe")
       time.sleep(2)
       return

    sql = "INSERT INTO alunos (nome, idade, fk_idcurso, fk_idturma) VALUES (%s, %s, %s, %s)"

    try:
        if validation(nome,idade,id_curso,id_turma):
            cursor.execute(sql, (nome,idade,id_curso,id_turma))
            conn.commit()
            print("|")
            print("| aluno cadastrado com sucesso")
            time.sleep(3)
            return
    except Error as e:
        print(f"| erro no cadastro: {e}")
        time.sleep(3) 
        return
    finally:
       cursor.close()
       conn.close()

def adicionarNota():
   conn = conectar()
   cursor = conn.cursor()
   print("|")
   print("| aviso! para cadastrar uma nota deve haver pelo menos um aluno e um professor cadastrado")
   time.sleep(2)
   prosseguir = input("| deseja prosseguir? (s/n): ")

   if prosseguir.lower() == "n":
      return
   elif prosseguir.lower() == "s":
      cursor.execute("SELECT COUNT(*) FROM alunos")
      total_alunos = cursor.fetchone()[0]

      if total_alunos == 0:
         print("|")
         print("| erro encontrado. não há alunos presentes")
         print(f"| alunos cadastrados: {total_alunos}")
         time.sleep(4)
         return
      
      listaAluno()
      
      try:
         selectAluno = int(input("\n| qual o ID do aluno que deseja adicionar nota?: "))
      except ValueError:
         print("| digite um ID válido")
         time.sleep(2)
         return

      cursor.execute("SELECT id_aluno FROM alunos WHERE id_aluno = %s", (selectAluno,))
      if not cursor.fetchone():
         print("|")
         print("| ID não existe")
         time.sleep(2)
         return
      
      listaMaterias()
      try:
         print("|")
         selectMateria = int(input("| digite o ID da matéria: "))
      except ValueError:
         print("| digite um ID válido")
         time.sleep(2)
         return

      cursor.execute("SELECT id_materia FROM materias WHERE id_materia = %s", (selectMateria,))
      if not cursor.fetchone():
         print("| ID não existe")
         time.sleep(2)
         return

      try:
         print("|")
         nota = float(input("| digite a nota do aluno (ex: 8.5): "))
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
          INSERT INTO notas (nota, fk_idmateria, fk_idaluno)
          VALUES (%s, %s, %s)
         """
         valores = (nota, selectMateria, selectAluno)

         cursor.execute(sql, valores)
         conn.commit()

         print("| nota cadastrada")
         time.sleep(2)  
      except Error as e:
         print(f"| erro no cadastro: {e}")
         time.sleep(5)
         return
   else:
      print("| digite apenas s ou n")
      time.sleep(2)
      return

   cursor.close()
   conn.close()
