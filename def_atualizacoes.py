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