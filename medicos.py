import imports

def nome(): 
    
    while True:
        nome_completo = input("Digite o nome do médico a ser cadastrado: ").strip()
        nome_completo_partes = nome_completo.split()
        
        #verifica se cada parte contém um carácter que não se enquandra no nome completo de alguém
        contador = 0
        nome_valido = True
        while contador < len(nome_completo_partes):
            if not nome_completo_partes[contador].isalpha():
                nome_valido = False
                break
            contador += 1

        if nome_valido:
            if len(nome_completo_partes) == 1:
                nome = nome_completo_partes[0]
                sobrenome = ""
            else:
                nome = nome_completo_partes[0]
                #join -> juntar elementos de uma lista em uma string
                sobrenome = " ".join(nome_completo_partes[1:])
                print("Nome do médico cadastrado com sucesso\n")
            return nome + " " + sobrenome
        else:
            print("Entrada inválida! Digite apenas letras.")

    
    
def email():
    while True:
        email = input("Digite o email do médico: ")
        
        if ("@" in email) and (".com" in email) and (" " not in email):
            return email
        
        print("\nEmail inválido!\nDigite o email contendo os seguintes carácteres: '@', '.com' e sem espaços em branco.")            
            

def funcao():
    funcao = input("Insira a função do médico a ser cadastrado: ")
    return funcao
        

def crm():
    crm = input("Insira o CRM do médico a ser cadastrado: ")
    return crm
        

def cadastrar_medicos():
    print("\n" + "─"*45)
    print(f"{'NOVO CADASTRO DE MÉDICO':^45}")
    print("─"*45 + "\n")
    comando=f"insert into medico (crm, nome, email, funcao) values ('{crm()}','{nome()}','{email()}', '{funcao()}')"
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Medico cadastrado com sucesso!")
    
    

def listar_medicos():
    print("\n" + "─"*45)
    print(f"{'CORPO CLÍNICO CADASTRADO':^45}")
    print("─"*45 + "\n")
    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    comando = f"SELECT * FROM medico"
    cursor.execute(comando)
    medicos = cursor.fetchall()

    print("\n=== LISTA DE MÉDICOS ===")
    
    print("-" * 110)
    print(f"{'ID':<5}| {'CRM':<20}| {'Nome':<30}| {'Email':<35}| {'Função':<15}")
    print("-" * 110)
    
    contador = 0
    while contador < len(medicos):
        print(
            f"{medicos[contador][0]:<5}| "
            f"{medicos[contador][1]:<20}| "
            f"{medicos[contador][2]:<30}| "
            f"{medicos[contador][3]:<35}| "
            f"{medicos[contador][4]:<15}"
        )
        contador += 1

        contador+=1
        
    return medicos


def buscar_medico(id_medico):
    print("\n" + "─"*45)
    print(f"{'CONSULTA DE CADASTRO MÉDICO':^45}")
    print("─"*45 + "\n")
    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM medico")
    linhas_medico = cursor.fetchall() 
            
    id_medicos_validos = []
    contador = 0;
    
    while contador < len(linhas_medico):
        id_medicos_validos.append(linhas_medico[contador][0])
        contador += 1
        
    
    if id_medico == None:
        while True:
            try:
                id_med = int(input("\nDigite o id do médico para busca-lo: "))
            except ValueError:
                print("\nValor inválido, apenas números são aceitos. \nDigite novamente, por favor!")
                continue
            else:
                
                if(id_med not in id_medicos_validos):
                    print("\nMédico não existente para esse valor de identificação (id_medico)!\n")

                    continue
                
                conexao = imports.chamadaBanco.obtem_conexao()
                cursor = conexao.cursor()
                comando = f"SELECT * FROM medico WHERE id_medico = {id_med}"

                cursor.execute(comando)
                medico = cursor.fetchall()

                return medico[0]
            
    else:
        if(id_medico not in id_medicos_validos):
            print("\nMédico não existente para esse valor de identificação (id_medico)!\n")

            return None
        
        conexao = imports.chamadaBanco.obtem_conexao()
        cursor = conexao.cursor()
        comando = f"SELECT * FROM medico WHERE id_medico = {id_medico}"

        cursor.execute(comando)
        medico = cursor.fetchall()

        return medico[0]

