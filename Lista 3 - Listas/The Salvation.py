qnt_pre_selecionados = int(input())
capacidade_bunker = int(input())

max_medico = False
max_engenheiro = False
max_cientista = False
max_professor = False
continuar = True

lista_pessoas = []
lista_profissoes = []
profissoes_uteis = ["Medico(a)", "Engenheiro(a)", "Cientista", "Professor(a)"]
for _ in range(qnt_pre_selecionados):
    if continuar:
        pre_selecionado = input()
        pessoa, profissao = pre_selecionado.split(": ")

        # LIMITE DA PROFISSÃO NÃO ATINGIDO
        if lista_profissoes.count(profissao) < capacidade_bunker / 4 and profissao in profissoes_uteis:
            lista_pessoas.append(pessoa)
            lista_profissoes.append(profissao)

            # LIMITE DA PROFISSÃO ATINGIDO
            if lista_profissoes.count(profissao) == capacidade_bunker / 4:
                # QNT MÉDICOS IGUAL A CAPACIDADE MÁXIMA DE MÉDICOS
                if profissao == "Medico(a)" and max_medico == False:
                    print("Conseguimos chegar a quantidade maxima de Medicos")
                    max_medico = True

                # QNT ENGENHEIROS IGUAL A CAPACIADDE MÁXIMA
                elif profissao == "Engenheiro(a)" and max_engenheiro == False:
                    print("Conseguimos chegar a quantidade maxima de Engenheiros")
                    max_engenheiro = True

                # QNT DE CIENTISTAS IGUAL A CAPACIDADE MÁXIMA
                elif profissao == "Cientista" and max_cientista == False:
                    print("Conseguimos chegar a quantidade maxima de Cientistas")
                    max_cientista = True

                # QNT DE PROFESSORES IGUAL A CAPACIDADE MÁXIMA
                elif profissao == "Professor(a)" and max_professor == False:
                    print("Conseguimos chegar a quantidade maxima de Professores")
                    max_professor = True

        if len(lista_pessoas) == capacidade_bunker:  # CAPACIDADE MÁXIMA DO BUNKER
            if continuar == True:
                print("Chegamos a nossa capacidade maxima")
                continuar = False

try:
    while continuar:
        comando = input()

        if comando == "buscar":
            pessoa = input()
            if pessoa not in lista_pessoas:
                print(f"{pessoa} ainda não chegou no bunker...")
            else:
                print(f"{pessoa} ja esta no bunker")

        elif comando == "adicionar":
            pessoa_profissao = input()
            pessoa, profissao = pessoa_profissao.split(": ")

            # LIMITE DA PROFISSÃO NÃO ATINGIDO
            if lista_profissoes.count(profissao) < capacidade_bunker / 4 and profissao in profissoes_uteis:
                lista_pessoas.append(pessoa)
                lista_profissoes.append(profissao)

            # LIMITE DA PROFISSÃO ATINGIDO
            if lista_profissoes.count(profissao) == capacidade_bunker / 4:
                # QNT MÉDICOS IGUAL A CAPACIDADE MÁXIMA DE MÉDICOS
                if profissao == "Medico(a)" and max_medico == False:
                    print("Conseguimos chegar a quantidade maxima de Medicos")
                    max_medico = True

                # QNT ENGENHEIROS IGUAL A CAPACIADDE MÁXIMA
                elif profissao == "Engenheiro(a)" and max_engenheiro == False:
                    print("Conseguimos chegar a quantidade maxima de Engenheiros")
                    max_engenheiro = True

                # QNT DE CIENTISTAS IGUAL A CAPACIDADE MÁXIMA
                elif profissao == "Cientista" and max_cientista == False:
                    print("Conseguimos chegar a quantidade maxima de Cientistas")
                    max_cientista = True

                # QNT DE PROFESSORES IGUAL A CAPACIDADE MÁXIMA
                elif profissao == "Professor(a)" and max_professor == False:
                    print("Conseguimos chegar a quantidade maxima de Professores")
                    max_professor = True

        else:
            print("**COMANDO INVALIDO**")

        if len(lista_pessoas) == capacidade_bunker: # CAPACIDADE MÁXIMA DO BUNKER
            if continuar == True:
                print("Chegamos a nossa capacidade maxima")
                continuar = False


except EOFError:
    if len(lista_pessoas) < capacidade_bunker:
        print("Na nossa busca no banco de dados, nao achamos pessoas suficientes com os parametros de selecao")

print(f"""\nRelatorio:
Medicos: {lista_profissoes.count('Medico(a)')}
Engenheiros: {lista_profissoes.count('Engenheiro(a)')}
Cientistas: {lista_profissoes.count('Cientista')}
Professores: {lista_profissoes.count('Professor(a)')}""")