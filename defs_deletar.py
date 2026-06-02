import time
import mysql.connector
from mysql.connector import Error
from MYSQLxPYTHON import *

def deletarAluno():
   conn = conectar()
   cursor = conn.cursor()

   try:
      id_deletar = int(input("digite o ID do aluno: "))
   except ValueError:
      print("digite um ID válido")
      time.sleep(3)
      return

   try:
      cursor.execute("DELETE FROM alunos WHERE id_aluno = %s",(id_deletar,))
      conn.commit()

      if cursor.rowcount > 0:
         print("aluno deletado")
         time.sleep(3)
         return
      else:
         print("nenhum aluno com esse ID")
         time.sleep(3)
         return
   except Error as e:
      print(f"erro ao deletar aluno: {e}")
      time.sleep(5)
      return
   finally:
      cursor.close()
      conn.close()

def deletarProfessor():
   conn = conectar()
   cursor = conn.cursor()

   try:
      id_deletar = int(input("digite o ID do professor: "))
   except ValueError:
      print("digite um ID válido")
      time.sleep(3)
      return

   try:
      cursor.execute("DELETE FROM professores WHERE id_professor = %s",(id_deletar,))
      conn.commit()

      if cursor.rowcount > 0:
         print("professor deletado")
         time.sleep(3)
         return
      else:
         print("nenhum professor com esse ID")
         time.sleep(3)
         return
   except Error as e:
      print(f"erro ao deletar professor: {e}")
      time.sleep(5)
      return
   finally:
      cursor.close()
      conn.close()