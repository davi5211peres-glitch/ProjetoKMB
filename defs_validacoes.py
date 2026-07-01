import time
from MYSQLxPYTHON import conectar

def validation(nome,idade,id_curso,id_turma):
    """valida dados do aluno"""

    if nome.strip() == "":
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False
    try:
        idade = int(idade)

    except ValueError:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False


    if idade <= 0:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False

    if idade >= 22:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if id_curso.strip() == "":
       print("| erro encontrado (curso)")
       time.sleep(3)
       return False


    if not nome.replace(" ", "").isalpha():
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False
    
    if not id_curso.isdigit():
       print("| erro encontrado (curso)")
       time.sleep(3)
       return False
    
    return True
 
def validarProf(professor, idadeP, id_materia):
  
    if professor.strip() == "":
       print("| erro encontrado (nome)")
       time.sleep(3)
       return
    
    try:
        idadeP = int(idadeP)
    except ValueError:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if idadeP <= 21:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if idadeP >= 100:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False

    if id_materia.strip() == "":
        print("| erro encontrado (materia)")
        time.sleep(3)
        return False

    if not professor.replace(" ", "").isalpha():
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False

    if not id_materia.isdigit():
        print("| erro encontrado (materia)")
        time.sleep(3)
        return False


    return True
