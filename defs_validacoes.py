import time

def validation(nome,idade,id_curso):
    if nome.strip() == "":
        print("erro encontrado (1)")
        time.sleep(3)
        return False
    try:
        idade = int(idade)

    except ValueError:
        print("erro encontrado (idadeT)")
        time.sleep(3)
        return False
        

    if idade >= 21:
        print("erro encontrado (idade)")
        time.sleep(3)
        return False
    
    if id_curso.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False


    if not nome.replace(" ", "").isalpha():
        print("erro encontrado (4)")
        time.sleep(3)
        return False
    
    if not id_curso.isdigit():
       print("erro encontrado (5)")
       time.sleep(3)
       return False
    
    return True
 
def validarProf(professor, idadeP, materia, cursoP):
  
    if professor.strip() == "":
       print("erro encontrado (1)")
       time.sleep(3)
       return
    
    try:
        idadeP = int(idadeP)

    except ValueError:
        print("erro encontrado (idadeT)")
        time.sleep(3)
        return False
    
    if idadeP <= 21:
        print("erro encontrado (idade)")
        time.sleep(3)
        return False
 
    if cursoP.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False 
    
    
    if materia.strip() == "":
       print("erro encontrado (4)")
       time.sleep(3)
       return False
    
    if not professor.replace(" ", "").isalpha():
        print("erro encontrado (5)")
        time.sleep(3)
        return False

    if not materia.replace(" ", "").isalpha():
        print("erro encontrado (6)")
        time.sleep(3)
        return False

    if not cursoP.replace(" ", "").isalpha():
        print("erro encontrado (7)")
        time.sleep(3)
        return False
    

    return True
