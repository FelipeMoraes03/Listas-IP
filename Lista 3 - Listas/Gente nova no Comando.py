lista_votos = []
lista_candidatos = [] # APENAS OS SHELBY
lista_votos_por_candidato = [] # NUMERO DE VOTOS DE CADA SHELBY
maior_numero_votos = 0
segundo_maior_numero_votos = 0

numero_eleitores = int(input())

for _ in range(numero_eleitores):
    geral = input()
    eleitor, votos = geral.split(": ")
    nome, sobrenome = votos.split(" ")
    lista_votos.append(votos)

    if votos not in lista_candidatos and sobrenome == "Shelby":
        lista_candidatos.append(votos)

# CONTAR QUANTOS VOTOS CADA SHELBY ESTÁ RECEBENDO:
for candidato in lista_candidatos:
    votos_por_candidato = lista_votos.count(candidato)
    lista_votos_por_candidato.append(votos_por_candidato)

# VERIFICAR QUEM É O MAIS VOTADO E QUEM É O SEGUNDO MAIS VOTADO:
for candidato in lista_votos_por_candidato:
    indice = lista_votos_por_candidato.index(candidato)
    numero_votos = lista_votos_por_candidato[indice]
    if numero_votos > maior_numero_votos:
        segundo_maior_numero_votos = maior_numero_votos
        maior_numero_votos = numero_votos
    elif numero_votos > segundo_maior_numero_votos:
        segundo_maior_numero_votos = numero_votos

# NENHUM SHELBY RECEBEU VOTOS:
if len(lista_candidatos) == 0:
    print("Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!")

# SHELBYS RECEBERAM VOTOS:
else:
    copia_lista_candidatos = lista_candidatos.copy()
    indice_mais_votado = lista_votos_por_candidato.index(maior_numero_votos)
    candidato_mais_votado = copia_lista_candidatos[indice_mais_votado]
    copia_lista_candidatos.pop(indice_mais_votado)
    lista_votos_por_candidato.pop(indice_mais_votado)
    porcentagem_mais_votado = 100 * maior_numero_votos / numero_eleitores

    # APENAS 1 SHELBY RECEBEU VOTOS:
    if len(lista_candidatos) == 1:
        if porcentagem_mais_votado > 50:
            if candidato_mais_votado == "Thomas Shelby":
                print(f"{candidato_mais_votado} ganhou a eleição com {porcentagem_mais_votado:.2f}% dos votos e continuara sendo o líder dos Peaky Blinders!!!")
            elif candidato_mais_votado != "Thomas Shelby":
                print(f"Assumindo o lugar de Tommy, {candidato_mais_votado} agora é o novo líder da gangue vencendo a eleição com {porcentagem_mais_votado:0.2f}% dos votos!")
        elif porcentagem_mais_votado <= 50:
            print("Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!")

    # MAIS DE UM SHELBY RECEBEU VOTOS:
    elif len(lista_candidatos) > 1:
        indice_segundo_mais_votado = lista_votos_por_candidato.index(segundo_maior_numero_votos)
        segundo_candidato_mais_votado = copia_lista_candidatos[indice_segundo_mais_votado]
        porcentagem_segundo_mais_votado = 100 * segundo_maior_numero_votos / numero_eleitores

        # SHELBY MAIS VOTADO RECEBEU MAIS DE 50% DOS VOTOS:
        if porcentagem_mais_votado > 50:
            if candidato_mais_votado == "Thomas Shelby":
                print(f"{candidato_mais_votado} ganhou a eleição com {porcentagem_mais_votado:.2f}% dos votos e continuara sendo o líder dos Peaky Blinders!!!")
            elif candidato_mais_votado != "Thomas Shelby":
                print(f"Assumindo o lugar de Tommy, {candidato_mais_votado} agora é o novo líder da gangue vencendo a eleição com {porcentagem_mais_votado:.2f}% dos votos!")

        # SHELBY MAIS VOTADO RECEBEU MENOS OU IGUAL A 50% DOS VOTOS:
        elif porcentagem_mais_votado <= 50:
            if candidato_mais_votado == "Thomas Shelby" or segundo_candidato_mais_votado == "Thomas Shelby":
                print(f"Precisaremos ter uma segunda rodada entre os membros {candidato_mais_votado} e {segundo_candidato_mais_votado}, "
                      f"que tiveram respectivamente {porcentagem_mais_votado:.2f}% e {porcentagem_segundo_mais_votado:.2f}% dos votos, Tommy ainda está na disputa.")
            elif candidato_mais_votado != "Thomas Shelby" and segundo_candidato_mais_votado != "Thomas Shelby":
                print(f"Precisaremos ter uma segunda rodada entre os membros {candidato_mais_votado} e {segundo_candidato_mais_votado}, "
                      f"que tiveram respectivamente {porcentagem_mais_votado:.2f}% e {porcentagem_segundo_mais_votado:.2f}% dos votos, teremos um novo líder!")