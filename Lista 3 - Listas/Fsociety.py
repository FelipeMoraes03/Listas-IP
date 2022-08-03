key = input()
lista_key = key.split(" ")
mensagem_criptografada = input()
lista_mensagem = mensagem_criptografada.split(" ")
letra_inicial = input()

letra_adicionada = letra_inicial
mensagem_final = ""
indice_letra_adicionada = lista_key.index(letra_inicial)

for caracter in lista_mensagem:
    if caracter == "/":
        mensagem_final += " "
    elif caracter == "R":
        mensagem_final += letra_adicionada
    else:
        indice_letra_adicionada = (int(caracter) + indice_letra_adicionada) % 26
        letra_adicionada = lista_key[indice_letra_adicionada]
        mensagem_final += letra_adicionada

print(mensagem_final)