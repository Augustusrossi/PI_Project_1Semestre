import paciente, imports, medicos

#Inserção
def inserir_dados_requerimento(valorMinino, valorMaximo):
    
    while True:
        try:
            text = f'Escolha entre {valorMinino} e {valorMaximo}: '
            value = int(input(text))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro. \nDigite Novamente| \n")
            print("----------------------------------")

        else:
            if value >= valorMinino and value <= valorMaximo:
                return value
            else: 
                print("Entrada inválida. Apenas números dentro do intervalo de", valorMinino, "e", valorMaximo,"!\nDigite Novamente| \n")
                print("----------------------------------")
                continue

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
    print("\n" + "="*40)
    print(f"{'ABERTURA DE NOVO REQUERIMENTO':^40}")
    print("="*40,"\n")
    
    print("Digite o nível de dor (1 a 10): ",end="")
    valor_dor = int(inserir_dados_requerimento(1, 10))
    
    print("Digite o nível de desconforto (1 a 5): ",end="")
    valor_desconforto = int(inserir_dados_requerimento(1, 5))
    
    print("\nQuanto tempo está com os sintomas? \n1- Menos de 1 semana; \n2- Entre 1 e 2 semanas; \n3- Entre 2 e 3 semanas; \n4- Entre 3 e 4 semanas; \n5- Por volta de 5 ou mais semanas; \n")
    valor_tempo = int(inserir_dados_requerimento(1,5))
    text_tempo = ''
    if valor_tempo == 1:
        text_tempo = 'menos de 1 semana.'
    elif valor_tempo == 2:
        text_tempo = 'cerca de 1 e 2 semanas.'
    elif valor_tempo == 3:
        text_tempo = 'cerca de 2 e 3 semanas.'
    elif valor_tempo == 4:
        text_tempo = 'cerca de 3 e 4 semanas.'
    else:
        text_tempo = 'um tempo maior que 5 semanas.'
    
    id_paciente = paciente.procurar_paciente(id_paciente_escolhido,0);
    nome_paciente = paciente.procurar_paciente(id_paciente_escolhido,1);
    
    print("ID:", id_paciente, end='')
    print(", Nome:", nome_paciente)
    
    texto_prioridade = calculo_prioridade(valor_dor, valor_tempo, valor_desconforto)[1]
    descricao_completa = f"O paciente, {nome_paciente}, apresenta um desconforto de grau: {valor_desconforto} e uma dor de grau: {valor_dor} por {text_tempo}"
    
    comando=f"insert into requerimentos (id_medico, id_paciente, descricao, data_hora_abertura, data_hora_fechamento, status, prioridade) values (NULL, {id_paciente}, '{descricao_completa}', '{data_br}', NULL,'aberto','{texto_prioridade}') "
    
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Solicitação cadastrada com sucessor")


#Visualização


