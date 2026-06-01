import mysql.connector
import time
from mysql.connector import Error
from MYSQLxPYTHON import conectar

def lista():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    resultados = cursor.fetchall()

    if not resultados:
       print("nenhum aluno cadastrado")
       time.sleep(3)
       return

    for aluno in resultados:
       print(f"ID: {aluno[0]} || Nome: {aluno[1]} || Idade: {aluno[2]} || Curso: {aluno[3]}*")

    time.sleep(3)
    return

def listaProf():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM professores")
   resultados = cursor.fetchall()

   if not resultados:
      print("nenhum professor cadastrado")
      time.sleep(3)
      return

   for professor in resultados:
      print(f"ID: {professor[0]} || Nome: {professor[1]} || Idade: {professor[2]} || Matéria: {professor[3]} || Curso: {professor[4]}")

   time.sleep(3)
   return