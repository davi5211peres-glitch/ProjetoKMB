import time
import mysql.connector
from mysql.connector import Error
from MYSQLxPYTHON import *
from defs_listagens import *

def deletarAluno():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT COUNT(*) FROM alunos")#SELECT CONTE vai contar quantos alunos tem
   total_alunos = cursor.fetchone()[0]#busca um item na lista

   if total_alunos == 0:
        print("| erro encontrado. não há alunos presentes")
        time.sleep(4)
        return

   listaAluno()
   try:
      id_deletar = int(input("| digite o ID do aluno: "))
   except ValueError:#se nao for int vai dar erro
      print("| digite um ID válido")
      time.sleep(3)
      return
#cursor.execute executa o comando entre () no mysql
   try:
      cursor.execute("DELETE FROM alunos WHERE id_aluno = %s",(id_deletar,))#DELETA da tabela alunos ONDE id do aluno = id_deletar
      conn.commit()

      if cursor.rowcount > 0:
         print("| aluno deletado")
         time.sleep(3)
         return
      else:
         print("| nenhum aluno com esse ID")
         time.sleep(3)
         return
   except Error as e:#vai pegar erros especificamente do mysql
      print(f"| erro ao deletar aluno: {e}")
      time.sleep(5)
      return
   finally:#se entrar tanto no try, tanto no except, ele vai passar pelo finally
      cursor.close()
      conn.close()

def deletarProfessor():
   conn = conectar()
   cursor = conn.cursor()
#pega a conexão com o banco e chama o cursor
   cursor.execute("SELECT COUNT(*) FROM professores")
   total_profs = cursor.fetchone()[0]

   if total_profs == 0:
        print("| erro encontrado. não há professores presentes")
        time.sleep(4)
        return

   listaProf()
   try:#o try tenta o valor int, se não for, entra no except
      id_deletar = int(input("| digite o ID do professor: "))
   except ValueError:
      print("| digite um ID válido")
      time.sleep(3)
      return

   try:
      cursor.execute("DELETE FROM professores WHERE id_professor = %s",(id_deletar,))#DELETA da tabela professores ONDE id do professor = id_deletar
      conn.commit()

      if cursor.rowcount > 0:#rowcount conta quantas linhas foram alteradas
         print("| professor deletado")
         time.sleep(3)
         return
      else:
         print("| nenhum professor com esse ID")
         time.sleep(3)
         return
   except Error as e:
      print(f"| erro ao deletar professor: {e}")
      time.sleep(5)
      return
   finally:
      cursor.close()
      conn.close()

def deletarNota():
   conn = conectar()
   cursor = conn.cursor()

   cursor.execute("SELECT COUNT(*) FROM notas")#vai contar a quantas notas tem
   total_notas = cursor.fetchone()[0]

   if total_notas == 0:
        print("| erro encontrado. não há notas cadastradas")
        time.sleep(4)
        return

   listaNotas()
   try:
      id_deletar = int(input("digite o ID da nota: "))
   except ValueError:
      print("| digite um ID válido")
      time.sleep(3)
      return

   try:
      cursor.execute("DELETE FROM notas WHERE id_nota = %s",(id_deletar,))
      conn.commit()

      if cursor.rowcount > 0:
         print("| nota deletada")
         time.sleep(3)
         return
      else:
         print("| nenhuma nota com esse ID")
         time.sleep(3)
         return
   except Error as e:
      print(f"| erro ao deletar nota: {e}")
      time.sleep(5)
      return
   finally:
      cursor.close()
      conn.close()
