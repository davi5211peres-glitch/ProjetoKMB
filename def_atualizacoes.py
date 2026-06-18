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
        print("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝚄𝙼 𝙸𝙳 𝚅𝙰𝙻𝙸𝙳𝙾")
        time.sleep(2)
        return
    
    novo_nome = input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙾 𝙽𝙾𝚅𝙾 𝙽𝙾𝙼𝙴 (vazio para não alterar): ")
    nova_idade = input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙰 𝙽𝙾𝚅𝙰 𝙸𝙳𝙰𝙳𝙴 (vazio para não alterar): ")
    listaCursos()
    try:
        novo_curso = int(input("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝙾 𝙸𝙳 𝙳𝙾 𝙽𝙾𝚅𝙾 𝙲𝚄𝚁𝚂𝙾 (vazio para não alterar): "))
    except ValueError:
        print("| 𝙳𝙸𝙶𝙸𝚃𝙴 𝚄𝙼 𝙸𝙳 𝚅𝙰𝙻𝙸𝙳𝙾")
        time.sleep(2)
        return

    if novo_nome:
        cursor.execute("UPDATE alunos SET nome = %s WHERE id_aluno = %s ", (novo_nome, id_busca))

    if nova_idade:
        cursor.execute("UPDATE alunos SET idade = %s WHERE id_aluno = %s", (nova_idade, id_busca))

    if novo_curso:
        cursor.execute("UPDATE alunos SET fk_idcurso = %s WHERE id_aluno = %s", (novo_curso, id_busca))

    conn.commit()
    print("\n| 𝙰𝙻𝚄𝙽𝙾 𝙰𝚃𝚄𝙰𝙻𝙸𝚉𝙰𝙳𝙾 𝙲𝙾𝙼 𝚂𝚄𝙲𝙴𝚂𝚂𝙾")
    time.sleep(2)
    cursor.close()
    conn.close()
    return