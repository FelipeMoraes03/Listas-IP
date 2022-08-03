frase1 = str(input())
frase2 = str(input())
frase3 = str(input())
frase4 = str(input())

incrivel = str("Sua apresentacao foi incrivel!")
potencial = str("Voce errou algumas notas, mas tem potencial")
dor = str("Sua performance me deu dor de cabeca")

#Jurado 1:
if (frase1 == incrivel):
    x = float(200)
elif (frase1 == potencial):
    x = float(0)
else:
    x = float(0)

#Jurado 2:
if (frase2 == incrivel):
    y = float(x + 200)
elif (frase2 == potencial):
    y = float(x + x**(1/2))
else:
    if (x > 100):
        y = float(x - 100)
    else:
        y = float(0)

#Jurado 3:
if (frase3 == incrivel):
    z = float(y + 200)
elif (frase3 == potencial):
    z = float(y + y**(1/2))
else:
    if (y > 100):
        z = float(y - 100)
    else:
        z = float(0)

#Jurado 4:
if (frase4 == incrivel):
    w = float(z + 200)
elif (frase4 == potencial):
    w = float(z + z**(1/2))
else:
    if (z > 100):
        w = float(z - 100)
    else:
        w = float(0)

#Resultado:
if (w > 150):
    print(f"Parabens! Voce atingiu a pontuacao de {w:.2f} e passou para a proxima fase!")
elif (w >= 100) and (w <= 150):
    print("Foi por pouco! Voce tem que ajustar algumas notas para alcancar a pontuacao necessaria")
else:
    print("A area musical nao foi feita para voce!")
