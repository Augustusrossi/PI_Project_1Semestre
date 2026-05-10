import paciente, imports, medicos

#Inserção

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

data_br = imports.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")

def insercao_requerimento(id_paciente_escolhido):
    id_paciente = paciente.procurar_paciente(id_paciente_escolhido,0);
    nome_paciente = paciente.procurar_paciente(id_paciente_escolhido,1);
    
    print("ID:", id_paciente, end='')
    print(", Nome:", nome_paciente)
    
    valor_dor = dor()
    valor_desconforto = desconforto()
    valor_tempo, text_tempo = tempo()
    
    
    comando=f"insert into requerimentos (id_medico, id_paciente, descricao, data_hora_abertura, data_hora_fechamento, status, prioridade) values (NULL, {id_paciente}, 'O paciente, {nome_paciente}, apresenta um desconforto de grau: {valor_desconforto} e uma dor de grau: {valor_dor} por {text_tempo}', '{data_br}', NULL,'aberto',{calculo_prioridade(valor_dor, valor_tempo, valor_desconforto)[0]}) "
    
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Solicitação cadastrada com sucessor")


#Visualização

#verificar status

def visualizar_requerimentos_relacionados(id_medico_escolhido,id_requerimento):
    comando = ''

    #lista um requerimento em específico baseado no id de requerimento
    if id_medico_escolhido == None and id_requerimento != None:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE id_requerimento = {id_requerimento}"
    
    #lista requerimentos baseado no id do médico
    elif id_medico_escolhido != None and id_requerimento == None:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE id_medico = {id_medico_escolhido} order by prioridade desc"
        
    #lista um requerimento específico baseado no id do requerimento e em um id de algum medico
    elif id_medico_escolhido != None and id_requerimento != None:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE id_medico = {id_medico_escolhido} and id_requerimento = {id_requerimento} order by prioridade desc"
        
    #lista todos os requerimentos que estão relacionados a algum médico
    else:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE id_medico is not null and data_hora_fechamento is null order by prioridade desc"

    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    if linhas == []: return False

    atual = 0 
    print("\nNome:  |  RG:  |  id do Requerimento:  |  id do Médico:  |  id do Paciente:  |  Descrição:  |  Data de criação do Requerimento:  |  Data de finalização do Requerimento  |  Status:  |  Nível de prioridade: ")
    print('------------------------------------------')
    while atual < len(linhas):
        print(linhas[atual][0], "|", linhas[atual][1], "|", linhas[atual][2], "|", linhas[atual][3], "|", linhas[atual][4], "|", linhas[atual][5], "|", linhas[atual][6], "|", linhas[atual][7], "|", linhas[atual][8], "|", linhas[atual][9])
        print('------------------------------------------')

        atual +=1     
    
    return linhas

        
def buscar_requerimento(id_requerimento,objetivo):
    
    #requerimentos sem relação alguma
    if objetivo.lower() == 'nao_relacionado' and id_requerimento == None:    
        print('\n--- Lista de requerimentos sem relação com algum médico ---\n')
        comando = f"SELECT * FROM requerimentos WHERE id_medico IS NULL" 
        
    #todos os requerimentos
    elif objetivo.lower() == 'geral' and id_requerimento == None:
        print('\n--- Lista de todos os requerimentos ---\n')
        comando = f"SELECT * FROM requerimentos"
        
    #todos os requerimentos finalizados
    else:
        print('\n--- Lista de todos os requerimentos finalizados ---\n')
        comando = f"SELECT * FROM requerimentos where data_hora_fechamento is not null"
        
    #apenas o requerimento especifico 
    # else:
    #     print('\n--- Buscar Requerimento Específico ---\n')
    #     comando = f"SELECT * FROM requerimentos WHERE id_requerimento = {id_requerimento}"
    
    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    atual = 0 
    while atual < len(linhas):
        print(linhas[atual][0], "|", linhas[atual][1], "|", linhas[atual][2], "|", linhas[atual][3], "|", linhas[atual][4], "|", linhas[atual][5], "|", linhas[atual][6], "|", linhas[atual][7])
        print('------------------------------------------')
        atual +=1 
    
    return linhas

def estatistica():
    conexao=imports.chamadaBanco.obtem_conexao()
    
    cursor=conexao.cursor()
    cursor.execute("""select count(id_paciente) from paciente;""")
    value_1 = cursor.fetchall()[0]

    cursor.execute("""select count(id_paciente) from paciente where data_cadastro BETWEEN'2026-01-01' and '2027-01-01';""")
    value_2 = cursor.fetchall()[0]
    
    cursor.execute("""select pac.nome, count(id_requerimento) as maior from requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente group by req.id_paciente order by maior desc limit 1;""")
    value_3 = cursor.fetchall()[0]
    
    cursor.execute("""SELECT AVG(total_requerimentos) AS media_requerimentos
        FROM (
            SELECT COUNT(id_requerimento) AS total_requerimentos
            FROM requerimentos req
            GROUP BY req.id_paciente
        ) as media_paciente""")
    value_4 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_requerimento) from requerimentos;""")
    value_5 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_requerimento) from requerimentos where status LIKE 'aberto';""")
    value_6 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_requerimento) from requerimentos where status LIKE 'andamento';""")
    value_7 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_requerimento) from requerimentos where status LIKE 'finalizado';""")
    value_8 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_requerimento) from requerimentos where data_hora_abertura > '2026-01-01' 
