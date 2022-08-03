estilo = int(input())
musica = int(input())

if(estilo == 1):
    print("Você escolheu o genero: Rock")
    print("Escolha a musica")
    if(musica == 1):
        print("Tocando: In the end - Linkin Park")
    elif(musica == 2):
        print("Tocando: Californication - Red Hot Chilli Peppers")
    else:
        print("Tocando: Yellow - Coldplay")
elif(estilo == 2):
    print("Você escolheu o genero: Eletronica")
    print("Escolha a musica")
    if(musica == 1):
        print("Tocando: Big Jet Plane - Alok & Mathieu")
    elif(musica == 2):
        print("Tocando: Everyday - Marshmello & Logic")
    else:
        print("Tocando: On & On - Cartoon")
else:
    print("Você escolheu o genero: Hip-hop/Rap")
    print("Escolha a musica")
    if(musica == 1):
        print("Tocando: Congratulations - Post Malone")
    elif(musica == 2):
        print("Tocando: HIGHEST IN THE ROOM - Travis Scott")
    else:
        print("Tocando: Devil Eyes - Hippie Sabotage")