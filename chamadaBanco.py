#biblioteca de conexao com o banco !DOCUMENTAR
import mysql.connector


def obtem_conexao (servidor, usuario, senha, bd):
    if obtem_conexao.conexao == None:
        obtem_conexao.conexao = mysql.connector.connect( 
            host=f"{servidor}",\
            user=f"{usuario}",\
            password=f"{senha}",\
            database=f"{bd}"
        )
    return obtem_conexao.conexao

obtem_conexao.conexao = None
