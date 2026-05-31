#imports: 
import requerimentos, paciente, medicos


def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()
    
    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Escolha uma opção para efetuar o cadastro! \nQual a opção que deseja? ', 'Opção inválida', opcoesValidas)


menuLogin = [
    'Acessar menu do Paciente',\
    'Acessar menu do Médico',\
    'Estatísticas',\
    'Sair do programa'
]

menuPaciente = [
    'Cadastrar novo paciente', \
    'Solicitar um atendimento',\
    'Visualizar status de um atendimento',\
    'Listar histórico dos atendimentos',\
    'Listar todos os pacientes cadastrados',\
    'Procurar um paciente pelo id',\
    'Voltar'
]

menuMedico = [
    'Cadastrar um novo médico no sistema', \
    'Visualizar todos os médicos cadastrados',\
    'Visualizar pacientes relacionados',\
    'Visualizar requerimentos relacionados',\
    'Associar médico a um requerimento',\
    'Listar pacientes baseado em um filtro',\
    'Fechamento do requerimento de um paciente específico',\
    'Voltar'
]

def chamarMenuPaciente():
    desejaSairDoPrograma=False
    print("\n" + "="*50)
    print(f"{'MENU DOS PACIENTES':^50}")
    print("="*50,'\n') 
    while not desejaSairDoPrograma:
        opcao = int(opcaoEscolhida(menuPaciente))

        if opcao==1:
            cadastrarPaciente()
        elif opcao==2:
            solicitarAtendimento()
        elif opcao==3:
            visualizarStatus()
        elif opcao==4:
            listarHistorico()
        elif opcao==5:
            listarPacientes()
        elif opcao==6:
            procurarPacienteId()
        else: # if opcao==7:
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')

def chamarMenuMedico():
    desejaSairDoPrograma=False
    print("\n" + "="*50)
    print(f"{'MENU DOS MÉDICOS':^50}")
    print("="*50,'\n') 
    
    while not desejaSairDoPrograma: 
        
        opcao = int(opcaoEscolhida(menuMedico))

        if opcao==1:
            cadastrarMedico()
        elif opcao==2:
            visualizarMedicos()
        elif opcao==3:
            visualizarPacientesRelacionados()
        elif opcao==4:
            visualizarRequerimentos()
        elif opcao==5:
            relacionarMedicoRequerimento()
        elif opcao==6:
            listar_requerimentos_baseado_filtro()
        elif opcao==7:
            fecharRequerimento ()
        else: # if opcao=8:
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')


#funções paciente:
def cadastrarPaciente():
    print('\n----------------------------------------')
    print("      CADASTRO DE NOVO PACIENTE         ")
    print('----------------------------------------\n')
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Inserir Paciente\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                paciente.insercao_paciente()
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def solicitarAtendimento():    
    print('\n----------------------------------------')
    print("      SOLICITAR NOVO ATENDIMENTO        ")
    print('----------------------------------------\n')
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Solicitar um Atendimento\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                
                while True:
                    try:
                        paciente.listar_pacientes()
                        id_paciente = int(input("Digite o id do paciente que corresponderá ao requerimento dele: "))
                        
                        if(paciente.procurar_paciente(id_paciente,0) == False):
                            print("Paciente não existente para esse valor de identificação (id_paciente)!\n")
                            continue
                        
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        requerimentos.insercao_requerimento(id_paciente)
                        break
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def listarPacientes():
    print('\n----------------------------------------')
    print("    VISUALIZAR PACIENTES CADASTRADOS    ")
    print('----------------------------------------\n')
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Listar Pacientes\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                paciente.listar_pacientes()
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue
    
def procurarPacienteId():
    print('\n----------------------------------------')
    print("       BUSCAR PACIENTE POR ID           ")
    print('----------------------------------------\n')
    
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Procurar Paciente\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
    
                while True:
                    try:
                        id_paciente = int(input("Digite o id do paciente que corresponderá ao requerimento dele: "))
                        
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        if(paciente.procurar_paciente(id_paciente,0) == False):
                            print("Paciente não existente para esse valor de identificação (id_paciente)!\n")
                            continue
                        
                        print(paciente.procurar_paciente(id_paciente, None))
                        break
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue
        
