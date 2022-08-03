manobra = ""
primeiro_colocado = ""
pontuacao_primeiro_colocado = 0
segundo_colocado = ""
pontuacao_segundo_colocado = 0
terceiro_colocado = ""
pontuacao_terceiro_colocado = 0

pontuacao_competidor = 0

numero_competidores = int(input())

for i in range(numero_competidores):
    nome_competidor = input()
    while manobra != "Fim":
        manobra = input()

        if manobra == "Gap":
            pontuacao_competidor += 10
        elif manobra == "Barspin":
            pontuacao_competidor += 30
        elif manobra == "Superhomem":
            pontuacao_competidor += 100
        elif manobra == "Rotacao de 360":
            pontuacao_competidor += 50
        elif manobra == "Rotacao de 720":
            pontuacao_competidor += 150
        elif manobra == "Rotacao de 1080":
            pontuacao_competidor += 400
        elif manobra == "Backflip":
            pontuacao_competidor += 250
        elif manobra == "Frontflip":
            pontuacao_competidor += 500

    manobra = ""

    if pontuacao_competidor > pontuacao_primeiro_colocado:
        terceiro_colocado = segundo_colocado
        pontuacao_terceiro_colocado = pontuacao_segundo_colocado
        segundo_colocado = primeiro_colocado
        pontuacao_segundo_colocado = pontuacao_primeiro_colocado
        primeiro_colocado = nome_competidor
        pontuacao_primeiro_colocado = pontuacao_competidor
    elif pontuacao_competidor > pontuacao_segundo_colocado:
        terceiro_colocado = segundo_colocado
        pontuacao_terceiro_colocado = pontuacao_segundo_colocado
        segundo_colocado = nome_competidor
        pontuacao_segundo_colocado = pontuacao_competidor
    elif pontuacao_competidor > pontuacao_terceiro_colocado:
        terceiro_colocado = nome_competidor
        pontuacao_terceiro_colocado = pontuacao_competidor

    pontuacao_competidor = 0

print(primeiro_colocado)
print(pontuacao_primeiro_colocado)
print(segundo_colocado)
print(pontuacao_segundo_colocado)
print(terceiro_colocado)
print(pontuacao_terceiro_colocado)