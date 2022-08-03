import string

def tornar_minusculas(codigo: str, index_codigo: int = 0, codigo_minuscula: str = "") -> str:
    alfabeto_maiusculo = [i for i in string.ascii_uppercase]
    alfabeto_minusculo = [i for i in string.ascii_lowercase]

    if index_codigo <= len(codigo) - 1:
        if codigo[index_codigo] in alfabeto_maiusculo:
            index_alfabeto = alfabeto_maiusculo.index(codigo[index_codigo])
            codigo_minuscula += alfabeto_minusculo[index_alfabeto]

        else:
            codigo_minuscula += codigo[index_codigo]

        return tornar_minusculas(codigo, index_codigo + 1, codigo_minuscula)

    else:
        return codigo_minuscula

def inverter_lista(codigo: str, index_codigo: int =  1, codigo_invertido: str = "") -> str:
    index_contrario = len(codigo) - index_codigo
    if index_contrario >= 0:
        codigo_invertido += codigo[index_contrario]
        return inverter_lista(codigo, index_codigo + 1, codigo_invertido)

    else:
        return codigo_invertido

def analisar_resultado(mensagem: str) -> str:
    if mensagem == "amigo" or mensagem == "ogima" or mensagem == "mellon" or mensagem == "nollem":
        resultado = "Desvendamos o misterio e a porta se abriu!"
    else:
        resultado = "Acho que ainda nao acertamos, Gandalf, o que faremos agora?"
    
    return resultado

codigo = input()
codigo = tornar_minusculas(codigo)
mensagem = inverter_lista(codigo)

resultado = analisar_resultado(mensagem)

print(mensagem)
print(resultado)