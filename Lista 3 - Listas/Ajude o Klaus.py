sobrenaturais = ['Damon Salvatore', 'Stefan Salvatore', 'Caroline Forbes', 'Elena Gilbert', 'Bonnie Bennett', 'Kai Parker', 'Katherine Pierce']
sobrenaturais_encontrados = []

try:
    while True:
        seres = input()
        if seres in sobrenaturais and seres not in sobrenaturais_encontrados:
            sobrenaturais_encontrados.append(seres)
except EOFError:
    if len(sobrenaturais_encontrados) == 0:
        print("Nenhum sobrenatural foi encontrado :/")
    else:
        print("Os sobrenaturais encontrados foram:\n")
        for i in range(len(sobrenaturais_encontrados)):
                print(sobrenaturais_encontrados[i])
        print("\nAgora Klaus, Rebekah, Elijah, Kol e toda a família original sabem bem em quem podem confiar e quem devem matar.")