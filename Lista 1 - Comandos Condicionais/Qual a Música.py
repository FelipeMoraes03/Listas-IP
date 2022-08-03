genero = str(input())
nacional = str(input())
decada = str(input())

rock = ("Rock")
samba = ("Samba")
pop = ("Pop")

s = ("Sim")
n = ("Nao")

ses = ("60")
set = ("70")
oit = ("80")
nov = ("90")

#Rock
if(genero == rock):
    if(nacional == s):
        if(decada == set):
            print("A musica que voce esta procurando eh: O Pirata")
        elif(decada == oit):
            print("A musica que voce esta procurando eh: Indios")
        else:
            print("Musica nao encontrada")
    elif(nacional == n):
        if(decada == set):
            print("A musica que voce esta procurando eh: Bohemian Rapsody")
        else:
            print("Musica nao encontrada")
#Samba
elif(genero == samba):
    if(nacional == s):
        if(decada == ses):
            print("A musica que voce esta procurando eh: Mas que Nada")
        elif(decada == set):
            print("A musica que voce esta procurando eh: Apesar de Voce")
        elif(decada == oit):
            print("A musica que voce esta procurando eh: Conselho")
        else:
            print("Musica nao encontrada")
    else:
        print("Musica nao encontrada")
#Pop
elif(genero == pop):
    if(nacional == s):
        if(decada == nov):
            print("A musica que voce esta procurando eh: Anna Julia")
        else:
            print("Musica nao encontrada")
    elif(nacional == n):
        if(decada == oit):
            print("A musica que voce esta procurando eh: Take On Me")
        elif(decada == nov):
            print("A musica que voce esta procurando eh: Candle in the Wind 1997")
        else:
            print("Musica nao encontrada")
    else:
        print("Musica nao encontrada")

#Nenhuma:
else:
    print("Musica nao encontrada")
