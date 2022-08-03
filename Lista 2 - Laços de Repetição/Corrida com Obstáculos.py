numero_voltas = int(input())
tempo_restante = numero_voltas * 72
teste_2_erros_consecultivos = 0  # VERIFICAR SE VÃO OCORRER 2 ERROS CONSECULTIVOS
teste_5_erros_consecultivos = 0  # VERIFICAR SE VÃO OCORRER 5 ERROS CONSECULTIVOS
erros_total = 0

for obstaculo in range(10 * numero_voltas):
    tentativa = input()
    if tentativa == "erro":
        tempo_restante -= 9
        teste_2_erros_consecultivos += 1
        teste_5_erros_consecultivos += 1
        erros_total += 1
    elif tentativa == "acerto":
        tempo_restante -= 5
        teste_2_erros_consecultivos = 0
        teste_5_erros_consecultivos = 0

    if teste_2_erros_consecultivos == 2:
        print("Voce precisa melhorar, Carlinhos")
        teste_2_erros_consecultivos = 0

    if teste_5_erros_consecultivos == 5:
        print("O treino de hoje nao esta rendendo Carlinhos, vamos tentar de novo amanha")
        break

    if tempo_restante <= 0:
        print("Temos que trabalhar urgentemente na sua velocidade, voce precisa errar menos")
        break

if erros_total == 0:
    print("Que desempenho excelente, Carlinhos, melhor impossivel")
elif erros_total > 0:
    print("Seu desempenho esta bom, mas poderia ter sido muito melhor")