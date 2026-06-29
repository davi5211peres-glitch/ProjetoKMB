import mysql.connector
from mysql.connector import Error
#importa
conn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
)
#conexão inicial com mysql
cursor = conn.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS escola;
    """)

cursor.execute("USE escola")



def conectar():
#def é definição da função
    try:
        conexão = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
            database = "escola",
        )
        return conexão
    except Error as e:
        print(f"| Erro ao conectar ao MySQL:{e}")
        return None


cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos(
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        curso VARCHAR(100) NOT NULL UNIQUE
    )
""")
#executando o comando que cria uma tabela de cursos

cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias (
        id_materia INT AUTO_INCREMENT PRIMARY KEY,
        materia VARCHAR(100) NOT NULL UNIQUE           
    )
""")
#de materias

cursor.execute("""
    CREATE TABLE IF NOT EXISTS turmas (
        id_turma INT AUTO_INCREMENT PRIMARY KEY,
        turma VARCHAR(50) NOT NULL UNIQUE
    )
""")
#de turmas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id_aluno INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        fk_idcurso INT NOT NULL,
        fk_idturma INT NOT NULL,
               
        FOREIGN KEY (fk_idcurso)
            REFERENCES cursos(id_curso)
            ON DELETE CASCADE

        FOREIGN KEY (fk_idturma)
            REFERENCES turmas(id_turma)
            ON DELETE CASCADE
    )
""")
#ela pega os dados de uma tabela de fora, nesse caso ela ta pegando um dado da tabela de cursos, que é o id curso

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
        nota DECIMAL(4,2) NOT NULL,
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

cursor.execute("INSERT IGNORE INTO turmas (turma) VALUES ('Primeiro Ano');")
cursor.execute("INSERT IGNORE INTO turmas (turma) VALUES ('Segundo Ano');")
cursor.execute("INSERT IGNORE INTO turmas (turma) VALUES ('Terceiro Ano');")

cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Artes')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Algoritimos')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Biologia')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Banco de Dados')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Filosofia')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Física')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Geografia')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('História')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Matemática')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Química')")
cursor.execute("INSERT IGNORE INTO materias (materia) VALUES ('Sociologia')")

conn.commit()
