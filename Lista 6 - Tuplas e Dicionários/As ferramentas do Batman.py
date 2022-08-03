def calcular_vida(num: int, vida: int, armas_disponiveis: dict) -> int:
    vida_atual = vida

    #NUMERO DE ARMAS UTILIZADAS:
    for _ in range(num):
        arma = input()

        #ARMA DISPONÍVEL NO ARSENAL:
        if arma in armas_disponiveis:
            dano = armas_disponiveis[arma]

            if vida_atual > vida * 4 / 10:
                vida_atual -= dano

            else:
                if dano >= 100 and dano < 200:
                    vida_atual -= dano / 2
                elif dano >= 200 and dano < 300:
                    vida_atual -= dano / 4
                elif dano >= 300:
                    vida_atual -= dano * 3 / 20

        #ARMA NÃO DISPONÍVEL NO ARSENAL:
        else:
            print(f"{arma}? Infelizmente esta ferramenta não está disponível.")

    return vida_atual

def analisar_batalha(vida_inicial: int, vida_final: int, resultado: dict) -> dict:
    if vida_final > vida_inicial * 3 / 20:
        resultado["fugas"] += 1
    elif vida_final <= vida_inicial * 3 / 20 and vida_final > 0:
        resultado["incapacitados"] += 1
    else:
        resultado["mortos"] += 1

    return resultado

def printar_resultado(resultado: dict):
    print(f"Mortos: {resultado['mortos']}\nFugas: {resultado['fugas']}\nIncapacitados: {resultado['incapacitados']}")

    #NÚMERO DE SUCESSOS MAIOR QUE O NÚMERO DE FRACASSOS:
    if resultado["incapacitados"] > resultado["fugas"] + resultado["mortos"]:

        #NÚMERO DE FRACASSOS MAIOR QUE 0:
        if resultado["fugas"] + resultado["mortos"] > 0:
            print("Batman conseguiu capturar a maioria dos criminosos, nosso herói está no caminho certo.")
        
        #NÚMERO DE FRACASSOS IGUAL A 0:
        else:
            print("Batman conseguiu capturar todos os criminosos e garantiu uma noite segura em Gotham City.")
    
    #NÚMERO DE FRACASSOS MAIOR QUE O NÚMERO DE SUCESSOS:
    elif resultado["incapacitados"] < resultado["fugas"] + resultado["mortos"]:

        #NÚMERO DE SUCESSOS MAIOR QUE 0:
        if resultado["incapacitados"] > 0:
            print("Muitas missões fracassadas.. Pelo visto, o nosso herói precisa treinar mais.")

        #NÚMERO DE SUCESSOS IGUAL A 0:
        else:
            print("Muitas missões fracassadas... Tem certeza de que o seu programa passou as ferramentas corretas?")

    #NÚMERO DE SUCESSOS IGUAL AO NÚMERO DE FRACASSOS:
    else:
        print("Uma noite caótica em Gotham City, talvez o nosso herói precise mudar as ferramentas...")

def batalhas(armas_disponiveis: dict):
    num_batalhas = int(input())
    resultado_batalhas = {"mortos": 0, "fugas": 0, "incapacitados": 0}
    for _ in range(num_batalhas):
        num_ferramentas = int(input())
        vida_inimigo = int(input())

        vida_final = calcular_vida(num_ferramentas, vida_inimigo, armas_disponiveis)
        resultado_batalhas = analisar_batalha(vida_inimigo, vida_final, resultado_batalhas)
    printar_resultado(resultado_batalhas)


armas_batman = {"Batrangue": 270, "Bat-Minas": 255, "Tasers": 185, "Soqueiras": 150,\
    "Granada Sonica": 300, "Gel Explosivo": 400, "Faca Tatica": 345}
batalhas(armas_batman)