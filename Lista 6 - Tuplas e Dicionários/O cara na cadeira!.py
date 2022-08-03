def adicionar_viloes(dicionario: dict) -> dict:
    num_viloes = int(input())

    for _ in range(num_viloes):
        vilao = input()
        ataque, defesa, vida = input().split(" - ")
        ataque, valor_ataque = ataque.split(", ")
        defesa, valor_defesa = defesa.split(", ")
        vida, valor_vida = vida.split(", ")

        valor_ataque = int(valor_ataque)
        valor_defesa = int(valor_defesa)
        valor_vida = int(valor_vida)

        dicionario[vilao] = {"ataque": valor_ataque, "defesa": valor_defesa, "vida": valor_vida}

    return dicionario

def acoes_pter(dicionario: dict):
    num_acoes = int(input())

    for _ in range(num_acoes):
        acao = input()

        if acao == "pesquisar vilao":
            pesquisar_vilao(dicionario)

        elif acao == "pesquisar atributo":
            pesquisar_atributo(dicionario)

        elif acao == "comparar atributo":
            comparar_atributo(dicionario)

def pesquisar_vilao(dicionario: dict):
    vilao_pesquisado = input()

    #VILÃO EXISTE:
    if vilao_pesquisado in dicionario: 
        print(f"Os atributos do {vilao_pesquisado} foram:\n\
ataque: {dicionario[vilao_pesquisado]['ataque']}\n\
defesa: {dicionario[vilao_pesquisado]['defesa']}\n\
vida: {dicionario[vilao_pesquisado]['vida']}")

    #VILÃO NÃO EXISTE:
    else: 
        print("Peter, foca nos viloes que tao ai agora! se liga, boy")

def pesquisar_atributo(dicionario: dict):
    vilao_pesquisado = input()

    #VILÃO NÃO EXISTE:
    if vilao_pesquisado not in dicionario: 
        atributo = input()
        print("Peter, foca nos viloes que tao ai agora! se liga, boy")

    #VILÃO EXISTE:
    else: 
        atributo = input()

        #ATRIBUTO NÃO EXISTE:
        if atributo not in dicionario[vilao_pesquisado]:
            print("Ta viajando, peter? nao existe esse atributo")

        #ATRIBUTO EXISTE:
        else:
            print(f"O(a) {atributo} do {vilao_pesquisado} e: {dicionario[vilao_pesquisado][atributo]}")

            if atributo == "vida":
                if dicionario[vilao_pesquisado][atributo] <= 5: #VIDA <= A
                    print(f"{vilao_pesquisado} esta enfraquecido! va para cima dele, peter!!")
                elif dicionario[vilao_pesquisado][atributo] >= 15: #VIDA >= A 15
                    print(f"Nao foque em {vilao_pesquisado} ainda! ele esta muito bem")

            elif atributo == "defesa":
                if dicionario[vilao_pesquisado][atributo] <= 5: #DEFESA <= A 5
                    print(f"Va agora! {vilao_pesquisado} nao se defende bem")
                elif dicionario[vilao_pesquisado][atributo] >= 15: #DEFESA >= A 15
                    print(f"cara, voce nao vai conseguir machuca-lo, {vilao_pesquisado} e uma muralha!")

            elif atributo == "ataque" and dicionario[vilao_pesquisado][atributo] >= 15: #ATAQUE >= A 15
                print(f"{vilao_pesquisado} vai destruir a cidade, chama o Dr. estranho!")

def comparar_atributo(dicionario: dict):
    vilao1 = input()
    vilao2 = input()
    atributo = input()

    print(f"Aqui esta a comparacao, peter!\n\
{vilao1}: {dicionario[vilao1][atributo]} X {vilao2}: {dicionario[vilao2][atributo]}")

    if dicionario[vilao1][atributo] > dicionario[vilao2][atributo]:
        print(f"O vilao com menos {atributo} e o {vilao2}, pra cima dele!")
    else:
        print(f"O vilao com menos {atributo} e o {vilao1}, pra cima dele!")

dic_viloes = {}
dic_viloes = adicionar_viloes(dic_viloes)
acoes_pter(dic_viloes)