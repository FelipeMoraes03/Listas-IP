alfabeto = ["a", "b", "c", "d", "e", "f", "g" ,"h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" ,"z"]

def fibonacci(num: int) -> int:
    numero_fibonacci = 0
    if num == 1:
        numero_fibonacci = 1
    elif num >= 2:
        var = 0
        numero_fibonacci = 1
        for _ in range(1, num):
            numero_fibonacci_anterior = var
            var = numero_fibonacci
            numero_fibonacci += numero_fibonacci_anterior
    return numero_fibonacci

numero_frases = int(input())

for _ in range(numero_frases):
    mensagem_criptografada = ""

    chave = int(input())

    frase = input()
    frase = frase.split(" ")
    frase = "".join(frase)
    frase = frase.lower()

    for letra in frase:
        indice_letra_inicial = alfabeto.index(letra)
        indice = (indice_letra_inicial + fibonacci(chave)) % 26

        mensagem_criptografada += alfabeto[indice]
        chave += 1

    print(mensagem_criptografada)