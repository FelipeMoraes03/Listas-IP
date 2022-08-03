musica1 = str(input())
musica2 = str(input())
musica3 = str(input())
musica4 = str(input())
musica5 = str(input())

ps = str("pelados em santos")
vv = str("vira-vira")
rg = str("robocop gay")
num1406 = str("1406")
ma = str("mundo animal")

if (musica1 == ps) or (musica2 == ps) or (musica3 == ps) or (musica4 == ps) or (musica5 == ps):
    x = 1
else:
    x = 0

if (musica1 == vv) or (musica2 == vv) or (musica3 == vv) or (musica4 == vv) or (musica5 == vv):
    y = 1
else:
    y = 0

if (musica1 == rg) or (musica2 == rg) or (musica3 == rg) or (musica4 == rg) or (musica5 == rg):
    z = 1
else:
    z = 0

if (musica1 == num1406) or (musica2 == num1406) or (musica3 == num1406) or (musica4 == num1406) or (musica5 == num1406):
    w = 1
else:
    w = 0

if (musica1 == ma) or (musica2 == ma) or (musica3 == ma) or (musica4 == ma) or (musica5 == ma):
    q = 1
else:
    q = 0

if (x + y + z + w + q) == 5:
    print("Parabens voce e um genio conhecedor da musica brasileira, voce merece 5 pontos")
elif (x + y + z + w + q) == 4:
    print("Quase perfeito mano: 3 pontos")
elif (x + y + z + w + q) == 2 or (x + y + z + w + q) == 3:
    print("Ate que tu foi bem mas nao chegou la: 1 ponto")
else:
    print("Errou feio, errou rude: 0 pontos")
