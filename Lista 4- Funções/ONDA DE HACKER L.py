id_jogador, _ = input().split("id")
print(f"Analisando ID: {id_jogador}")

casas_id = list(id_jogador)
casas_id.reverse()

indice = 0
soma_total = 0
def somatorio():
    if indice % 2 == 1:
        soma = int(casa)

    elif indice % 2 == 0:
        numero = int(casa) * 2
        if numero >= 10:
            unidade = numero % 10
            dezena = int(numero / 10)
            numero = unidade + dezena
        soma = numero

    return soma

for casa in casas_id:
    indice += 1
    soma_total += somatorio()

if soma_total % 10 == 0:
    print("Situacao: Jogador limpo")
else:
    print("Situacao: XITADO ATE OS DENTES")
