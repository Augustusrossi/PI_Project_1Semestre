from datetime import date, datetime
import chamadaBanco

def nome(): 
    valor_verificado = False
    while valor_verificado == False:
        
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
            else:
                nome = nome_completo_partes[0]
                #join -> juntar elementos de uma lista em uma string
                sobrenome = " ".join(nome_completo_partes[1:])
                print("Nome do paciente cadastrado com sucesso\n")
                
        else:
            print("Entrada inválida! Digite apenas letras.")
                
        return nome + " " + sobrenome
        
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


data_br = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    
def insercao_paciente():
    comando=f"insert into paciente (nome, rg, telefone, data_cadastro) values ('{nome()}','{documento_rg()}', '{telefone_contato()}', '{data_br}')"
    conexao=chamadaBanco.obtem_conexao("127.0.0.1","root","123456","sistemaHospital")
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Paciente cadastrado com sucessor")
    
    
def listar_pacientes():
    comando = f"select * from paciente"
    conexao=chamadaBanco.obtem_conexao("127.0.0.1","root","123456","sistemaHospital")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    
    atual = 0
<<<<<<< Updated upstream
    while atual<len(linhas):
        print(linhas[atual][0]," | ",linhas[atual][1]," | ",linhas[atual][2]," | ", linhas[atual][3]," | ",linhas[atual][4])
        atual+=1

def listar_consultas_por_nome(nome_paciente):
    comando = f"""
        SELECT r.id_requerimento, p.nome AS paciente, m.nome AS medico,
               r.descricao, r.data_hora_abertura, r.data_hora_fechamento,
               r.estagio, r.prioridade
        FROM requerimentos r
        JOIN Paciente p ON r.id_paciente = p.id_paciente
        JOIN medico m ON r.id_medico = m.crm
        WHERE p.nome = '{nome_paciente}';
    """
=======
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
        
>>>>>>> Stashed changes

    conexao = chamadaBanco.obtem_conexao("127.0.0.1", "root", "123456", "sistemaHospital")
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
<<<<<<< Updated upstream

    for consulta in linhas:
        print(
            f"Consulta {consulta[0]} | Paciente: {consulta[1]} | Médico: {consulta[2]} | "
            f"Descrição: {consulta[3]} | Abertura: {consulta[4]} | Fechamento: {consulta[5]} | "
            f"Estágio: {consulta[6]} | Prioridade: {consulta[7]}"
        )
=======
    
    
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

#listar_pacientes()
>>>>>>> Stashed changes
