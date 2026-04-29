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
    while atual<len(linhas):
        print(linhas[atual][0]," | ",linhas[atual][1]," | ",linhas[atual][2]," | ", linhas[atual][3]," | ",linhas[atual][4])
        atual+=1