import mysql.connector
from mysql.connector import Error

    
conn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
)

cursor = conn.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS escola;
    """)

cursor.execute("USE escola")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        curso VARCHAR(50) NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id_professor INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        materia VARCHAR(50) NOT NULL,
        curso VARCHAR(200) NOT NULL
    );
""")

def conectar():
    try:
        conexão = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
            database = "escola",
        )
        return conexão
    except Error as e:
        print(f"Erro ao conectar ao MySQL:{e}")
        return None
    
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas(
        id_notas INT AUTO_INCREMENT PRIMARY KEY,
        notas float NOT NULL,
        materia VARCHAR(50) NOT NULL,
        fk_idaluno INT NOT NULL,
        fk_idprofessor INT NOT NULL,
        
        FOREIGN KEY (fk_idaluno) 
            REFERENCES alunos(id_aluno)
            ON DELETE CASCADE, 
        
        FOREIGN KEY (fk_idprofessor) 
            REFERENCES professores(id_professor)
            ON DELETE CASCADE
    );
""")