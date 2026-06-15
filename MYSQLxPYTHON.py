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
        curso VARCHAR(100) NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias (
        id_materia INT AUTO_INCREMENT PRIMARY KEY,
        materia VARCHAR(100) NOT NULL UNIQUE           
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
        fk_idmateria INT NOT NULL,
        fk_idcurso INT NOT NULL,
        
        FOREIGN KEY (fk_idmateria)
            REFERENCES materias(id_materia)
            ON DELETE CASCADE,
        
        FOREIGN KEY (fk_idcurso)
            REFERENCES cursos(id_curso)
            ON DELETE CASCADE
            
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas(
        id_nota INT AUTO_INCREMENT PRIMARY KEY,
        nota float NOT NULL,
        fk_idmateria INT NOT NULL,
        fk_idaluno INT NOT NULL,

        FOREIGN KEY (fk_idmateria)
            REFERENCES materias(id_materia)
            ON DELETE CASCADE,
        
        FOREIGN KEY (fk_idaluno) 
            REFERENCES alunos(id_aluno)
            ON DELETE CASCADE
               
    )
""")

cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Desenvolvimento de Sistemas');")
cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Multimídia');")
cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Jogos Digitais');")
cursor.execute("INSERT IGNORE INTO cursos (curso) VALUES ('Todos');")

cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Português')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Matemática')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('História')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Geografia')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Artes')")

conn.commit()