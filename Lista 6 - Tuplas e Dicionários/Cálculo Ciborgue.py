def funcao_flash(num_inimigos: int):
    if num_inimigos <= 15:
        print("A velocidade cuida dos nossos problemas")
    else:
        print("Flash cansou de correr")

def funcao_batman(num_inimigos: int):
    if num_inimigos <= 25:
        print("Morcego rei da noite")
    else:
        print("Volte para a batcaverna")

def funcao_aquaman(num_inimigos: int):
    if num_inimigos <= 20:
        print("O tridente brandiu")
    else:
        print("Sushi de heroi")

def funcao_maravilha(num_inimigos: int):
    if num_inimigos <= 50:
        print("O laco da verdade vai estralar")
    else:
        print("Volte para casa princesa Diana")

dic_herois = {"flash": funcao_flash, "batman": funcao_batman, "aquaman": funcao_aquaman, "maravilha": funcao_maravilha}

numero_entradas = int(input())
for i in range(numero_entradas):
    heroi, inimigos = input().split()
    inimigos = int(inimigos)

    dic_herois[heroi](inimigos)