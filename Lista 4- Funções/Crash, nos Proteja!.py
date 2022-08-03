numero_viloes = int(input())
numero_vitorias = 0
numero_derrotas = 0
total_frutas = 0

def luta():
    derrota = 0
    vitoria = 0
    if vida <= dano:
        print("Aku-Aku estamos precisando de você!")
        derrota = 1
    elif vida > dano:
        print(f"O nosso herói conseguiu mais uma vez! Pisou no {inimigo}.")
        vitoria = 1

    return [derrota, vitoria]

def multiplicador_vida():
    if mascara == "Aku-Aku":
        multiplicador = 2
    elif mascara == "Velo":
        multiplicador = 1.25
    elif mascara == "Apo-Apo":
        multiplicador = 1.5

    return multiplicador

def frutas_coletadas():
    frutas = True
    total_frutas_coletadas = 0
    while frutas:
        frutas_coletadas = int(input())
        total_frutas_coletadas += frutas_coletadas
        if frutas_coletadas == 0:
            frutas = False

    return total_frutas_coletadas

if numero_viloes == 0:
    print("Nenhum vilão teve coragem de encarar o Crash hoje!")

else:
    for _ in range(numero_viloes):
        mascara_vida = input().split(" ")
        mascara = mascara_vida[0]
        vida = int(mascara_vida[1]) #TRANSFORMAR VIDA EM INTEIRO

        inimigo_dano = input().split(" ")
        inimigo = inimigo_dano[0]
        dano = int(inimigo_dano[1]) #TRANSFORMAR DANO EM INTEIRO

        # VIDA REAL:
        vida *= multiplicador_vida()

        # FRUTAS COLETADAS:
        total_frutas = 0
        total_frutas += frutas_coletadas()

        # DANO REAL:
        if total_frutas < 10:
            print(f"Infelizmente o Crash só conseguiu pegar {total_frutas}\
 frutas, então, não é hoje que ele vai derrotar o {inimigo} =(")
        elif total_frutas <= 20:
            dano **= 2
            derrota, vitoria = luta()
            numero_derrotas += derrota
            numero_vitorias += vitoria
        elif total_frutas <= 30:
            dano *= 2
            derrota, vitoria = luta()
            numero_derrotas += derrota
            numero_vitorias += vitoria
        else:
            derrota, vitoria = luta()
            numero_derrotas += derrota
            numero_vitorias += vitoria

    if numero_derrotas >= numero_vitorias:
        print(f"Não é possível, o Crash não conseguiu vencer?")
    else:
        print(f"O Crash conseguiu livrar as Ilhas Wumpa das mãos dos vilões!!!")