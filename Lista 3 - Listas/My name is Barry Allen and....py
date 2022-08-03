velocistas_posicoes = []
posicoes = []
ordenados = []

for _ in range(5):
    velocista_posicao = input()
    velocistas_posicoes.append(velocista_posicao)

    velocista, posicao = velocista_posicao.split(" - ")
    posicoes.append(posicao)

print("Velocista - Posicao\n")

for i in posicoes: # Procurar o 1º colocado
    if i == "1":
        index = posicoes.index(i)
        ordenados.append(velocistas_posicoes[index])
for i in posicoes: # Procurar o 2º colocado
    if i == "2":
        index = posicoes.index(i)
        ordenados.append(velocistas_posicoes[index])
for i in posicoes: # Procurar o 3º colocado
    if i == "3":
        index = posicoes.index(i)
        ordenados.append(velocistas_posicoes[index])
for i in posicoes: # Procurar o 4º colocado
    if i == "4":
        index = posicoes.index(i)
        ordenados.append(velocistas_posicoes[index])
for i in posicoes: # Procurar o 5º colocado
    if i == "5":
        index = posicoes.index(i)
        ordenados.append(velocistas_posicoes[index])

for k in ordenados:
    print(k)