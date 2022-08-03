def testar_anagrama(dic: dict) -> bool:
    #TESTA SE PRA CADA LETRA NA SENHA TEM UMA CORRESPONDENTE NA CHAVE:
    for letra in dic["senha"]:
        if letra in dic["chave"]:
            dic["chave"].remove(letra)
        
        #SE HÁ ALGUMA LETRA NA SENHA QUE NÃO ESTÁ NA CHAVE, NÃO É ANAGRAMA:
        else:
            return False
    
    #SE ALGUMA LETRA DA CHAVE NÃO FOR ASSOCIADA A NENHUMA LETRA DA SENHA, NÃO É UM ANAGRAMA:
    if len(dic["chave"]) > 0:
        return False

    #SE CADA LETRA DA CHAVE FOR ASSOCIADA A UMA LETRA DA SENHA, É UM ANAGRAMA:
    else:
        return True

dic = {}
dic["chave"] = list(input().lower())
dic["senha"] = list(input().lower())

teste_anagrama = testar_anagrama(dic)

if teste_anagrama == True:
    print("Acesso liberado. Bem vindo Senhor Stark.")
else:
    print("Acesso negado.")