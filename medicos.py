import mysql.connector


# CONEXÃO

def conectar():
    return mysql.connector.connect(
        host="172.16.12.14",
        user="BD240226161",
        password="Kpwza7",
        database="BD240226161",
        port=3306
    )

# PRIORIDADE

def calcular_prioridade(dor, tempo, desconforto):
    p = ((dor*5)+(tempo*3)+(desconforto*2))/10

    if p < 5:
        return "baixa"
    elif p <= 7:
        return "urgente"
    else:
        return "critico"

# CADASTRAR PACIENTE

def cadastrar_paciente():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        nome = input("Nome do paciente: ")
        rg = input("RG: ")
        descricao = input("Descrição inicial: ")

        query = """
        INSERT INTO paciente (nome, rg, descricao)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (nome, rg, descricao))
        conexao.commit()

        id_paciente = cursor.lastrowid

        print(f" Paciente cadastrado com ID: {id_paciente}\n")

        cursor.close()
        conexao.close()

        return id_paciente

    except Exception as e:
        print(" Erro ao cadastrar paciente:", e)
        return None

# TRIAGEM

def triagem():
    try:
        sintomas = input("Sintomas: ")
        dor = int(input("Dor (1-10): "))
        desconforto = int(input("Desconforto (1-5): "))
        tempo = int(input("Tempo dos sintomas (dias)"))
        return sintomas, dor, desconforto, tempo
    except:
        print(" Erro: Entrada inválida!")
        return triagem()

# VALIDAR MÉDICO

def validar_medico(crm):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT crm, nome FROM medico WHERE crm = %s", (crm,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

# LISTAR MÉDICOS

def listar_medicos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT crm, nome, funcao FROM medico")
    medicos = cursor.fetchall()

    print("\n=== MÉDICOS DISPONÍVEIS ===")
    for m in medicos:
        print(f"{m[0]} - {m[1]} ({m[2]})")

    cursor.close()
    conexao.close()

# CRIAR REQUERIMENTO

def criar_requerimento(id_paciente):
    try:
        if not id_paciente:
            print("Paciente inválido!")
            return

        listar_medicos()

        crm = int(input("CRM do médico: "))
        medico = validar_medico(crm)

        if not medico:
            print(" Médico não encontrado!\n")
            return

        print(f" Médico selecionado: {medico[1]}")

        sintomas, dor, desconforto, tempo = triagem()
        prioridade = calcular_prioridade(dor, tempo, desconforto)

        descricao = f"{sintomas} | Dor:{dor} | Desconforto:{desconforto} | Tempo:{tempo}"

        conexao = conectar()
        cursor = conexao.cursor()

        query = """
        INSERT INTO requerimentos 
        (id_medico, id_paciente, descricao, status, prioridade)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (crm, id_paciente, descricao, "aguardando", prioridade))
        conexao.commit()

        print(" Requerimento criado com sucesso!\n")

        cursor.close()
        conexao.close()

    except Exception as e:
        print(" Erro ao criar requerimento:", e)

# BUSCA GLOBAL

def busca_global():
    conexao = conectar()
    cursor = conexao.cursor()

    termo = input("Buscar (CRM / médico / paciente): ")
    termo_like = f"%{termo}%"

    query = """
    SELECT 
        m.crm,
        m.nome,
        p.nome,
        r.status,
        r.prioridade,
        r.descricao
    FROM medico m
    LEFT JOIN requerimentos r ON m.crm = r.id_medico
    LEFT JOIN paciente p ON p.id_paciente = r.id_paciente
    WHERE 
        m.nome LIKE %s OR
        COALESCE(p.nome, '') LIKE %s OR
        CAST(m.crm AS CHAR) LIKE %s
    """

    cursor.execute(query, (termo_like, termo_like, termo_like))
    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum resultado\n")
        return

    print("\n===== RESULTADOS =====")
    for r in resultados:
        print(f"""
Médico: {r[1]} (CRM {r[0]})
Paciente: {r[2] if r[2] else '---'}
Status: {r[3] if r[3] else 'sem atendimento'}
Prioridade: {r[4] if r[4] else '---'}
Descrição: {r[5] if r[5] else '---'}
---------------------------
""")

    cursor.close()
    conexao.close()

# BUSCAR MÉDICO

def buscar_medico():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome do médico: ")
    termo = f"%{nome}%"

    cursor.execute("SELECT crm, nome, funcao FROM medico WHERE nome LIKE %s", (termo,))
    resultados = cursor.fetchall()

    if not resultados:
        print(" Nenhum médico encontrado\n")
        return

    for m in resultados:
        print(f"{m[0]} - {m[1]} ({m[2]})")

    cursor.close()
    conexao.close()

# BUSCAR POR CRM

def buscar_medico_crm():
    try:
        crm = int(input("CRM: "))
    except:
        print(" CRM inválido")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT crm, nome, funcao FROM medico WHERE crm = %s", (crm,))
    m = cursor.fetchone()

    if not m:
        print(" Médico não encontrado\n")
        return

    print(f"{m[0]} - {m[1]} ({m[2]})\n")

    cursor.close()
    conexao.close()

# ATENDIMENTO

def iniciar_atendimento():
    id_req = int(input("ID do requerimento: "))
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("UPDATE requerimentos SET status='em atendimento' WHERE id_requerimento=%s", (id_req,))
    conexao.commit()

    print("Atendimento iniciado!\n")

def finalizar_atendimento():
    id_req = int(input("ID do requerimento: "))
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("UPDATE requerimentos SET status='finalizada' WHERE id_requerimento=%s", (id_req,))
    conexao.commit()

    print("Atendimento finalizado!\n")

# MENU

def menu():
    while True:
        print("""
1 - Cadastrar paciente + triagem
2 - Buscar atendimentos
3 - Buscar médico (nome)
4 - Buscar médico (CRM)
5 - Iniciar atendimento
6 - Finalizar atendimento
0 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            id_paciente = cadastrar_paciente()
            criar_requerimento(id_paciente)

        elif op == "2":
            busca_global()

        elif op == "3":
            buscar_medico()

        elif op == "4":
            buscar_medico_crm()

        elif op == "5":
            iniciar_atendimento()

        elif op == "6":
            finalizar_atendimento()

        elif op == "0":
            break

        else:
            print("Opção inválida\n")

menu()