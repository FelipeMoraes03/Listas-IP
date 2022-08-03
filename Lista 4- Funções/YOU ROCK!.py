lista_linhas = []
continuar = True
pontuacao_total = 0

def identificar_linha(linha):
    pontuacao_linha = 0
    if linha == "0 0 0 0 0":
        continuar = False
    else:
        lista_linhas.append(teclas)
        if teclas == "X X X X X":
            print("Note streak!")
            pontuacao_linha = 20
        continuar = True

    return [continuar, pontuacao_linha]

def comparar_elementos(elemento, elemento_anterior=None):
    if elemento == "X":
        pontuacao_tecla = 5
        if elemento_anterior == "X":
            pontuacao_tecla = 10
    else:
        pontuacao_tecla = 0

    return pontuacao_tecla

while continuar:
    teclas = input()
    continuar, pontuacao_linha = identificar_linha(teclas)
    pontuacao_total += pontuacao_linha

for linha in lista_linhas:
    tecla1, tecla2, tecla3, tecla4, tecla5 = linha.split(" ")
    lista_teclas = [tecla1, tecla2, tecla3, tecla4, tecla5]

    for index in range(len(lista_teclas)):
        if index == 0: #NÃO EXISTE ELEMENTO ANTERIOR
            pontuacao_tecla = comparar_elementos(lista_teclas[index])
        else: #EXISTE ELEMENTO ANTERIOR
            pontuacao_tecla = comparar_elementos(lista_teclas[index], lista_teclas[index - 1])

        pontuacao_total += pontuacao_tecla

if pontuacao_total < 15:
    print("Song failed!")
elif pontuacao_total < 50:
    print("Nada bom, amigo...")
elif pontuacao_total < 70:
    print("Wow, rock and roll na veia!")
elif pontuacao_total <= 100:
    print("YOU ROCK!!!")
else:
    print("TEMOS UMA NOVA LENDA DO ROCK!")

print(f"Sua pontuação foi de {pontuacao_total} pontos")