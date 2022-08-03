pontos_djoko = 0
pontos_federer = 0
diferenca_pontos = 0

while pontos_djoko < 4 and pontos_federer < 4:
    ponto_atual = input()
    if ponto_atual == "djoko":
        pontos_djoko += 1
    elif ponto_atual == "federer":
        pontos_federer += 1

    if pontos_djoko >= pontos_federer:
        diferenca_pontos = pontos_djoko - pontos_federer
    else:
        diferenca_pontos = pontos_federer - pontos_djoko

if diferenca_pontos < 2:
    while diferenca_pontos < 2:
        ponto_atual = input()
        if ponto_atual == "djoko":
            pontos_djoko += 1
        elif ponto_atual == "federer":
            pontos_federer += 1

        if pontos_djoko >= pontos_federer:
            diferenca_pontos = pontos_djoko - pontos_federer
        else:
            diferenca_pontos = pontos_federer - pontos_djoko

if pontos_djoko > pontos_federer:
    print(f"Djokovic ganhou o game com a pontuacao de {pontos_djoko} a {pontos_federer}!")
else:
    print(f"Roger federer ganhou o game com a pontuacao de {pontos_federer} a {pontos_djoko}!")