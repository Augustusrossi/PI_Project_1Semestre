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
    'Vizualisar status do atendimento',\
    'Listar histórico dos atendimentos',\
    'Listar todos os pacientes cadastrados',\
    'Procurar um paciente pelo id',\
    'Voltar'
]

menuMedico = [
    'Cadastrar um novo médico no sistema', \
    'Vizualisar todos os médicos cadastrados',\
    'Vizualisar pacientes relacionados',\
    'Vizualisar requerimentos relacionados',\
    'Associar médico a  um requerimento',\
    'Fechamento do requerimento de um paciente específico',\
    'Voltar'
]

def chamarMenuPaciente():
    desejaSairDoPrograma=False
    while not desejaSairDoPrograma:
        print('\n------------------------')
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
            fechaConexao()
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')

def chamarMenuMedico():
    desejaSairDoPrograma=False
    while not desejaSairDoPrograma:
        print('\n------------------------')
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
            fecharRequerimento ()
        else: # if opcao==5:
            fechaConexao()
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')


#funções paciente:
def cadastrarPaciente():
    print('------------------------\n')
    print("--- Inserir um paciente no sistema! ---")
    paciente.insercao_paciente()

    
def solicitarAtendimento():
    print('\n------------------------\n ')
    listarPacientes()
    print("\n--- Solicitação de atendimento / cadastro do requerimento --- !")
    
    while True:
        try:
            id_paciente = int(input("Digite o id do paciente que corresponderá ao requerimento dele: "))
            
            if(paciente.procurar_paciente(id_paciente,0) == False):
                print("Paciente não existente para esse valor de identificação (id_paciente)!\n")
                continue
            
        except ValueError:
            print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
        else:
            requerimentos.insercao_requerimento(id_paciente)
            break


def listarPacientes():
    print('------------------------')
    print("\n--- Visualização de todos os pacientes ---")
    paciente.listar_pacientes()

    
def procurarPacienteId():
    print('------------------------')
    print("\n--- Procurar um paciente pelo id do mesmo! ---")
    
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

        
def visualizarStatus():
    print('------------------------')
    print("\n--- Visualização do status do paciente! ---")
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
            

def listarHistorico ():
    print('------------------------')
    print("\n--- Listagem de últimas consultas realizadas para aquele paciente! ---")
    
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
    
def fechaConexao():
    print('\n------------------------')
    print("\n--- Conexão encerrada com sucesso! ---")



#funções médico:
def cadastrarMedico ():
    print('\n------------------------')
    print("\n--- Cadastro de médico! ---")
    medicos.cadastrar_medicos()

def visualizarMedicos():
    print('\n------------------------')
    print("\n--- Visualizar todos os médicos! ---")
    medicos.listar_medicos()
    

def visualizarPacientesRelacionados ():
    print('\n------------------------')
    print("\n--- Listagem dos pacientes relacionados - nome! ---")
    requerimentos.visualizar_requerimentos_relacionados(None, None)

def relacionarMedicoRequerimento ():
    print('\n------------------------')
    print("\n--- Escolha um requerimento para o médico fazer o atendimento! ---") 
    requerimentos.escolher_requerimento_relacao()

def visualizarRequerimentos ():
    print('\n------------------------')
    print("\n--- Visualização dos requerimentos relacionados! ---")
    
    while True:
        medicos.listar_medicos()
        
        try:
            
            id_medico = int(input("Digite o id do medico para a listagem dos requerimentos relacionados a ele: "))
            
            if(medicos.buscar_medico(id_medico) == False):
                print("Paciente não existente para esse valor de identificação (id_paciente)!\n")
                continue
            
        except ValueError:
            print("Valor inválido, apenas números são aceitos. \nDigite novamente, por favor!\n")
        else:
            requerimentos.visualizar_requerimentos_relacionados(id_medico, None)
            break

    
def fecharRequerimento ():
    print('\n------------------------')
    print("\n--- Dê alta para um paciente! ---")
    requerimentos.finalizar_requerimento()

def estatisticas():
    print('\n------------------------')
    print("\n--- Estatisticas Gerais! ---") 
    requerimentos.estatistica()


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

