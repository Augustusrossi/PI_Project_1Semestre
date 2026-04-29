#imports: 
import requerimentos, paciente, chamadaBanco


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
    'Sair do programa'
]

menuPaciente = [
    'Cadastrar novo paciente', \
    'Solicitar um atendimento',\
    'Vizualisar status do atendimento',\
    'Listar histórico dos atendimentos',\
    'Listar todos os pacientes cadastrados',\
    'Procurar um paciente pelo nome',\
    'Voltar'
]

menuMedico = [
    'Cadastrar um novo médico no sistema', \
    'Vizualisar pacientes relacionados',\
    'Vizualisar requerimentos relacionados',\
    'Mudar status do requerimento de um paciente específico',\
    'Voltar'
    
]

def chamarMenuPaciente():
    desejaSairDoPrograma=False
    while not desejaSairDoPrograma:
        print('------------------------')
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
            procurarPacienteNome()
        else: # if opcao==7:
            fechaConexao()
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')

def chamarMenuMedico():
    desejaSairDoPrograma=False
    while not desejaSairDoPrograma:
        print('------------------------')
        opcao = int(opcaoEscolhida(menuMedico))

        if opcao==1:
            cadastrarMedico()
        elif opcao==2:
            visualizarPacientesRelacionados()
        elif opcao==3:
            visualizarRequerimentos()
        elif opcao==4:
            atualizarStatus()
        else: # if opcao==5:
            fechaConexao()
            desejaSairDoPrograma=True

    print()        
    print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')


#funções paciente:
def cadastrarPaciente():
    print('\n------------------------')
    print("--- Inserir um paciente no sistema! ---")
    paciente.insercao_paciente()
    
def solicitarAtendimento():
    print('\n------------------------')
    print("--- Solicitação de atendimento / cadastro do requerimento --- !")
    
    prioridade = ((requerimentos.dor() * 5) + (requerimentos.tempo() * 3) + (requerimentos.desconforto() * 2)) / 10

    if prioridade < 5:
        print("Sem urgência")
    elif prioridade <= 7:
        print("Urgente")
    else:
        print("Crítico")

def listarPacientes():
    print('\n------------------------')
    print("Visualização de todos os pacientes")
    paciente.listar_pacientes()
    
def procurarPacienteNome():
    print('\n------------------------')
    print("--- Procurar um paciente pelo nome do mesmo! ---")
    
def visualizarStatus():
    print('\n------------------------')
    print("--- Visualização do status do paciente! ---")

def listarHistorico ():
    print('\n------------------------')
    print("--- Listagem de últimas consultas realizadas para aquele paciente! ---")
    
def fechaConexao():
    print('\n------------------------')
    print("--- Conexão encerrada com sucesso! ---")



#funções médico:
def cadastrarMedico ():
    print('\n------------------------')
    print("--- Cadastro de médico! ---")
    
def visualizarPacientesRelacionados ():
    print('\n------------------------')
    print("--- Listagem dos pacientes relacionados - nome! ...")

def visualizarRequerimentos ():
    print('\n------------------------')
    print("--- Visualização dos requerimentos relacionados! ---")
    
def atualizarStatus ():
    print('\n------------------------')
    print("--- Alteração do status de um requerimento! ---")


desejaSairDoPrograma=False
while not desejaSairDoPrograma:
    print('------------------------')
    opcao = int(opcaoEscolhida(menuLogin))

    if opcao==1:
        chamarMenuPaciente()
    elif opcao==2:
        chamarMenuMedico()
    else: # if opcao==3:
        fechaConexao()
        desejaSairDoPrograma=True

print()        
print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')

