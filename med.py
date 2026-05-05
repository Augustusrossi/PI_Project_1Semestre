import mysql.connector

# =========================
# CONEXÃO
# =========================


def conectar():
    return mysql.connector.connect(
        host="172.16.12.14",
        user="BD240226161",
        password="Kpwza7",
        database="BD240226161",
        port=3306
    )

# =========================
# "BANCO" EM MEMÓRIA
# =========================

pacientes = []
requerimentos = []

medicos = [
    {"crm": 101, "nome": "Dr João"},
    {"crm": 102, "nome": "Dra Ana"},
    {"crm": 103, "nome": "Dr Carlos"},
]


# =========================
# PRIORIDADE
# =========================

def calcular_prioridade(dor, tempo, desconforto):
    p = ((dor*5)+(tempo*3)+(desconforto*2))/10

    if p < 5:
        return "baixa"
    elif p <= 7:
        return "urgente"
    else:
        return "critico"


# =========================
# TRIAGEM COMPLETA
# =========================

def triagem():
    sintomas = input("Descreva o que o paciente está sentindo: ")

    while True:
        try:
            dor = int(input("Nível de dor (1-10): "))
            if 1 <= dor <= 10:
                break
        except:
            pass
        print("Valor inválido")

    while True:
        try:
            desconforto = int(input("Nível de desconforto (1-5): "))
            if 1 <= desconforto <= 5:
                break
        except:
            pass
        print("Valor inválido")

    print("""
Tempo de sintomas:
1 - Menos de 1 semana
2 - 1 a 2 semanas
3 - 2 a 3 semanas
4 - 3 a 4 semanas
5 - Mais de 5 semanas
""")

    while True:
        try:
            tempo = int(input("Escolha: "))
            if 1 <= tempo <= 5:
                break
        except:
            pass
        print("Valor inválido")

    textos = [
        "menos de 1 semana",
        "1 a 2 semanas",
        "2 a 3 semanas",
        "3 a 4 semanas",
        "mais de 5 semanas"
    ]

    return sintomas, dor, desconforto, tempo, textos[tempo-1]


# =========================
# CADASTRO + TRIAGEM
# =========================

def cadastrar_paciente():
    nome = input("Nome do paciente: ")

    paciente = {
        "id": len(pacientes) + 1,
        "nome": nome
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado!\n")

    criar_requerimento_com_paciente(paciente["id"])


def criar_requerimento_com_paciente(id_paciente):
    print("\n=== SELECIONE O MÉDICO ===")
    for m in medicos:
        print(f"{m['crm']} - {m['nome']}")

    try:
        crm = int(input("CRM do médico: "))
    except:
        print("CRM inválido")
        return

    medico = next((m for m in medicos if m["crm"] == crm), None)

    if not medico:
        print("Médico não encontrado")
        return

    paciente = next((p for p in pacientes if p["id"] == id_paciente), None)

    sintomas, dor, desconforto, tempo, tempo_texto = triagem()

    prioridade = calcular_prioridade(dor, tempo, desconforto)

    descricao = f"{sintomas} | Dor: {dor} | Desconforto: {desconforto} | Tempo: {tempo_texto}"

    req = {
        "id": len(requerimentos) + 1,
        "crm": medico["crm"],
        "medico": medico["nome"],
        "paciente": paciente["nome"],
        "status": "aberto",
        "prioridade": prioridade,
        "descricao": descricao
    }

    requerimentos.append(req)

    print("\nRequerimento criado com sucesso!\n")


# =========================
# BUSCAS
# =========================

def buscar_por_crm():
    crm = int(input("CRM do médico: "))
    resultados = [r for r in requerimentos if r["crm"] == crm]
    mostrar(resultados)


def buscar_por_nome_medico():
    nome = input("Nome do médico: ").lower()
    resultados = [r for r in requerimentos if nome in r["medico"].lower()]
    mostrar(resultados)


def buscar_por_nome_paciente():
    nome = input("Nome do paciente: ").lower()
    resultados = [r for r in requerimentos if nome in r["paciente"].lower()]
    mostrar(resultados)


def mostrar(lista):
    if not lista:
        print("\nNenhum resultado\n")
        return

    print("\n===== RESULTADOS =====\n")

    for r in lista:
        print(f"""
Médico: {r['medico']} (CRM {r['crm']})
Paciente: {r['paciente']}
Status: {r['status']}
Prioridade: {r['prioridade']}
Descrição: {r['descricao']}
---------------------------
""")


# =========================
# MENU
# =========================

def menu():
    while True:
        print("""
===== SISTEMA =====

1 - Cadastrar paciente + triagem
2 - Buscar por CRM do médico
3 - Buscar por nome do médico
4 - Buscar por nome do paciente
0 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_paciente()
        elif op == "2":
            buscar_por_crm()
        elif op == "3":
            buscar_por_nome_medico()
        elif op == "4":
            buscar_por_nome_paciente()
        elif op == "0":
            break
        else:
            print("Opção inválida")


menu()