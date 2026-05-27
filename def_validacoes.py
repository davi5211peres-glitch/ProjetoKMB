import time

def validation(nome,idade,curso):
    if nome.strip() == "":
        print("erro encontrado (1)")
        time.sleep(3)
        return False
    
    if curso.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False
    
    if not idade.isdigit():
        print("erro encontrado (3)")
        time.sleep(3)
        return False

    if not nome.replace(" ", "").isalpha():
        print("erro encontrado (4)")
        time.sleep(3)
        return False
    
    if not curso.replace(" ", "").isalpha():
       print("erro encontrado (5)")
       time.sleep(3)
       return False
    
    return True
 
def validarProf(professor, turmaP, idadeP, materia):
  
    if professor.strip() == "":
       print("erro encontrado (1)")
       time.sleep(3)
       return
 
    if turmaP.strip() == "":
       print("erro encontrado (2)")
       time.sleep(3)
       return False 
    
    if idadeP.strip() == "":
       print("erro encontrado (3)")
       time.sleep(3)
       return False
    
    if materia.strip() == "":
       print("erro encontrado (4)")
       time.sleep(3)
       return False
    
    if not professor.isalpha():
        print("erro encontrado (5)")
        time.sleep(3)
        return False

    if not materia.isalpha():
        print("erro encontrado (6)")
        time.sleep(3)
        return False

    if not turmaP.isdigit() or not idadeP.isdigit():
        print("erro encontrado (7)")
        time.sleep(3)
        return False
    return True
