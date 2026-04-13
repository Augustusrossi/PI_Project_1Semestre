# PI_Project_1Semestre
---

## Descrição do projeto:
Sistema de gerenciamento de consultas

#codigo em py para requerimento do paciente especifico, pesquisa por nome do paciente

import mysql.connector

conexao = mysql.connector.connect(
    host="172.16.12.14",
    user="BD240226161",
    password="Kpwza7",
    database="BD240226161"
)

cursor = conexao.cursor()


nome = input("Digite o nome do paciente: ")


query = """
SELECT p.nome, r.descricao
FROM requerimentos r
JOIN Paciente p ON r.id_paciente = p.id_paciente
WHERE p.nome LIKE %s
"""

cursor.execute(query, (f"%{nome}%",))


for linha in cursor.fetchall():
    print("Paciente:", linha[0])
    print("Requerimento:", linha[1])
    print("-----")


cursor.close()
conexao.close()

#Lembrar de mudar os dados de conexao do Banco para o seu pessoal 
