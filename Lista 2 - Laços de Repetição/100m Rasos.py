numero_baterias = int(input())

soma_atleta1 = 0
soma_atleta2 = 0
soma_atleta3 = 0
soma_atleta4 = 0
soma_atleta5 = 0

RECORDE_MUNDIAL = 9.58

for i in range(numero_baterias):
    tempo_atleta1 = float(input())
    tempo_atleta2 = float(input())
    tempo_atleta3 = float(input())
    tempo_atleta4 = float(input())
    tempo_atleta5 = float(input())

    soma_atleta1 += tempo_atleta1
    soma_atleta2 += tempo_atleta2
    soma_atleta3 += tempo_atleta3
    soma_atleta4 += tempo_atleta4
    soma_atleta5 += tempo_atleta5

    if tempo_atleta1 < RECORDE_MUNDIAL:
        print(f"O atleta 1 bateu o recorde mundial com o tempo: {tempo_atleta1}")
    if tempo_atleta2 < RECORDE_MUNDIAL:
        print(f"O atleta 2 bateu o recorde mundial com o tempo: {tempo_atleta2}")
    if tempo_atleta3 < RECORDE_MUNDIAL:
        print(f"O atleta 3 bateu o recorde mundial com o tempo: {tempo_atleta3}")
    if tempo_atleta4 < RECORDE_MUNDIAL:
        print(f"O atleta 4 bateu o recorde mundial com o tempo: {tempo_atleta4}")
    if tempo_atleta5 < RECORDE_MUNDIAL:
        print(f"O atleta 5 bateu o recorde mundial com o tempo: {tempo_atleta5}")


if soma_atleta1 <= soma_atleta2 and soma_atleta1 <= soma_atleta3 and soma_atleta1 <= soma_atleta4 and soma_atleta1 <= soma_atleta5:
    print("Vencedor com o menor tempo somando todas as baterias foi: Atleta 1")
elif soma_atleta2 <= soma_atleta3 and soma_atleta2 <= soma_atleta4 and soma_atleta2 <= soma_atleta5:
    print("Vencedor com o menor tempo somando todas as baterias foi: Atleta 2")
elif soma_atleta3 <= soma_atleta4 and soma_atleta3 <= soma_atleta5:
    print("Vencedor com o menor tempo somando todas as baterias foi: Atleta 3")
elif soma_atleta4 <= soma_atleta5:
    print("Vencedor com o menor tempo somando todas as baterias foi: Atleta 4")
else:
    print("Vencedor com o menor tempo somando todas as baterias foi: Atleta 5")