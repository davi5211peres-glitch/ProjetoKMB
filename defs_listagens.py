import mysql.connector
import time
from mysql.connector import Error
from MYSQLxPYTHON import conectar
from defs_validacoes import *

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
       print("| nenhum aluno cadastrado")
       time.sleep(3)
       return

    for id_aluno, nome, idade, curso in resultados:
       print(f"| ID: {id_aluno} | Nome: {nome} | Idade: {idade} | Curso: {curso}")

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
      print("| 𝙽𝙴𝙽𝙷𝚄𝙼 𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁 𝙲𝙰𝙳𝙰𝚂𝚃𝚁𝙰𝙳𝙾")
      time.sleep(3)
      return

   for id_professor, nome, idade, materia, curso in resultados:
      print(f"| ID: {id_professor} | Nome: {nome} | Idade: {idade} | Matéria: {materia} | Curso: {curso}")

   time.sleep(5)
   return

def listaNotas():
   conn = conectar()
   cursor = conn.cursor()

   listaAluno()
   try:
      selectAluno = int(input("Digite o ID do aluno: "))
   except ValueError:
      print("| Digite um ID válido")
      time.sleep(2)
      return
   
   cursor.execute("""
      SELECT
         n.id_nota,
         a.nome,
         ROUND(n.nota, 2),
         m.materia
      FROM notas n
      INNER JOIN alunos a
         ON n.fk_idaluno = a.id_aluno
      INNER JOIN materias m
         ON n.fk_idmateria = m.id_materia
      WHERE id_aluno = %s
   """, (selectAluno,))

   resultados = cursor.fetchall()
   if not resultados:
      print("| 𝙽E𝙽𝙷𝚄𝙼𝙰 𝙽𝙾𝚃𝙰 𝙲𝙰𝙳𝙰𝚂𝚃𝚁𝙰𝙳𝙰")
      time.sleep(3)
      return
   
   for id_nota, nota, materia, aluno in resultados:
      print(f"| ID: {id_nota} | Nota: {nota} | Matéria: {materia} | Aluno: {aluno}")

   time.sleep(5)
   return

def listaCursos():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM cursos ORDER BY id_curso ASC")
   resultados = cursor.fetchall()

   if not resultados:
      print("| 𝙽E𝙽𝙷𝚄𝙼 𝙲𝚄𝚁𝚂𝙾 𝙽𝙾 𝚂𝙸𝚂𝚃𝙴𝙼𝙰")
      time.sleep(3)
      return
   
   for curso in resultados:
      print(f"| ID: {curso[0]} | Curso: {curso[1]}")

   time.sleep(3)
   return

def listaMaterias():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM materias ORDER BY id_materia ASC")
   resultados = cursor.fetchall()

   for materia in resultados:
      print(f"| ID: {materia[0]} | Matéria: {materia[1]}")

   time.sleep(3)
   return

def listaMedia():
   conn = conectar()
   cursor = conn.cursor()

   listaAluno()
   try:
      id_busca = int(input("| Digite o ID do aluno: "))
   except ValueError():
      print("| Digite um ID válido")
      time.sleep(2)
      return

   cursor.execute("""
      SELECT
         a.id_aluno,
         a.nome,
         ROUND(AVG(n.nota), 2) AS media
      FROM alunos a
      INNER JOIN notas n ON n.fk_idaluno = a.id_aluno
      WHERE id_aluno = %s
      GROUP BY a.id_aluno, a.nome
   """, (id_busca,))

   resultados = cursor.fetchall()

   if not resultados:
      print("| sem aluno ou notas cadastradas")
      time.sleep(2)
      return

   for id_aluno, nome, media in resultados:
      if media >= 7 and media <= 10:
         situacao = "aprovado"
      elif media < 7 and media >= 4:
         situacao = "recuperação"
      elif media < 4 and media >= 0:
         situacao = "reprovado"
      print(f"\n| ID do aluno: {id_aluno} | Nome: {nome} | Média: {media} | Situação: {situacao}")

   time.sleep(5)
   return
