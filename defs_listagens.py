import mysql.connector
import time
from mysql.connector import Error
from MYSQLxPYTHON import conectar

def listaAluno():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
         SELECT
            a.id_aluno,
            a.nome,
            a.idade,
            c.curso
         FROM alunos a
         INNER JOIN cursos c
            ON a.fk_idcurso = c.id_curso
    """)
    resultados = cursor.fetchall()

    if not resultados:
       print("nenhum aluno cadastrado")
       time.sleep(3)
       return

    for id_aluno, nome, idade, curso in resultados:
       print(f"\nID: {id_aluno} || Nome: {nome} || Idade: {idade} || Curso: {curso}")

    time.sleep(5)
    return

def listaProf():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("""
      SELECT
         p.id_professor,
         p.nome,
         p.idade,
         m.materia,
         c.curso
      FROM professores p
      INNER JOIN materias m
         ON p.fk_idmateria = m.id_materia
      INNER JOIN cursos c
         ON p.fk_idcurso = c.id_curso
   """)
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhum professor cadastrado")
      time.sleep(3)
      return

   for id_professor, nome, idade, materia, curso in resultados:
      print(f"\nID: {id_professor} || Nome: {nome} || Idade: {idade} || Matéria: {materia} || Curso: {curso}")

   time.sleep(5)
   return

def listaNotas():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("""
      SELECT
         n.id_nota,
         n.nota,
         m.materia,
         a.nome
      FROM notas n
      INNER JOIN materias m
         ON n.fk_idmateria = m.id_materia
      INNER JOIN alunos a
         ON n.fk_idaluno = a.id_aluno
   """)
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhuma nota cadastrada")
      time.sleep(3)
      return
   
   for id_nota, nota, materia, aluno in resultados:
      print(f"\nID: {id_nota} || Nota: {nota} || Matéria: {materia} || Aluno: {aluno}")

   time.sleep(5)
   return

def listaCursos():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM cursos ORDER BY id_curso ASC")
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhum curso no sistema")
      time.sleep(3)
      return
   
   for curso in resultados:
      print(f"ID: {curso[0]} || Curso: {curso[1]}")

   time.sleep(3)
   return

def listaMaterias():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM materias ORDER BY id_materia ASC")
   resultados = cursor.fetchall()

   for materia in resultados:
      print(f"ID: {materia[0]} || Matéria: {materia[1]}")

   time.sleep(3)
   return