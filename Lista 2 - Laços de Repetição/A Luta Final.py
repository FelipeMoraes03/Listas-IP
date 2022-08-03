vida_logan = 100
vida_eu = 100
ciclo = 0

while vida_eu > 0 and vida_logan > 0:
    ciclo += 1
    ataque = int(input())
    defesa = int(input())

    if ciclo % 2 == 1:
        if ataque > defesa:
            if ataque - defesa <= 20:
                vida_eu -= ataque - defesa
            else:
                vida_eu -= (ataque - defesa) * 1.5
        else:
            if defesa - ataque > 20:
                vida_logan -= defesa - ataque
    else:
        if ataque > defesa:
            if ataque - defesa <= 20:
                vida_logan -= ataque - defesa
            else:
                vida_logan -= (ataque - defesa) * 1.5
        else:
            if defesa - ataque > 20:
                vida_eu -= defesa - ataque

if vida_eu <= 0:
    print("Infelizmente nao foi dessa vez, Logan Paul leva a vitoria.")
elif vida_logan <= 0:
    print("Apos longos anos de esforco voce finalmente conseguiu, e ouro pro Brasil!")
