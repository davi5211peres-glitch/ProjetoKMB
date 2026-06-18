import time
import mysql.connector
from mysql.connector import Error
from MYSQLxPYTHON import *
from def_loading import *
from defs_validacoes import *
from defs_listagens import *

def mudarAluno():
    conn = conectar()
    cursor = conn.cursor()

    listaAluno()
    try:
        id_busca = int(input("Digite o ID do aluno que deseja mudar: "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    novo_nome = input("digite o novo nome (vazio para não alterar): ")
    nova_idade = input("digite a nova idade (vazio para não alterar): ")
    listaCursos()
    try:
        novo_curso = int(input("digite o ID do novo curso (vazio para não alterar): "))
    except ValueError:
        print("digite um ID válido")
        time.sleep(2)
        return

    if novo_nome:
        cursor.execute("UPDATE alunos SET nome = %s WHERE id_aluno = %s ", (novo_nome, id_busca))

    if nova_idade:
        cursor.execute("UPDATE alunos SET idade = %s WHERE id_aluno = %s", (nova_idade, id_busca))

    if novo_curso:
        cursor.execute("UPDATE alunos SET fk_idcurso = %s WHERE id_aluno = %s", (novo_curso, id_busca))

    conn.commit()
    print("\naluno atualizado com sucesso")
    time.sleep(2)
    cursor.close()
    conn.close()
    return

def mudarProf():
    conn = conectar()
    cursor = conn.cursor()

    listaProf()
    try:
        id_buscaP = int(input("Digite o ID do professor que deseja mudar: "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    novo_nome = input("Digite o novo nome (vazio para não alterar): ")
    nova_idade = input("Digite a nova idade (vazio para não alterar): ")
    listaMaterias()
    try:
        id_buscaM = int(input("Digite o ID da matéria (vazio para não alterar): "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    listaCursos()
    try:
        id_buscaC = int(input("Digite o ID da matéria (vazio para não alterar): "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    if novo_nome:
        cursor.execute("UPDATE professores SET nome = %s WHERE id_professor = %s", (novo_nome, id_buscaP))

    if nova_idade:
        cursor.execute("UPDATE professores SET idade = %s WHERE id_professor = %s", (nova_idade, id_buscaP))

    if id_buscaM:
        cursor.execute("UPDATE professores SET fk_idmateria = %s WHERE id_professor = %s", (id_buscaM, id_buscaP))

    if id_buscaC:
        cursor.execute("UPDATE professores SET fk_idcurso = %s WHERE id_professor = %s", (id_buscaC, id_buscaP))

    conn.commit()
    print("\nprofessor atualizado com sucesso")
    time.sleep(2)
    cursor.close()
    conn.close()
    return

def mudarNota():
    conn = conectar()
    cursor = conn.cursor()

    listaNotas()
    try:
        id_buscaN = int(input("Digite o ID da nota: "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    try:
        nova_nota = float(input("Digite a nova nota (ex: 8.5)(vazio para não alterar): "))
    except ValueError:
        print("Digite uma nota válida")
        time.sleep(2)
        return

    listaMaterias()
    try:
        id_buscaM = int(input("Digite o ID da matéria (vazio para não alterar): "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    if nova_nota:
        cursor.execute("UPDATE notas SET nota = %s WHERE id_nota = %s", (nova_nota, id_buscaN))
    
    if id_buscaM:
        cursor.execute("UPDATE notas SET fk_idmateria = %s WHERE id_nota = %s", (id_buscaM, id_buscaN))

    conn.commit()
    print("\nnota atualizada com sucesso")
    cursor.close()
    conn.close()
    return