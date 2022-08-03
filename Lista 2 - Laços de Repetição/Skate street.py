numero_voltas = int(input())

jurado_1 = 0
jurado_2 = 0
jurado_3 = 0
jurado_4 = 0
jurado_5 = 0
soma_jurados = 0
pontuacao_final = 0

for i in range(numero_voltas):
    jurado_1 = int(input())
    jurado_2 = int(input())
    jurado_3 = int(input())
    jurado_4 = int(input())
    jurado_5 = int(input())
    soma_jurados = jurado_1 + jurado_2 + jurado_3 + jurado_4 + jurado_5

    print(f"A pontuacao na volta {i + 1} foi de {soma_jurados} pontos!")

    if soma_jurados > pontuacao_final:
        pontuacao_final = soma_jurados

print(f"A pontuacao final de Rayssa foi de {pontuacao_final} pontos!")