and data_hora_abertura < '2027-01-01';""")
    value_9 = cursor.fetchall()[0]
    
    cursor.execute("""select count(id_medico) from medico""")
    value_10 = cursor.fetchall()[0]
    
    cursor.execute("""SELECT AVG(total_requerimentos) AS media_requerimentos
        FROM (
            SELECT COUNT(id_requerimento) AS total_requerimentos
            FROM requerimentos req
            GROUP BY req.id_medico
        ) as media_paciente""")
    value_11 = cursor.fetchall()[0]
    
    cursor.execute("""select med.nome, count(id_requerimento) as maior
        from requerimentos req INNER JOIN medico med on med.id_medico = req.id_medico
        group by req.id_medico order by maior desc limit 1""")
    value_12 = cursor.fetchall()[0]
    
    cursor.execute("""SELECT AVG(total_requerimentos) AS media_requerimentos
        FROM (
            SELECT COUNT(id_requerimento) AS total_requerimentos
            FROM requerimentos
            GROUP BY DATE(data_hora_abertura)
        ) as media_requerimentos_diario """)
    value_13 = cursor.fetchall()[0]
    
    print(f"{'Estatística':50} | {'Valor'}")
    print("-" * 70)

    print(f"{'Total de pacientes':50} | {value_1[0]}")
    print(f"{'Total de pacientes cadastrados no último ano':50} | {value_2[0]}")

    print(f"{'Paciente com mais solicitações':50} | {value_3}")
    print(f"{'Média de requerimentos p/ paciente':50} | {value_4[0]}")

    print(f"{'Total de requerimentos':50} | {value_5[0]}")
    print(f"{'Value 6':50} | {value_6[0]}")

    print(f"{'Solicitações em aberto':50} | {value_7[0]}")
    print(f"{'Solicitações em andamento':50} | {value_8[0]}")

    print(f"{'Solicitaçõs finalizadas':50} | {value_9[0]}")
    print(f"{'Solicitações cadastradas no último ano':50} | {value_10[0]}")

    print(f"{'Quantidade de requerimentos p/ médico':50} | {value_11[0]:.2f}")
    print(f"{'Médico com mais requerimentos':50} | {value_12}")

    print(f"{'Média diária de requerimentos':50} | {value_13[0]}")
    
    print("-" * 70,"\n")


#Alterações
def escolher_requerimento_relacao():
    
    linhas_paciente = buscar_requerimento(None, 'nao_relacionado')  
            
    id_rquerimentos_validos = []
    contador = 0;
    
    while contador < len(linhas_paciente):
        id_rquerimentos_validos.append(linhas_paciente[contador][0])
        contador+=1
    
    if len(linhas_paciente) != 0:

        while True:
            
            try:
                id_req = int(input ("\nDigite o ID do requerimento que você deseja relacionar o médico: "))
                
                if(id_req < 0):
                    print("\nApenas valores positivos são aceitos.\nDigte novamente.")
                    continue
                
            except ValueError:
                print("Por favor, os identificadores dos requerimentos são números inteiros, portando apenas esse tipo de digíto é aceito. Digite Novamente!\n")
                continue
            else:
                if id_req in id_rquerimentos_validos:
                    print ("ID do requerimento é válido!")
                                
                else:
                    print("\nIdentificador inválido!\nNão existe requerimento com esse identificador.\nDigite novamente!")
                    continue
                
                id_medico = medicos.buscar_medico(None)[0]
                                    
                conexao = imports.chamadaBanco.obtem_conexao()
                cursor = conexao.cursor()
                comando = f"UPDATE requerimentos set id_medico = {id_medico}, status = 'Andamento' WHERE id_requerimento = {id_req}"

                cursor.execute(comando)
                conexao.commit()
                
                if cursor.rowcount > 0:
                    print("Requerimento atualizado com sucesso!\n")
                    visualizar_requerimentos_relacionados(id_medico, None)
                    break
    else:
        print("Não há nenhum requerimento disponível para relacionamento.")
        print("Por favor, cadastre uma nova solicitação para efetuar a relação entre algum médico e o requerimento desejado.\n")
                    

def finalizar_requerimento():
    
    linhas_requerimentos = visualizar_requerimentos_relacionados(None, None)  
            
    id_rquerimentos_validos = []
    contador = 0;
    
    while contador < len(linhas_requerimentos):
        id_rquerimentos_validos.append(linhas_requerimentos[contador][0])
        contador+=1
    
    if len(id_rquerimentos_validos) != 0:
    
        while True:
        
            try:
                id_req = int(input ("\nDigite o ID do requerimento que você deseja finalizar: "))
                
                if(id_req < 0):
                    print("\nApenas valores positivos são aceitos.\nDigte novamente.")
                    continue
                
            except ValueError:
                print("Por favor, os identificadores dos requerimentos são números inteiros, portando apenas esse tipo de digíto é aceito. Digite Novamente!\n")
                continue
            else:
                conexao = imports.chamadaBanco.obtem_conexao()
                cursor = conexao.cursor()
                comando = f"UPDATE requerimentos set data_hora_fechamento = '{data_br}' , status = 'Finalizado' WHERE id_requerimento = {id_req}" 
                
                cursor.execute(comando)
                conexao.commit()
                
                if cursor.rowcount > 0:
                    print("Requerimento Finalizado com sucesso!")
                    visualizar_requerimentos_relacionados(None, id_req)
                    break
    else:
        print("Não há nenhum requerimento disponível para ser finalizado.")
        print("Por favor, cadastre uma nova solicitação.\nEm seguida, efetue a relação entre algum médico e o requerimento desejado.")
        print("Após esses passos será permitido que o requerimento escolhido seja finalizado.\n")
    