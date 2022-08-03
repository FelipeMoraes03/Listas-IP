objeto1 = str(input())
objeto2 = str(input())
objeto3 = str(input())
objeto4 = str(input())

a = str("Alicate")
cf = str("Chave de Fenda")
lant = str("Lanterna")
m = str("Martelo")

if (objeto1 == a) or (objeto2 == a) or (objeto3 == a) or (objeto4 == a):
    x = int(1)
else:
    x = 0
if (objeto1 == cf) or (objeto2 == cf) or (objeto3 == cf) or (objeto4 == cf):
    y = int(1)
else:
    y = 0
if (objeto1 == lant) or (objeto2 == lant) or (objeto3 == lant) or (objeto4 == lant):
    z = int(1)
else:
    z = 0
if (objeto1 == m) or (objeto2 == m) or (objeto3 == m) or (objeto4 == m):
    w = int(1)
else:
    w = 0

if (x + y + z + w) == 4:
    print("Tuê, encontrei tudo! Tá tudo Jóia, ficou bem BOOMZIM!!!")
elif (x + y + z + w) == 0:
    print("Tuêzin! Se a seca chegar, não vai se desanimar...")
else:
    print("Andam dizendo que o Tuê é um baiano...")
