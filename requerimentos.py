import paciente, imports


def desconforto():
    valor_verificado = False
    while valor_verificado == False:
        try:
            desconforto = int(input("\nDigite o nível de desconforto (1 a 5): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o nível de desconforto. \nDigite Novamente| \n")
            print("----------------------------------")

        else:
            if desconforto >= 1 and desconforto <= 5:
                valor_verificado = True
                return desconforto
            else: 
                valor_verificado = False
                print("Nível de desconforto deve ser entre 1 e 5. \nDigite Novamente| \n")
                print("----------------------------------")
    
def dor():
    valor_verificado = False
    while valor_verificado == False:
        try:
            desconforto = int(input("Digite o nível de dor (1 a 10): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o nível de dor. \nDigite Novamente| \n")
            print("----------------------------------")
        else:
            if desconforto >= 1 and desconforto <= 10:
                valor_verificado = True
                return desconforto
            else: 
                valor_verificado = False
                print("Nível de dor deve ser entre 1 e 10. \nDigite Novamente| \n")
                print("----------------------------------")

def tempo():
    valor_verificado = False
    while valor_verificado == False:
        try:
            tempo = int(input("\nQuanto tempo está com os sintomas? \n1- Menos de 1 semana; \n2- Entre 1 e 2 semanas; \nEntre 2 e 3 semanas; \n4- Entre 3 e 4 semanas; \n5- Por volta de 5 ou mais semanas; \n"))


        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o tempo.")
            print("----------------------------------\n")
        else:
            if tempo >= 1 and tempo <= 5:
                valor_verificado = True
                
                tempo_text = ''
                
                if(tempo == 1):
                    tempo_text = 'menos de 1 semana.'
                elif(tempo == 2):
                    tempo_text = 'cerca de 1 e 2 semanas.'
                elif(tempo == 3):
                    tempo_text = 'cerca de 2 e 3 semanas.'
                elif(tempo == 4):
                    tempo_text = 'cerca de 3 e 4 semanas.'
                else:
                    tempo_text = 'um tempo maior que 5 semanas'
                
                result = [tempo, tempo_text]
                return result
            else: 
                valor_verificado = False
                print("Opção para o tempo deve ser entre 1 e 5. \nDigite Novamente| \n")
                print("----------------------------------\n")

def calculo_prioridade(valor_dor, valor_tempo, valor_desconforto):
    prioridade = ((valor_dor * 5) + (valor_tempo * 3) + (valor_desconforto) * 2) / 10
    prioridade_text = ''

    if prioridade < 5:
        prioridade_text = 'Sem urgência'
    elif prioridade <= 7:
        prioridade_text = 'Urgente'
    else:
        prioridade_text = 'Crítico'

        
    return [prioridade, prioridade_text]


#id_paciente = paciente.procurar_paciente(1,0);
#nome_paciente = paciente.procurar_paciente(1,1);
data_br = imports.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")


def insercao_requerimento(id_paciente_escolhido):
    id_paciente = paciente.procurar_paciente(id_paciente_escolhido,0);
    nome_paciente = paciente.procurar_paciente(id_paciente_escolhido,1);
    
    print("ID:", id_paciente)
    print("Nome:", nome_paciente)
    
    valor_dor = dor()
    valor_desconforto = desconforto()
    valor_tempo, text_tempo = tempo()
    
    
    comando=f"insert into requerimentos (id_medico, id_paciente, descricao, data_hora_abertura, data_hora_fechamento, status, prioridade) values (NULL, {id_paciente}, 'O paciente, {nome_paciente}, apresenta um desconforto de grau: {valor_desconforto} e uma dor de grau: {valor_dor} por {text_tempo}', '{data_br}', NULL,'aberto',{calculo_prioridade(valor_dor, valor_tempo, valor_desconforto)[0]}) "
    
    conexao=imports.chamadaBanco.obtem_conexao("127.0.0.1","root","123456","sistemaHospital")
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Solicitação cadastrada com sucessor")


print("=== PROGRAMA DE PRIORIDADE MÉDICA ===")
