#INPUTS:
musica_1, cantor_1, tempo_1 = str(input()).split(" - ")
musica_2, cantor_2, tempo_2 = str(input()).split(" - ")
musica_3, cantor_3, tempo_3 = str(input()).split(" - ")
musica_4, cantor_4, tempo_4 = str(input()).split(" - ")
musica_5, cantor_5, tempo_5 = str(input()).split(" - ")
musica_6, cantor_6, tempo_6 = str(input()).split(" - ")

ze = ("Ze vaqueiro")
jg = ("Joao gomes")

#TEMPOS DE ZÉ VAQUEIRO:
ze_1 = int(0)
ze_2 = int(0)
ze_3 = int(0)
ze_4 = int(0)
ze_5 = int(0)
ze_6 = int(0)

#QUANTIDADE DE MÚSICAS DE ZÉ VAQUEIRO:
z1 = int(0)
z2 = int(0)
z3 = int(0)
z4 = int(0)
z5 = int(0)
z6 = int(0)

#TEMPOS DE JOÃO GOMES:
jg_1 = int(0)
jg_2 = int(0)
jg_3 = int(0)
jg_4 = int(0)
jg_5 = int(0)
jg_6 = int(0)

#QUANTIDADE DE MÚSICAS DE JOÃO GOMES:
j1 = int(0)
j2 = int(0)
j3 = int(0)
j4 = int(0)
j5 = int(0)
j6 = int(0)

#IFS:
if(cantor_1 == ze):
    ze_1 = float(tempo_1)
    z1 = int(1)
elif(cantor_1 == jg):
    jg_1 = float(tempo_1)
    j1 = int(1)

if(cantor_2 == ze):
    ze_2 = float(tempo_2)
    z2 = int(1)
elif(cantor_2 == jg):
    jg_2 = float(tempo_2)
    j2 = int(1)

if(cantor_3 == ze):
    ze_3 = float(tempo_3)
    z3 = int(1)
elif(cantor_3 == jg):
    jg_3 = float(tempo_3)
    j3 = int(1)

if(cantor_4 == ze):
    ze_4 = float(tempo_4)
    z4 = int(1)
elif(cantor_4 == jg):
    jg_4 = float(tempo_4)
    j4 = int(1)

if(cantor_5 == ze):
    ze_5 = float(tempo_5)
    z5 = int(1)
elif(cantor_5 == jg):
    jg_5 = float(tempo_5)
    j5 = int(1)

if(cantor_6 == ze):
    ze_6 = float(tempo_6)
    z6 = int(1)
elif(cantor_6 == jg):
    jg_6 = float(tempo_6)
    j6 = int(1)

#TEMPO TOTAL E QUANTIDADE DAS MÚSICAS DE ZÉ VAQUEIRO:
tempo_total_ze = float(ze_1 + ze_2 + ze_3 + ze_4 + ze_5 + ze_6)
qt_musicas_ze = int(z1 + z2 + z3 + z4 + z5 + z6)

#TEMPO TOTAL E QUANTIDADE DAS MÚSICAS DE JOÃO GOMES:
tempo_total_jg = float(jg_1 + jg_2 + jg_3 + jg_4 + jg_5 + jg_6)
qt_musicas_jg = int(j1 + j2 + j3 + j4 + j5 + j6)

#RESULTADOS:
if (qt_musicas_ze != 0) and (qt_musicas_jg != 0):
    media_ze = tempo_total_ze / qt_musicas_ze
    media_jg = tempo_total_jg / qt_musicas_jg
    if(media_ze < media_jg):
        print("De acordo com estes dados temos um forte indicativo de que as musicas de Joao gomes sao mais longas que as de Ze vaqueiro.")
    elif (media_ze > media_jg):
        print("De acordo com estes dados temos um forte indicativo de que as musicas de Ze vaqueiro sao mais longas que as de Joao gomes.")
    elif(media_ze == media_jg):
        print("Tivemos um empate tecnico.")
else:
    print("Nao tivemos dados suficientes para chegar uma conclusao.")