import mysql.connector
import time
from mysql.connector import Error
from MYSQLxPYTHON import conectar

def lista():
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
       print(f"ID: {id_aluno} || Nome: {nome} || Idade: {idade} || Curso: {curso}")

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
         p.materia,
         c.curso
      FROM professores p
      INNER JOIN cursos c
         ON p.fk_idcurso = c.id_curso
   """)
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhum professor cadastrado")
      time.sleep(3)
      return

   for id_professor, nome, idade, materia, curso in resultados:
      print(f"ID: {id_professor} || Nome: {nome} || Idade: {idade} || Matéria: {materia} || Curso: {curso}")

   time.sleep(5)
   return

def listaNotas():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM notas")
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhuma nota cadastrada")
      time.sleep(3)
      return
   
   for nota in resultados:
      print(f"ID: {nota[0]} || Nota: {nota[1]} || Matéria: {nota[2]} || ID do aluno: {nota[3]} || ID do professor: {nota[4]}")

   time.sleep(5)
   return

def listaCursos():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM cursos")
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhum curso no sistema")
      time.sleep(3)
      return
   
   for curso in resultados:
      print(f"ID: {curso[0]} || Curso: {curso[1]}")

   time.sleep(3)
   return
