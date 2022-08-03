energia_competidor1 = int(input())
peso_competidor1 = int(input())
energia_competidor2 = int(input())
peso_competidor2 = int(input())
energia_competidor3 = int(input())
peso_competidor3 = int(input())

rodadas = 3

#COMPETIDOR_x = True => ESTÁ ACORDADO
#COMPETIDOR_x = False => ESTÁ DESMAIADO
competidor_1 = True
competidor_2 = True
competidor_3 = True

for i in range(rodadas):
    levantamento_competidor1 = int(input())
    if competidor_1 == True:
        energia_competidor1 -= levantamento_competidor1 / peso_competidor1
    if energia_competidor1 <= 0 and competidor_1 == True:
        print("O competidor 1, desmaiou")
        competidor_1 = False

    levantamento_competidor2 = int(input())
    if competidor_2 == True:
        energia_competidor2 -= levantamento_competidor2 / peso_competidor2
    if energia_competidor2 <= 0 and competidor_2 == True:
        print("O competidor 2, desmaiou")
        competidor_2 = False

    levantamento_competidor3 = int(input())
    if competidor_3 == True:
        energia_competidor3 -= levantamento_competidor3 / peso_competidor3
    if energia_competidor3 <= 0 and competidor_3 == True:
        print("O competidor 3, desmaiou")
        competidor_3 = False

if competidor_1 == True:
    if competidor_2 == True:
        if competidor_3 == True:
            if energia_competidor1 <= energia_competidor2 and energia_competidor1 <= energia_competidor3:
                print("O vencedor foi o competidor 1")
            elif energia_competidor2 <= energia_competidor3:
                print("O vencedor foi o competidor 2")
            else:
                print("O vencedor foi o competidor 3")
        elif competidor_3 == False:
            if energia_competidor1 <= energia_competidor2:
                print("O vencedor foi o competidor 1")
            else:
                print("O vencedor foi o competidor 2")
    elif competidor_2 == False:
        if competidor_3 == True:
            if energia_competidor1 <= energia_competidor3:
                print("O vencedor foi o competidor 1")
            else:
                print("O vencedor foi o competidor 3")
        elif competidor_3 == False:
            print("O vencedor foi o competidor 1")
elif competidor_1 == False:
    if competidor_2 == True:
        if competidor_3 == True:
            if energia_competidor2 <= energia_competidor3:
                print("O vencedor foi o competidor 2")
            else:
                print("O vencedor foi o competidor 3")
        elif competidor_3 == False:
            print("O vencedor foi o competidor 2")
    elif competidor_2 == False:
        if competidor_3 == True:
            print("O vencedor foi o competidor 3")
        elif competidor_3 == False:
            print("Todos os competidores desmaiaram")