#POSSIBILIDADE DE MOVIMENTOS:
direita = "direita"
esquerda = "esquerda"
cima = "cima"
baixo = "baixo"

movimento_1 = str(input())

#MOVIMENTO 1 DIFERENTE DO ESPERADO:
if(movimento_1 != direita and movimento_1 != esquerda and movimento_1 != cima and movimento_1 != baixo):
    print("O jogador nao fez nenhuma entrada valida")
else:
    movimento_2 = str(input())

# MOVIMENTO 2 DIFERENTE DO ESPERADO:
    if (movimento_2 != direita and movimento_2 != esquerda and movimento_2 != cima and movimento_2 != baixo):
        print("O jogador fez 1 movimento(s) e tentou uma entrada invalida")
    elif(movimento_1 == movimento_2) or (movimento_1 == direita and movimento_2 == esquerda) or (movimento_1 == esquerda and movimento_2 == direita) or (movimento_1 == cima and movimento_2 == baixo) or (movimento_1 == baixo and movimento_2 == cima):
        print("O jogador fez somente 1 movimento(s)")
    else:
        movimento_3 = str(input())

#MOVIMENTO 3 DIFERENTE DO ESPERADO:
        if (movimento_3 != direita and movimento_3 != esquerda and movimento_3 != cima and movimento_3 != baixo):
            print("O jogador fez 2 movimento(s) e tentou uma entrada invalida")
        elif(movimento_2 == movimento_3) or (movimento_2 == direita and movimento_3 == esquerda) or (movimento_2 == esquerda and movimento_3 == direita) or (movimento_2 == cima and movimento_3 == baixo) or (movimento_2 == baixo and movimento_3 == cima):
            print("O jogador fez somente 2 movimento(s)")
        else:
            movimento_4 = str(input())

#MOVIMENTO 4 DIFERENTE DO ESPERADO:
            if (movimento_4 != direita and movimento_4 != esquerda and movimento_4 != cima and movimento_4 != baixo):
                print("O jogador fez 3 movimento(s) e tentou uma entrada invalida")
            elif(movimento_3 == movimento_4) or (movimento_3 == direita and movimento_4 == esquerda) or (movimento_3 == esquerda and movimento_4 == direita) or (movimento_3 == cima and movimento_4 == baixo) or (movimento_3 == baixo and movimento_4 == cima):
                print("O jogador fez somente 3 movimento(s)")
            else:
                movimento_5 = str(input())

#MOVIMENTO 5 DIFERENTE DO ESPERADO:
                if (movimento_5 != direita and movimento_5 != esquerda and movimento_5 != cima and movimento_5 != baixo):
                    print("O jogador fez 4 movimento(s) e tentou uma entrada invalida")
                elif(movimento_4 == movimento_5) or (movimento_4 == direita and movimento_5 == esquerda) or (movimento_4 == esquerda and movimento_5 == direita) or (movimento_4 == cima and movimento_5 == baixo) or (movimento_4 == baixo and movimento_5 == cima):
                    print("O jogador fez somente 4 movimento(s)")

#TODOS MOVIMENTOS COMO ESPERADO:
                else:
                    print("O jogador conseguiu fazer todos 5 movimentos com sucesso!")