def visualizar_requerimentos_relacionados(id_medico_escolhido,id_requerimento):
    print("\n" + "="*45)
    print(f"{'REQUERIMENTOS VINCULADOS A MÉDICOS':^45}")
    print("="*45,'\n')
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
    print("-" * 140)
    print(f"{'Nome':<25}| "f"{'RG':<12}| "f"{'ID Req.':<8}| "f"{'ID Méd.':<8}| "f"{'ID Pac.':<8}| "f"{'Data Abertura':<20}| "f"{'Data Fechamento':<20}| "f"{'Status':<12}| "f"{'Prioridade':<12}")
    print("-" * 140)
    while atual < len(linhas):
        print(
            f"{linhas[atual][0]:<25}|",
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
        print("-" * 140)

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

    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    print("-" * 140)
    print(f"{'ID Req.':<10}| "f"{'ID Méd.':<10}| "f"{'ID Pac.':<10}| "f"{'Data Abertura':<20}| "f"{'Data Fechamento':<20}| "f"{'Status':<15}| "f"{'Prioridade':<15}" )
    print("-" * 140)

    atual = 0 
    while atual < len(linhas):
        print(
            f"{linhas[atual][0]:<10}| "
            f"{str(linhas[atual][1]):<10}| "
            f"{linhas[atual][2]:<10}| "
            f"{str(linhas[atual][4]):<20}| "
            f"{str(linhas[atual][5]):<20}| "
            f"{linhas[atual][6]:<15}| "
            f"{linhas[atual][7]:<15}"
        )
        print(f"Descrição: {linhas[atual][3]}")
        print("-" * 140)
        atual +=1 
    
    return linhas

def visualizacao_simplificada():
    
    print('\n--- Lista de todos os requerimentos ---\n')
    comando = f"SELECT req.id_requerimento, req.id_paciente, pac.nome,  req.id_medico, med.nome, req.data_hora_abertura FROM requerimentos req inner join paciente pac on pac.id_paciente = req.id_paciente inner join medico med on med.id_medico = req.id_medico"
        
    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    print("-" * 111)
    print(f"{'ID Req.':<10}| "f"{'ID Pac.':<10}| "f"{'Nome Pacientes':<25}| "f"{'ID Mec.':<10}| "f"{'Nome Médicos':<25}| "f"{'Data Abertura':<20}| " )
    print("-" * 111)

    atual = 0 
    while atual < len(linhas):
        print(
            f"{linhas[atual][0]:<10}| "
            f"{str(linhas[atual][1]):<10}| "
            f"{linhas[atual][2]:<25}| "
            f"{str(linhas[atual][3]):<10}| "
            f"{linhas[atual][2]:<25}| "
            f"{str(linhas[atual][5]):<20}| "
        )
        # print(f"Descrição: {linhas[atual][3]}")
        print("-" * 111)
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
    value_3 = cursor.fetchone()

    if value_3 is None:
        value_3 = ("Nenhum paciente", 0)
    
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
    value_12 = cursor.fetchone()

    if value_12 is None:
        value_12 = ("Nenhum médico", 0)
    
    cursor.execute("""SELECT AVG(total_requerimentos) AS media_requerimentos
        FROM (
            SELECT COUNT(id_requerimento) AS total_requerimentos
            FROM requerimentos
            GROUP BY DATE(data_hora_abertura)
        ) as media_requerimentos_diario """)
    value_13 = cursor.fetchall()[0]
    
    if (
        value_3 is None or
        value_12 is None or
        value_4[0] is None or
        value_11[0] is None or
        value_13[0] is None
    ):
        print("\nDados insuficientes para fornecer as estatísticas.\n")
        return
    
    print(f"{'Estatística':50} | {'Valor'}")
    print("-" * 70)

    print(f"{'Total de pacientes':50} | {value_1[0]}")
    print(f"{'Total de pacientes cadastrados no último ano':50} | {value_2[0]}")

    print(f"{'Paciente com mais solicitações':50} | {value_3}")
    print(f"{'Média de requerimentos p/ paciente':50} | {value_4[0]}")

    print(f"{'Total de requerimentos':50} | {value_5[0]}")
    print(f"{'Solicitações em aberto':50} | {value_6[0]}")

    print(f"{'Solicitações em andamento':50} | {value_7[0]}")
    print(f"{'Solicitaçõs finalizadas':50} | {value_8[0]}")

    print(f"{'Solicitações cadastradas no último ano':50} | {value_9[0]}")
    print(f"{'Total de médicos cadastrados':50} | {value_10[0]}")

    print(f"{'Quantidade de requerimentos p/ médico':50} | {value_11[0]:.2f}")
    print(f"{'Médico com mais requerimentos':50} | {value_12}")

    print(f"{'Média diária de requerimentos':50} | {value_13[0]}")
    
    print("-" * 70,"\n")


def listagem_requerimentos(opcao,filtro):
    print("\n" + "="*40)
    print(f"{'FILTRAR REQUERIMENTOS':^40}")
    print("="*40,'\n')   
    #lista um requerimento em específico baseado na prioridade
    print(opcao, filtro)
    if int(opcao) == 1:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE prioridade like '{filtro}'"
    elif int(opcao) == 2:
        comando = f"SELECT pac.nome, pac.rg, req.* FROM requerimentos req INNER JOIN paciente pac on pac.id_paciente = req.id_paciente WHERE status like '{filtro}'"
    
    conexao = imports.chamadaBanco.obtem_conexao()
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()
    
    print("-" * 180)
    print(f"{'Nome':<25}| ""{'RG':<12}| "f"{'ID Req.':<8}| "f"{'ID Méd.':<8}| "f"{'ID Pac.':<8}| "f"{'Data Abertura':<20}| "f"{'Data Fechamento':<20}| "f"{'Status':<12}| "f"{'Prioridade':<12}"
    )
    print("-" * 180)  
    atual = 0 
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

        atual +=1 
    
    return linhas


#Alterações
def escolher_requerimento_relacao():
    print("\n" + "="*40)
    print(f"{'VINCULAR MÉDICO AO REQUERIMENTO':^40}")
    print("="*40,'\n')
    
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
    print("\n" + "="*40)
    print(f"{'ENCERRAMENTO DE REQUERIMENTO':^40}")
    print("="*40,'\n')
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
    
    