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

    cursor.execute("SELECT COUNT(*) FROM alunos")
    total_alunos = cursor.fetchone()[0]

    if total_alunos == 0:
        print("| erro encontrado. não há alunos presentes")
        time.sleep(4)
        return

    listaAluno()
    try:
        id_busca = int(input("| Digite o ID do aluno que deseja mudar: "))
    except ValueError:
        print("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝚄𝙼 𝙸𝙳 𝚅𝙰𝙻𝙸𝙳𝙾")
        time.sleep(2)
        return
    
    novo_nome = input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙾 𝙽𝙾𝚅𝙾 𝙽𝙾𝙼𝙴 (vazio para não alterar): ")
    nova_idade = input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙰 𝙽𝙾𝚅𝙰 𝙸𝙳𝙰𝙳𝙴 (vazio para não alterar): ")
    listaCursos()
    novo_curso = input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙾 𝙸𝙳 𝙳𝙾 𝙽𝙾𝚅𝙾 𝙲𝚄𝚁𝚂𝙾 (vazio para não alterar): ")


    if novo_nome:
        cursor.execute("UPDATE alunos SET nome = %s WHERE id_aluno = %s ", (novo_nome, id_busca))

    if nova_idade:
        cursor.execute("UPDATE alunos SET idade = %s WHERE id_aluno = %s", (nova_idade, id_busca))

    if novo_curso:
        try:
            novo_curso = int(novo_curso)
        except ValueError:
            print("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝚄𝙼 𝙸𝙳 𝚅𝙰𝙻𝙸𝙳𝙾")
            time.sleep(2)
            return
        cursor.execute("UPDATE alunos SET fk_idcurso = %s WHERE id_aluno = %s", (novo_curso, id_busca))

    conn.commit()
    print("\n| 𝙰𝙻𝚄𝙽𝙾 𝙰𝚃𝚄𝙰𝙻𝙸𝚉𝙰𝙳𝙾 𝙲𝙾𝙼 𝚂𝚄𝙲𝙴𝚂𝚂𝙾")
    time.sleep(2)
    cursor.close()
    conn.close()
    return

def mudarProf():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM professores")
    total_profs = cursor.fetchone()[0]

    if total_profs == 0:
        print("| erro encontrado. não há professores presentes")
        time.sleep(4)
        return


    listaProf()
    try:
        id_buscaP = int(input("| Digite o ID do professor que deseja mudar: "))
    except ValueError:
        print("| Digite um ID válido")
        time.sleep(2)
        return
    
    novo_nome = input("| Digite o novo nome (vazio para não alterar): ")
    nova_idade = input("| Digite a nova idade (vazio para não alterar): ")
    listaMaterias()
    id_buscaM = input("| Digite o ID da matéria (vazio para não alterar): ")
    
    if novo_nome:
        cursor.execute("UPDATE professores SET nome = %s WHERE id_professor = %s", (novo_nome, id_buscaP))

    if nova_idade:
        cursor.execute("UPDATE professores SET idade = %s WHERE id_professor = %s", (nova_idade, id_buscaP))

    if id_buscaM:
        try:
            id_buscaM = int(id_buscaM)
        except ValueError:
            print("| Digite um ID válido")
            time.sleep(2)
            return
        cursor.execute("UPDATE professores SET fk_idmateria = %s WHERE id_professor = %s", (id_buscaM, id_buscaP))

    conn.commit()
    print("\n| professor atualizado com sucesso")
    time.sleep(2)
    cursor.close()
    conn.close()
    return

def mudarNota():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM notas")
    total_notas = cursor.fetchone()[0]

    if total_notas == 0:
        print("| erro encontrado. não há notas cadastradas")
        time.sleep(4)
        return

    listaNotas()
    try:
        id_buscaN = int(input("| Digite o ID da nota: "))
    except ValueError:
        print("| Digite um ID válido")
        time.sleep(2)
        return
    
    nova_nota = input("| Digite a nova nota (ex: 8.5)(vazio para não alterar): ")

    listaMaterias()

    id_buscaM = input("| Digite o ID da matéria (vazio para não alterar): ")
    
    if nova_nota:
        try:
            nova_nota = float(nova_nota)
        except ValueError:
            print("| Digite uma nota válida")
            time.sleep(2)
            return
        cursor.execute("UPDATE notas SET nota = %s WHERE id_nota = %s", (nova_nota, id_buscaN))
    
    if id_buscaM:
        try:
            id_buscaM = int(id_buscaM)
        except ValueError:
            print("| Digite um ID válido")
            time.sleep(2)
            return
        cursor.execute("UPDATE notas SET fk_idmateria = %s WHERE id_nota = %s", (id_buscaM, id_buscaN))

    conn.commit()
    print("| nota atualizada com sucesso")
    cursor.close()
    conn.close()
    return
