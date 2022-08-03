tempo_decorrido = 0
qnt_moedas = 10
qnt_jogos = 0

def surfe_cacamba():
    global qnt_moedas
    global tempo_decorrido

    qnt_moedas += (qnt_moedas + tempo_decorrido) // 2
    tempo_decorrido += 20

    print(f"O pinguim acabou de concluir o jogo Surfe na Caçamba e agora possui {qnt_moedas} moedas.")

def pescaria_gelo():
    global qnt_moedas
    global tempo_decorrido

    if qnt_moedas % 2 == 0: #QUANTIDADE DE MOEDAS É PAR
        qnt_moedas += (qnt_moedas % 7) * 6
    else: #QUANTIDADE DE MOEDAS É ÍMPAR
        qnt_moedas += (qnt_moedas % 7) ** 2

    tempo_decorrido += 30

    print(f"O pinguim acabou de concluir o jogo Pescaria no Gelo e agora possui {qnt_moedas} moedas.")

def concurso_danca():
    global qnt_moedas
    global tempo_decorrido

    if qnt_moedas % 10 == 0: #QUANTIDADE DE MOEDAS É MÚLTIPLO DE 10
        qnt_moedas += 5
    else: #QUANTIDADE DE MOEDAS NÃO É MÚLTIPLO DE 10
        qnt_moedas += 10 - (qnt_moedas % 10)

    tempo_decorrido += 15

    print(f"O pinguim acabou de concluir o jogo Concurso de Dança e agora possui {qnt_moedas} moedas.")

def aquagrabber():
    global qnt_moedas
    global tempo_decorrido

    #SOMA DOS DÍGITOS DA QUANTIDADE DE MOEDAS:
    moedas_ganhas = str(qnt_moedas)
    lista = list(moedas_ganhas)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    moedas_ganhas = sum(lista)

    qnt_moedas += moedas_ganhas

    tempo_decorrido += 50

    print(f"O pinguim acabou de concluir o jogo Aquagrabber e agora possui {qnt_moedas} moedas.")

while tempo_decorrido < 120:
    jogo = input()
    qnt_jogos += 1

    if jogo == "Surfe":
        surfe_cacamba()
    elif jogo == "Pescaria":
        pescaria_gelo()
    elif jogo == "Danca":
        concurso_danca()
    elif jogo == "Aqua":
        aquagrabber()

print(f"\nParabens! Você terminou o Circuito Pinguim, participando de {qnt_jogos}\
 jogos e acumulando a quantia de {qnt_moedas} moedas.")