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

    lista()
    try:
        id_busca = int(input("Digite o ID do aluno que deseja mudar: "))
    except ValueError:
        print("Digite um ID válido")
        time.sleep(2)
        return
    
    novo_nome = input("digite o novo nome (vazio para não alterar): ")
    nova_idade = input("digite a nova idade (vazio para não alterar): ")

    if novo_nome:
        cursor.execute("UPDATE alunos SET nome = %s WHERE id_aluno = %s ", (novo_nome, id_busca))

    if nova_idade:
        cursor.execute("UPDATE alunos SET idade = %s WHERE id_aluno = %s", (nova_idade, id_busca))

    conn.commit()
    print("\naluno atualizado com sucesso")
    time.sleep(2)
    cursor.close()
    conn.close()
    return