import time

def validation(nome,idade,id_curso):
    if nome.strip() == "":
        print("erro encontrado (1)")
        time.sleep(3)
        return False
    
    if idade.strip() == "":
        print("erro encontrado (idade)")
        time.sleep(3)
        return False
    
    try:
        idade = int(idade)
    except ValueError:
        print("erro encontrado (idade)")

    if idade >= 21:
        print("erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if id_curso.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False
    

    if not nome.replace(" ", "").isalpha():
        print("erro encontrado (3)")
        time.sleep(3)
        return False
    
    if not id_curso.isdigit():
       print("erro encontrado (4)")
       time.sleep(3)
       return False
    
    return True
 
def validarProf(professor, idadeP, materia, id_cursoP):
  
    if professor.strip() == "":
       print("erro encontrado (1)")
       time.sleep(3)
       return
    
    if idadeP.strip() == "":
       print("erro encontrado (idade)")
       time.sleep(3)
       return False

    try:
        idadeP = int(idadeP)
    except ValueError:
        print("erro encontrado (idade)")

    if idadeP <= 21:
        print("erro encontrado (idade)")
        time.sleep(3)
        return False
 
    if id_cursoP.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False 
    
    
    if materia.strip() == "":
       print("erro encontrado (3)")
       time.sleep(3)
       return False
    
    if not professor.replace(" ", "").isalpha():
        print("erro encontrado (4)")
        time.sleep(3)
        return False

    if not materia.replace(" ", "").isalpha():
        print("erro encontrado (5)")
        time.sleep(3)
        return False

    if not id_cursoP.isdigit():
        print("erro encontrado (6)")
        time.sleep(3)
        return False
    
    return True