numero_partidas = int(input())
for i in range(numero_partidas):
    ponto = False

    saque = int(input())
    levantamento = int(input())
    atacante = input()
    sacador = input()

    if (saque ** 3) % 3 == 0:
        print(f"AAAAACE! ELE MESMO, {sacador}! UMA FERA! UMA BESTA ENJAULADA!")
    elif saque % 2 == 0:
        print(f"Saque pra fora do {sacador}, que desperdicio de uma bela oportunidade!!!")
    elif saque % 2 == 1:
        print(f"Bom saque do {sacador}, bola em jogo!")
        if int(levantamento ** (1 / 3)) % 2 == 0:
            print(f"Levantamento longo na lateral para o {atacante} finalizar")
        elif int(levantamento ** (1 / 3)) % 2 == 1:
            print(f"Levantamento rápido com maestria no meio para o {atacante} finalizar")
        if saque >= levantamento:
            print("NÃO! NÃO É ASSIM...")
            ponto = True
        elif saque < levantamento:
            print(f"Bom ataque do {atacante}! momento decisivo!")
            if (saque + levantamento) % 2 == 0:
                print("A bola volta para o campo do Brasil, recomeça o lance!")
            elif (saque + levantamento) % 2 == 1:
                print("É DO BRASIL!!!!")
                ponto = True

        while ponto == False:
            saque = int(input())
            levantamento = int(input())
            atacante = input()

            if int(levantamento ** (1/3)) % 2 == 0:
                print(f"Levantamento longo na lateral para o {atacante} finalizar")
            elif int(levantamento ** (1/3)) % 2 == 1:
                print(f"Levantamento rápido com maestria no meio para o {atacante} finalizar")
            if saque >= levantamento:
                print("NÃO! NÃO É ASSIM...")
                ponto = True
            elif saque < levantamento:
                print(f"Bom ataque do {atacante}! momento decisivo!")
                if (saque + levantamento) % 2 == 0:
                    print("A bola volta para o campo do Brasil, recomeça o lance!")
                elif (saque + levantamento) % 2 == 1:
                    print("É DO BRASIL!!!!")
                    ponto = True
