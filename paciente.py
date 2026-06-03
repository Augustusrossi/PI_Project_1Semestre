import imports

def nome(): 
    
    while True:
        
        #remove espaços iníciais e finais 
        nome_completo = input("Nome do paciente: ").strip()

        #divisão da string em partes
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
                print("Nome do paciente cadastrado com sucesso\n")

            else:
                nome = nome_completo_partes[0]
                #join -> juntar elementos de uma lista em uma string
                sobrenome = " ".join(nome_completo_partes[1:])
                print("Nome do paciente cadastrado com sucesso\n")
                
            return nome + " " + sobrenome
        else:
            print("Entrada inválida! Digite apenas letras.")
            continue    
        
def documento_rg():
    valor_verificado = False
    while valor_verificado == False:
        try: 
            rg = input("RG do paciente: ")
            if not rg.isdigit():
                print("Digite apenas números para o cadastro do RG do paciente")
                valor_verificado = False
        except ValueError:
            print("Digite apenas números para o cadastro do RG do paciente")
        else:
            if len(rg) >= 7 and len(rg) <=9:
                valor_verificado = True
                
                print("RG cadastrado com sucesso\n")
                return rg
            else:
                print("Quantidade de carácteres inválido: ")

def telefone_contato():
    valor_verificado = False
    while valor_verificado == False:
        try: 
            telefone_contato = input("Digite o telefone do paciente, para contato: ")
            if not telefone_contato.isdigit():
                print("Por favor, digite apenas números para indicação do contato")
  
        except ValueError:
            print("Por favor, digite apenas números para indicação do contato")
            valor_verificado = False
            
        else:
            if len(telefone_contato) == 11:
                valor_verificado = True
                
                print("Telefone cadastrado com sucesso\n")
                return telefone_contato
            else:
                print("Quantidade de carácteres inválido: ")


data_br = imports.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    
def insercao_paciente():
    print("\n" + "="*40)
    print(f"{'CADASTRO DE NOVO PACIENTE':^40}")
    print("="*40,'\n')
    comando=f"insert into paciente (nome, rg, telefone, data_cadastro) values ('{nome()}','{documento_rg()}', '{telefone_contato()}', '{data_br}')"
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Paciente cadastrado com sucesso")
    
    
def listar_pacientes():
    print("\n" + "="*50)
    print(f"{'PACIENTES CADASTRADOS NO SISTEMA':^50}")
    print("="*50,'\n')
    comando = f"select * from paciente"
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    
    atual = 0
    print("-" * 90)
    print(f"{'ID':<5}| {'Nome':<25}| {'RG':<12}| {'Telefone':<15}| {'Data de Cadastro':<25}")
    print("-" * 90)
    
    
    while atual<len(linhas):
        print(
            f"{linhas[atual][0]:<5}| "
            f"{linhas[atual][1]:<25}| "
            f"{linhas[atual][2]:<12}| "
            f"{linhas[atual][3]:<15}| "
            f"{linhas[atual][4]}"
        ) 
        atual+=1  
        
        
def procurar_paciente(id,posicao_info):
    comando = f"select id_paciente, nome, rg, telefone, DATE_FORMAT(data_cadastro, '%d/%m/%Y %H:%i:%s') as data_formatada from paciente where id_paciente = {id}"
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    
    #data = linhas[atual][4]
        
    if linhas == []: return False
    
    if posicao_info == None:
        return (linhas[0])
    else:
        return (linhas[0][posicao_info])
    
    

#listar histórico 
def listar_historico(id_paciente):
    print("\n" + "="*55)
    print(f"{'HISTÓRICO COMPLETO DO PACIENTE':^55}")
    print("="*55,'\n')
    comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE req.id_paciente = {id_paciente} order by data_hora_fechamento desc, data_hora_abertura"
    
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    
    atual = 0;
    print("-" * 180)
    print(f"{'Nome':<25}| "f"{'RG':<12}| "f"{'ID Req.':<8}| "f"{'ID Méd.':<8}| "f"{'ID Pac.':<8}| "f"{'Data Abertura':<20}| "f"{'Data Fechamento':<20}| "f"{'Status':<12}| "f"{'Prioridade':<12}")
    print("-" * 180)
    while atual < len(linhas):
        print(
            f"{linhas[atual][0]:<25}| "
            f"{linhas[atual][1]:<12}| "
            f"{linhas[atual][2]:<8}| "
            f"{str(linhas[atual][3]):<8}| "
            f"{linhas[atual][4]:<8}| "
            f"{str(linhas[atual][6]):<20}| "
            f"{str(linhas[atual][7]):<20}| "
            f"{linhas[atual][8]:<12}| "
            f"{linhas[atual][9]:<12}"
        )

        print(f"Descrição: {linhas[atual][5]}")
        print("-" * 180)
        atual += 1
        

def visualizar_status(id_requerimento):
    print("\n" + "="*45)
    print(f"{'STATUS ATUAL DO REQUERIMENTO':^45}")
    print("="*45,'\n') 
    comando = f"SELECT pac.nome, pac.rg, req.id_requerimento, req.status, req.prioridade FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente  WHERE id_requerimento = {id_requerimento}"

    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    
    atual = 0 
    print("-" * 90)
    print(f"{'Nome':<25}| "f"{'RG':<12}| "f"{'ID Req.':<10}| "f"{'Status':<15}| "f"{'Prioridade':<15}")
    print("-" * 90)
    while atual < len(linhas):
        print(
            f"{linhas[atual][0]:<25}| "
            f"{linhas[atual][1]:<12}| "
            f"{linhas[atual][2]:<10}| "
            f"{linhas[atual][3]:<15}| "
            f"{linhas[atual][4]:<15}"
        )

        atual += 1

        print("-" * 90)
        atual +=1     
    
    return linhas

