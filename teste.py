import imports, requerimentos, paciente

        
        
def procurar_paciente(id,posicao_info):
    comando = f"select id_paciente, nome, rg, telefone, DATE_FORMAT(data_cadastro, '%d/%m/%Y %H:%i:%s') as data_formatada from paciente where id_paciente = {id}"
    conexao=imports.chamadaBanco.obtem_conexao("127.0.0.1","root","123456","sistemaHospital")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    
    #data = linhas[atual][4]
        
    if linhas == []: return False
    
    if posicao_info == None:
        return(linhas[0])
    else:
        return(linhas[0][posicao_info])
        

def insercao_requerimento(id_paciente_escolhido):
    id_paciente = procurar_paciente(id_paciente_escolhido,0);
    nome_paciente = procurar_paciente(id_paciente_escolhido,1);
    
    print("ID:", id_paciente)
    print("Nome:", nome_paciente)


def inserir_dados_requerimento(valorMinino, valorMaximo):
    
    while True:
        try:
            value = int(input("Escolha entre , valorMinino, valorMaximo,: "))
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
            

def insercao_requerimento(id_paciente_escolhido):
    print("\n" + "="*40)
    print(f"{'ABERTURA DE NOVO REQUERIMENTO':^40}")
    print("="*40,"\n")
    
    print("Digite o nível de dor (1 a 10): ",end="")
    valor_dor = int(inserir_dados_requerimento(1, 10))
    
    print("Digite o nível de desconforto (1 a 5)")
    valor_desconforto = int(inserir_dados_requerimento(1, 5))
    
    print('''
        "\nQuanto tempo está com os sintomas? 
        \n1- Menos de 1 semana; 
        \n2- Entre 1 e 2 semanas; 
        \n3- Entre 2 e 3 semanas; 
        \n4- Entre 3 e 4 semanas; 
        \n5- Por volta de 5 ou mais semanas; \n"
        ''')
    valor_tempo = int(inserir_dados_requerimento(1,5))

    
    id_paciente = paciente.procurar_paciente(id_paciente_escolhido,0);
    nome_paciente = paciente.procurar_paciente(id_paciente_escolhido,1);
    
    print("ID:", id_paciente, end='')
    print(", Nome:", nome_paciente)
    
    comando=f"insert into requerimentos (id_medico, id_paciente, descricao, data_hora_abertura, data_hora_fechamento, status, prioridade) values (NULL, {id_paciente}, 'O paciente, {nome_paciente}, apresenta um desconforto de grau: {valor_desconforto} e uma dor de grau: {valor_dor} por {text_tempo}', '{data_br}', NULL,'aberto',{calculo_prioridade(valor_dor, valor_tempo, valor_desconforto)[1]}) "
    
    conexao=imports.chamadaBanco.obtem_conexao()
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Solicitação cadastrada com sucessor")



paciente.listar_pacientes()
