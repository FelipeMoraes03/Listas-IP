#ATIVIDADES QUE CADA PESSOA PRECISA REALIZAR:
pessoa_atividade = {}

#ATIVIDADES QUE A PESSOA NÃO PRECISA REALIZAR:
verificar_atividades = {}

#TODAS AS ATIVIDADES QUE PRECISAM SER FEITAS (INDEPENDENTE DA PESSOA):
lista_atividades = []

try:
    while True:
        nome, atividade = input().split(" ", 1)

        #PESSOA AINDA NÃO ESTÁ NO DICIONÁRIO COM TODOS OS VIZINHOS E SUAS TAREFAS:
        if nome not in pessoa_atividade:
            pessoa_atividade[nome] = [atividade]
            verificar_atividades[nome] = []

        #PESSOA JÁ ESTÁ NO DICIONÁRIO COM TODOS OS VIZINHOS E SUAS TAREFAS:
        else:

            #TAREFA AINDA NÃO FOI ASSOCIADA À PESSOA:
            if atividade not in pessoa_atividade[nome]:
                pessoa_atividade[nome].append(atividade)
        
        #ATIVIDADE AINDA NÃO ESTÁ NA LISTA DE TODAS AS ATIVIDADES:
        if atividade not in lista_atividades:
            lista_atividades.append(atividade)

except EOFError:
    for pessoa in pessoa_atividade:
        print(f"{pessoa}:")
        for tarefa in lista_atividades:

            #SE A PESSOA NÃO PRECISA FAZER A TAREFA:
            if tarefa not in pessoa_atividade[pessoa]:
                verificar_atividades[pessoa].append(tarefa)

        #PRINTAR TODAS AS TAREFAS QUE A PESSOA NÃO PRECISA REALIZAR:        
        for tarefa in verificar_atividades[pessoa]:
            print(f"- {tarefa}")