def visualizarStatus():
    print('\n----------------------------------------')
    print("     VISUALIZAR STATUS DE ATENDIMENTO   ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Visualizar status de um atendimento \n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
    
                while True:
                    try:    
                        requerimentos.buscar_requerimento(None, 'geral')
                        id_req = int(input("Digite o id do requerimento que deseja verificar o status: "))
                        
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        if(paciente.visualizar_status(id_req) == False):
                            print("Requerimento inexistente para esse valor de identificação (id_requerimento)!\n")
                            continue
                        break        
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")    
                continue

def listarHistorico ():
    print('\n----------------------------------------')
    print("        HISTÓRICO DE CONSULTAS          ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do paciente\n1- Procurar Paciente\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
    
                while True:
                    try:
                        paciente.listar_pacientes()
                        id_paciente = int(input("Digite o id do paciente que corresponderá ao histórico dele: "))
                        
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        if(paciente.procurar_paciente(id_paciente,0) == False):
                            print("Paciente não existente para esse valor de identificação (id_paciente)!\n")
                            continue
                        
                        paciente.listar_historico(id_paciente)
                        break
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue
    
def fechaConexao():
    print('\n----------------------------------------')
    print("        CONEXÃO ENCERRADA COM SUCESSO         ")
    print('----------------------------------------\n')



#funções médico:
def cadastrarMedico ():
    print('\n----------------------------------------')
    print("        CADASTRO DE NOVO MÉDICO         ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Cadastrar novo médico no sistema\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                medicos.cadastrar_medicos()
                
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def visualizarMedicos():
    print('\n----------------------------------------')
    print("      MÉDICOS CADASTRADOS NO SISTEMA    ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Visualizar médicos\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                medicos.listar_medicos()
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def listar_requerimentos_baseado_filtro():
    print('\n------------------------------------------------------')
    print("     LISTAR REQUERIMENTOS E PACIENTES COM FILTRO        ")
    print('------------------------------------------------------\n')
    
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Listar requerimentos\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                while True:
                    try: 
                        print("Escolha um filtro para a listagem dos pacientes: \n0 - Voltar para menu de médicos \n1 - Listar requerimentos baseado em prioridade \n2 - Listar requerimentos baseado no status\n")
                        opcaoFiltro = int(input("Digite a opção do filtro que deseja: "))
                    
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        if opcaoFiltro == 0:
                            break
                            
                        elif opcaoFiltro == 1:
                            
                            while True:
                                try: 
                                    print("0 - Voltar para menu de filtros \n1- Sem urgência\n2- Urgente\n3- Crítico\n")
                                    opcaoEscolhida = int(input("Digite quais requerimentos deseja visualizar: "))
                                
                                except ValueError:
                                    print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                                    continue
                                    
                                else:
                                    print(opcaoEscolhida)
                                    if opcaoEscolhida == 0:
                                        break
                                    elif opcaoEscolhida == 1:
                                        filtro = 'Sem urgência'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    elif opcaoEscolhida == 2:
                                        filtro = 'Urgente'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    elif opcaoEscolhida == 3:
                                        filtro = 'Crítico'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    else:
                                        print("Valor inválido, apenas os números 1, 2 ou 3, são aceitos. \nDigite novamente, por favor!\n")
                                        continue
                            
                        elif opcaoFiltro == 2:
                            while True:
                                try: 
                                    print("0 - Voltar para menu de filtros \n1- Aberto\n2- Em Andamento\n3- Finalizado\n")
                                    opcaoEscolhida = int(input("Digite quais requerimentos deseja visualizar: "));
                                except ValueError:
                                    print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                                    continue
                                else:
                                    print(opcaoEscolhida)

                                    if opcaoEscolhida == 0:
                                        break
                                    elif opcaoEscolhida == 1:
                                        filtro = 'aberto'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    elif opcaoEscolhida == 2:
                                        filtro = 'andamento'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    elif opcaoEscolhida == 3:
                                        filtro = 'Finalizado'
                                        return requerimentos.listagem_requerimentos(opcaoFiltro, filtro)
                                    else:
                                        print("Valor inválido, apenas os números 1, 2 ou 3, são aceitos. \nDigite novamente, por favor!\n")
                                        continue
                        
                        else:
                            print("Valor inválido, apenas números 1 ou 2 são aceitos. \nDigite novamente, por favor!\n")
                            continue

            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue    

def visualizarPacientesRelacionados ():
    print('\n----------------------------------------')
    print("         PACIENTES RELACIONADOS         ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Visualizar todos os pacientes relacionados a um médico\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                requerimentos.visualizar_requerimentos_relacionados(None, None)
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def relacionarMedicoRequerimento ():
    print('\n----------------------------------------')
    print("    VINCULAR MÉDICO A UM REQUERIMENTO   ")
    print('----------------------------------------\n')
    
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Relacionar médico a um requerimento\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                requerimentos.escolher_requerimento_relacao()
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def visualizarRequerimentos ():
    print('\n----------------------------------------')
    print("       REQUERIMENTOS VINCULADOS         ")
    print('----------------------------------------\n')
    
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Visualizar requerimentos relacionados\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:    
                while True:
                    medicos.listar_medicos()
                    
                    try:
                        
                        id_medico = int(input("Digite o id do medico para a listagem dos requerimentos relacionados a ele: "))
                        
                        if(medicos.buscar_medico(id_medico) == False):
                            print("Médico não existente para esse valor de identificação (id_paciente)!\n")
                            continue
                        
                    except ValueError:
                        print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
                    else:
                        requerimentos.visualizar_requerimentos_relacionados(id_medico, None)
                        break
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
    
def fecharRequerimento ():
    print('\n----------------------------------------')
    print("        FINALIZAR REQUERIMENTO          ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu do médico\n1- Finalizar um requerimento\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                requerimentos.finalizar_requerimento()
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue

def estatisticas():
    print('\n----------------------------------------')
    print("          ESTATÍSTICAS GERAIS           ")
    print('----------------------------------------\n')
        
    while True:
        try:
            opcaoEscolhida = int(input("\n==== Digite: ====\n0 - Voltar para o menu geral\n1- Visualizar estatísticas\n=== Escolha: "))
        except ValueError:
            print("\n==== ENTRADA INVÁLIDA ====\n Digite apenas números, por favor!")
            continue
        else:
            if opcaoEscolhida == 0:
                break
            elif opcaoEscolhida == 1:
                requerimentos.estatistica()
                break
            else: 
                print("\n==== ENTRADA INVÁLIDA ====\n Escolha entre 0 ou 1 apenas, por favor!")
                continue


desejaSairDoPrograma=False
while not desejaSairDoPrograma:
    print('------------------------')
    opcao = int(opcaoEscolhida(menuLogin))

    if opcao==1:
        chamarMenuPaciente()
    elif opcao==2:
        chamarMenuMedico()
    elif opcao==3:
        estatisticas()
    else: # if opcao==4:
        fechaConexao()
        desejaSairDoPrograma=True

print()        
print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')

