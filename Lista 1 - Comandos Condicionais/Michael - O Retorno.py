#Inputs:
musica = str(input())
seguidores_michael = int(input())
seguidores_raffa = int(input())
frase1 = str(input())
frase2 = str(input())
frase3 = str(input())

seguidores_esperados = int(seguidores_raffa + seguidores_michael)

#Possibilidades de Frases:
gang = ("Gang Gang Bro!")
hih = ("Hihiiiii UuHuu, 777 Bro!")
ayo = ("Ayouwoki, ayouwoki, ayouwoki")

#Todas frases diferentes:
if(frase1 != frase2) and (frase1 != frase3):
    if(frase1 == gang) or (frase2 == gang) or (frase3 == gang):
        seguidores_raffa = seguidores_raffa * 1.25
    if(frase1 == hih) or (frase2 == hih) or (frase3 == hih):
        seguidores_michael = seguidores_michael * 1.15
        seguidores_raffa = seguidores_raffa * 1.2
    if(frase1 == ayo) or (frase2 == ayo) or (frase3 == ayo):
        seguidores_michael = seguidores_michael * 0.7
        seguidores_raffa = seguidores_raffa * 0.75

#Todas frases iguais:
elif(frase1 == frase2) and (frase1 == frase3):
    if(frase1 == gang):
        seguidores_raffa = seguidores_raffa * (1.25 ** 3)
    elif(frase1 == hih):
        seguidores_michael = seguidores_michael * (1.15 ** 3)
        seguidores_raffa = seguidores_raffa * (1.2 ** 3)
    elif(frase1 == ayo):
        seguidores_michael = seguidores_michael * (0.7 ** 3)
        seguidores_raffa = seguidores_raffa * (0.75 ** 3)

#Frase1 igual a Frase2 e diferente da Frase3:
elif(frase1 == frase2) and (frase1 != frase3):
    if(frase1 == gang):
        seguidores_raffa = seguidores_raffa * (1.25 ** 2)
    elif(frase1 == hih):
        seguidores_michael = seguidores_michael * (1.15 ** 2)
        seguidores_raffa = seguidores_raffa * (1.2 ** 2)
    elif(frase1 == ayo):
        seguidores_michael = seguidores_michael * (0.7 ** 2)
        seguidores_raffa = seguidores_raffa * (0.75 ** 2)
    if(frase3 == gang):
        seguidores_raffa = seguidores_raffa * 1.25
    elif(frase3 == hih):
        seguidores_michael = seguidores_michael * 1.15
        seguidores_raffa = seguidores_raffa * 1.2
    elif(frase3 == ayo):
        seguidores_michael = seguidores_michael * 0.7
        seguidores_raffa = seguidores_raffa * 0.75

#Frase1 diferente da Frase2 e igual a Frase3:
elif(frase1 != frase2) and (frase1 == frase3):
    if(frase1 == gang):
        seguidores_raffa = seguidores_raffa * (1.25 ** 2)
    elif(frase1 == hih):
        seguidores_michael = seguidores_michael * (1.15 ** 2)
        seguidores_raffa = seguidores_raffa * (1.2 ** 2)
    elif(frase1 == ayo):
        seguidores_michael = seguidores_michael * (0.7 ** 2)
        seguidores_raffa = seguidores_raffa * (0.75 ** 2)
    if(frase2 == gang):
        seguidores_raffa = seguidores_raffa * 1.25
    elif(frase2 == hih):
        seguidores_michael = seguidores_michael * 1.15
        seguidores_raffa = seguidores_raffa * 1.2
    elif(frase2 == ayo):
        seguidores_michael = seguidores_michael * 0.7
        seguidores_raffa = seguidores_raffa * 0.75

#Frase1 difetente da Frase2 e Frase2 igual a Frase3:
elif(frase1 != frase2) and (frase2 == frase3):
    if(frase1 == gang):
        seguidores_raffa = seguidores_raffa * 1.25
    elif(frase1 == hih):
        seguidores_michael = seguidores_michael * 1.15
        seguidores_raffa = seguidores_raffa * 1.2
    elif(frase1 == ayo):
        seguidores_michael = seguidores_michael * 0.7
        seguidores_raffa = seguidores_raffa * 0.75
    if(frase2 == gang):
        seguidores_raffa = seguidores_raffa * (1.25 ** 2)
    elif(frase2 == hih):
        seguidores_michael = seguidores_michael * (1.15 ** 2)
        seguidores_raffa = seguidores_raffa * (1.2 ** 2)
    elif(frase2 == ayo):
        seguidores_michael = seguidores_michael * (0.7 ** 2)
        seguidores_raffa = seguidores_raffa * (0.75 ** 2)

seguidores_reais = int(seguidores_raffa + seguidores_michael)
resultado = float(seguidores_reais / seguidores_esperados)

#Resultado:
print("Então Michael, eu trouxe os seguintes resultados da música...")
print(f"Nome da Música: {musica.upper()}")
print(f"Número de Seguidores Esperados: {seguidores_esperados}")
print(f"Número de Seguidores Calculados: {seguidores_reais}")
print(f"Resultado: {(resultado * 100):.2f}%")

if(seguidores_reais > seguidores_esperados):
    print("E felizmente... BROOO! faz sol! Camisa do Rusbé vai vender!")
else:
    print("Rockstar e fé em Deus bro! Que vocês irão pensar em frases melhores...")