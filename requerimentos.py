    
    
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
            tempo = int(input("\n Quanto tempo está com os sintomas? \n 1- Menos de 1 semana; \n 2- Entre 1 e 2 semanas; \n Entre 2 e 3 semanas; \n 4- Entre 3 e 4 semanas; \n 5- Por volta de 5 ou mais semanas; \n"))


        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o tempo.")
            print("----------------------------------\n")
        else:
            if tempo >= 1 and tempo <= 5:
                valor_verificado = True
                return tempo
            else: 
                valor_verificado = False
                print("Opção para o tempo deve ser entre 1 e 5. \nDigite Novamente| \n")
                print("----------------------------------\n")

    

print("=== PROGRAMA DE PRIORIDADE MÉDICA ===")
