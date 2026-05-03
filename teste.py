import imports

        
        
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



insercao_requerimento(1)


