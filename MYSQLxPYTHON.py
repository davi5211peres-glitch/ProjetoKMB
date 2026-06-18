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
    CREATE TABLE IF NOT EXISTS cursos(
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        curso VARCHAR(100) NOT NULL
               
        
    )
""")



cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        fk_idcurso INT NOT NULL,
               
        FOREIGN KEY (fk_idcurso)
            REFERENCES cursos(id_curso)
            ON DELETE CASCADE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores(
        id_professor INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        curso VARCHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas(
        id_nota INT AUTO_INCREMENT PRIMARY KEY,
        nota float NOT NULL,
        materia VARCHAR(50) NOT NULL,
        fk_idaluno INT NOT NULL,

        FOREIGN KEY (fk_idaluno) 
            REFERENCES alunos(id_aluno)
            ON DELETE CASCADE
    )
""")

cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Desenvolvimento de Sistemas');")
cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Multimídia');")
cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Jogos Digitais');")

conn.commit()
