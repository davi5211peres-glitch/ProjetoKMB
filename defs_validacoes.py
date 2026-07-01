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
    
    if id_turma.strip() == "":
        print("| erro encontrado (turma)")
        time.sleep(3)
        return False
    
    if not id_turma.isdigit():
       print("| erro encontrado (turma)")
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

def validation2(novo_nome,nova_idade,novo_curso,nova_turma):

    if novo_nome.strip() == "":
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False
    try:
        nova_idade = int(nova_idade)

    except ValueError:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False


    if nova_idade <= 0:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False

    if nova_idade >= 22:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if novo_curso.strip() == "":
       print("| erro encontrado (curso)")
       time.sleep(3)
       return False


    if not novo_nome.replace(" ", "").isalpha():
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False
    
    if not novo_curso.isdigit():
       print("| erro encontrado (curso)")
       time.sleep(3)
       return False
    
    if nova_turma.strip() == "":
        print("| erro encontrado (turma)")
        time.sleep(3)
        return False
    
    if not nova_turma.isdigit():
       print("| erro encontrado (turma)")
       time.sleep(3)
       return False
    
    return True

def validarProf2(novo_prof, nova_idadeP, nova_materia):
  
    if novo_prof.strip() == "":
       print("| erro encontrado (nome)")
       time.sleep(3)
       return
    
    try:
        nova_idadeP = int(nova_idadeP)
    except ValueError:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if nova_idadeP <= 21:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if nova_idadeP >= 100:
        print("| erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if nova_materia.strip() == "":
        print("| erro encontrado (materia)")
        time.sleep(3)
        return False

    if not novo_prof.replace(" ", "").isalpha():
        print("| erro encontrado (nome)")
        time.sleep(3)
        return False

    try:
        nova_materia = int(nova_materia)
    except ValueError:
        print("| erro encontrado (materia)")
        time.sleep(3)
        return False

    return True