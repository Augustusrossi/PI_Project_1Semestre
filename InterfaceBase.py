print("=== PROGRAMA DE PRIORIDADE MÉDICA ===")
try:
    dor = int(input("Digite o nível de dor (1 a 10): "))
    if dor < 1 or dor > 10:
        print("Nível de dor deve ser entre 1 e 10.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para o nível de dor.")
else:
    try:
        desconforto = int(input("Digite o nível de desconforto (1 a 5): "))
        if desconforto < 1 or desconforto > 5:
            print("Nível de desconforto deve ser entre 1 e 5.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o nível de desconforto.")
    else:
        try:
            tempo = int(input("Quanto tempo está com os sintomas? \n 1- menos de 1 semana, \n 2- entre 1 e 2 semanas, \n 3- 3 semanas, \n 4- 4 semanas, \n 5- 5 ou mais semanas: "))
            if tempo < 0:
                print("Tempo deve ser um número positivo.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o tempo.")
        else:
            prioridade = (dor * 5 + tempo * 3 + desconforto * 2) / 10
            if prioridade < 5:
                print("Sem urgência")
            elif prioridade <= 7:
                print("Urgente")
            else:
                print("crítico")