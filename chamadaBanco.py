#biblioteca de conexao com o banco !DOCUMENTAR
import mysql.connector


def obtem_conexao ():
    if obtem_conexao.conexao == None:
        obtem_conexao.conexao = mysql.connector.connect( 
            host=f"{'127.0.0.1'}",\
            user=f"{'root'}",\
            password=f"{'123456'}",\
            database=f"{'sistemaHospital'}"
        )
    return obtem_conexao.conexao

obtem_conexao.conexao = None
