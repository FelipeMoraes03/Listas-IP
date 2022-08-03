jogador = input()
numero_treinos = int(input())

gols_melhor_treino = 0
gols_pior_treino = float("inf")

for i in range(numero_treinos):
    quantidade_gols = int(input())
    if quantidade_gols > gols_melhor_treino:
        gols_melhor_treino = quantidade_gols
    if quantidade_gols < gols_pior_treino:
        gols_pior_treino = quantidade_gols

print(f"Belo dia de treinos, {jogador}! Hoje o seu melhor desempenho foi de {gols_melhor_treino} gols e o pior foi de {gols_pior_treino} gols. Rumo ao Ouro!")
