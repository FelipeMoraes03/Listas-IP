nome_surfista_1 = input()
nome_surfista_2 = input()
nome_surfista_3 = input()

nacionalidade_surfista_1 = input()
nacionalidade_surfista_2 = input()
nacionalidade_surfista_3 = input()

pontuacao1_surfista1 = 0
pontuacao1_surfista2 = 0
pontuacao1_surfista3 = 0

soma_surfista1 = 0
soma_surfista2 = 0
soma_surfista3 = 0

numero_fases = int(input())

for i in range(numero_fases):
    pontuacao1_surfista1 = float(input())
    pontuacao1_surfista2 = float(input())
    pontuacao1_surfista3 = float(input())

    soma_surfista1 += pontuacao1_surfista1
    soma_surfista2 += pontuacao1_surfista2
    soma_surfista3 += pontuacao1_surfista3

if soma_surfista1 >= soma_surfista2 and soma_surfista1 >= soma_surfista3:
    if nacionalidade_surfista_1 == "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_1}! E do Brasil!")
    elif nacionalidade_surfista_1 != "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_1}!")
elif soma_surfista2 >= soma_surfista3:
    if nacionalidade_surfista_2 == "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_2}! E do Brasil!")
    elif nacionalidade_surfista_2 != "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_2}!")
else:
    if nacionalidade_surfista_3 == "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_3}! E do Brasil!")
    elif nacionalidade_surfista_3 != "Brasil":
        print(f"O vencedor da medalha de ouro de surf e {nome_surfista_3}!")
