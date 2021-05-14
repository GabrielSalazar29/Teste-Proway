def dias_do_mes(a):
    """
     Uma função para retornar o valor de dias do mês correspondente.
    :param a: variável que possui o valor do mês que queremos saber os dias.
    :return: retorna o número de dias do mês correspondente.
    """
    if a == 2:
        return 28
    elif a == 4 or a == 6 or a == 9 or a == 11:
        return 30
    else:
        return 31


def n_de_pessoas_visu(a):
    """
    Uma função que recebe um valor inicial de pessoas e calcula quantos clicks,
    compartilhamentos e número de pessoas que irão visualizar a partir desses
    compartilhamentos.
    :param a: variável que possui o valor de pessoas que queremos analisar.
    :return: retorna o valor de pessoas que terão acesso ao anúncio a partir do compartilhamento.
    """
    n_de_clicks = a * 12 / 100
    n_de_compartilhamentos = int(n_de_clicks) * 3 / 20
    n_de_pessoas_sec = int(n_de_compartilhamentos) * 40
    return n_de_pessoas_sec


# Cria uma lista vazia.
anuncios = []

# Cria um dicionário vazio.
dicionario = {}

# Cria uma lista vazia
informações = []

# Inicia um laço de repetição que para quando a resposta é "N".
while True:
    print("-=" * 50)

    # Adiciona as informações ao dicionário.
    dicionario["Anuncio:"] = str(input("Informe o nome do anúncio que deseja cadastrar: ")).strip().capitalize()
    dicionario["Cliente:"] = str(input("Informe o nome do cliente: ")).strip().capitalize()
    dicionario["data_in:"] = str(input("Informe a data de início do anúncio [dia/mes/ano]: ")).strip().split("/")
    dicionario["data_fim:"] = str(input("Informe a data de término do anúncio [dia/mes/ano]: ")).strip().split("/")
    dicionario["investimento:"] = float(input("Informe o investimento por dia: "))

    # Adiciona uma cópia do dicionário a lista criada no início do código.
    anuncios.append(dicionario.copy())

    # Limpa o dicionário.
    dicionario.clear()
    print("-=" * 50)

    # Faz uma pergunta para adicionar outro anúncio ou sair do loop.
    while True:
        resposta = str(input("Deseja cadastrar mais algum anúncio[Responda com S ou N]? ")).strip().upper()

        # Impede que o usuário digite outra coisa que não seja S ou N.
        if resposta != "N" and resposta != "S":
            print("\033[31mDigite apenas S ou N!!!\033[m")
        else:
            break

    # Se a resposta for N ele sai do loop.
    if resposta == "N":
        break

    # Mostra na tela a parte superior da tabela com a cor azul.
print("\033[34m-=\033[m" * 80)
print(f"{'Anuncios':<14}\033[34m{'/':<2}\033[m{'Valor Total Investido':<25}\033[34m{'/':<2}\033[m"
      f"{'Quantidade Máx de Visualizações':<40}", end='')
print(f"\033[34m{'/':<2}\033[m{'Quantidade Máx de Cliques':<35}\033[34m{'/':<2}\033[m"
      f"{'Quantidade Máx de Compartilhamentos':<20}")
print("\033[34m-=\033[m" * 80)

# Estrutura de repetição para pegar todos os valores digitados e colocar cada um em uma variável.
for anuncio in anuncios:
    for c in anuncio:
        if c == "data_in:":
            data_in = int(anuncio[c][0])
            mes_in = int(anuncio[c][1])
            ano_in = int(anuncio[c][2])
        elif c == "data_fim:":
            data_fim = int(anuncio[c][0])
            mes_fim = int(anuncio[c][1])
            ano_fim = int(anuncio[c][2])
        elif c == "Anuncio:":
            nome_anuncio = anuncio[c]
        elif c == "Cliente:":
            cliente = anuncio[c]
        else:
            investimento = anuncio[c]

    # Coloca a diferença entre os meses e anos, de início e fim do anúncio, dentro de variáveis.
    meses = mes_fim - mes_in
    anos = ano_fim - ano_in

    # Estrutura de condição para contar os dias entre a data de início e fim.
    if anos == 0:
        if meses == 0:
            dias_totais = 1 + (data_fim - data_in)
        elif meses == 1:
            dias_totais = 1 + (dias_do_mes(mes_in) - data_in)
            dias_totais += data_fim
        elif meses > 1:
            dias_totais = 1 + (dias_do_mes(mes_in) - data_in)
            dias_totais += data_fim
            for mes in range(mes_in + 1, mes_fim):
                dias_totais += dias_do_mes(mes)
    elif anos == 1:
        dias_totais = 1 + (dias_do_mes(mes_in) - data_in)
        dias_totais += data_fim
        for mes in range(mes_in + 1, 13):
            dias_totais += dias_do_mes(mes)
        for mes in range(1, mes_fim):
            dias_totais += dias_do_mes(mes)
    else:
        dias_totais = 1 + (dias_do_mes(mes_in) - data_in)
        dias_totais += data_fim
        for mes in range(mes_in + 1, 13):
            dias_totais += dias_do_mes(mes)
        for mes in range(1, mes_fim):
            dias_totais += dias_do_mes(mes)
        dias_totais += (anos - 1) * 365
    valor_total = dias_totais * investimento

    # Faz o processo de contas para pegar o número máximo de pessoas que verão o anúncio e guardar numa variável.
    n_de_pessoas = investimento * 30
    n_de_pessoas_2 = n_de_pessoas_visu(n_de_pessoas)
    n_de_pessoas_3 = n_de_pessoas_visu(n_de_pessoas_2)
    n_de_pessoas_4 = n_de_pessoas_visu(n_de_pessoas_3)
    n_máximo_de_pessoas = int(n_de_pessoas) + n_de_pessoas_2 + n_de_pessoas_3 + n_de_pessoas_4

    # Faz o processo de contas para pegar o número máximo de clicks e guarda numa variável.
    n_maximo_de_clicks = int(n_de_pessoas * 12 / 100) + int(n_de_pessoas_2 * 12 / 100)
    n_maximo_de_clicks += int(n_de_pessoas_3 * 12 / 100)
    n_maximo_de_clicks += int(n_de_pessoas_4 * 12 / 100)

    # Faz o processo de contas para pegar o número máximo de compartilhamentos e guarda numa variável.
    n_maximo_de_compartilhamentos = int(int(n_de_pessoas * 12 / 100) * 3 / 20)
    n_maximo_de_compartilhamentos += int(int(n_de_pessoas_2 * 12 / 100) * 3 / 20)
    n_maximo_de_compartilhamentos += int(int(n_de_pessoas_3 * 12 / 100) * 3 / 20)

    # Guarda todos os valores que aparecem na tabela numa lista.
    lista = [nome_anuncio, valor_total, n_máximo_de_pessoas * dias_totais, n_maximo_de_clicks * dias_totais,
             n_maximo_de_compartilhamentos * dias_totais]

    # Faz uma cópia da lista e adiciona a uma outra lista chamada "informações".
    informações.append(lista.copy())

    # Mostra na tela o conteúdo da tabela calculado anteriormente.
    print(f"{nome_anuncio:<14}\033[34m{'/':<2}\033[m"
          f"R${valor_total:<23.2f}\033[34m{'/':<2}\033[m".replace('.', ','), end='')
    print(f"{n_máximo_de_pessoas * dias_totais:<40}\033[34m{'/':<2}\033[m"
          f"{n_maximo_de_clicks * dias_totais:<35}", end='')
    print(f"\033[34m{'/':<2}\033[m{n_maximo_de_compartilhamentos * dias_totais:<20}")
print("\033[34m-=\033[m" * 80)

# Inicia um laço de repetição que para quando a resposta for N.
while True:

    # Faz uma pergunta para filtrar a tabela ou encerrar o programa.
    while True:
        resp = str(input("Deseja filtrar a tabela pelo nome do cliente e pela data[Responda com S ou N]? ")).strip().upper()

        # Impede que o usuário digite outra coisa que não seja S ou N.
        if resp != "N" and resp != "S":
            print("\033[31mDigite apenas S ou N!!!\033[m")
        else:
            break

    # Se a resposta for S inicia o processo para selecionar o anúncio que o usuário deseja.
    if resp == "S":

        # Atribui um valor -1 a variável.
        pedido = -1

        # Pede para o usuário digitar o nome e a data do anúncio que deseja ver e guarda em variáveis.
        nome = str(input("Informe o nome do cliente que deseja ver as informações do anúncio: ")).strip().capitalize()
        data_in = str(input("Informe a data de início do anúncio [dia/mes/ano]: ")).strip().split("/")
        data_fim = str(input("Informe a data de término do anúncio [dia/mes/ano]: ")).strip().split("/")

        # Estrutura de repetição para pegar a posição da lista que contém o anúncio escolhido e colocar numa variável.
        for anuncio in anuncios:
            if anuncio["Cliente:"] == nome and anuncio["data_in:"] == data_in and anuncio["data_fim:"] == data_fim:
                pedido = anuncios.index(anuncio)

        # Estrutura condicional para verificar se os dados digitados correspondem a algum anúncio cadastrado.
        if pedido != -1:

            # Mostra na tela a parte superior da tabela com a cor azul novamente.
            print("\033[34m-=\033[m" * 80)
            print(f"{'Anuncios':<14}\033[34m{'/':<2}\033[m{'Valor Total Investido':<25}\033[34m{'/':<2}\033[m"
                  f"{'Quantidade Máx de Visualizações':<40}", end='')
            print(f"\033[34m{'/':<2}\033[m{'Quantidade Máx de Cliques':<35}\033[34m{'/':<2}\033[m"
                  f"{'Quantidade Máx de Compartilhamentos':<20}")
            print("\033[34m-=\033[m" * 80)

            # Estrutura de repetição para comparar a posição solicitada da lista anterior com a lista "informações",
            # para exibir na tela as informações referentes ao anúncio que o usuário solicitou.
            for i in informações:
                if informações.index(i) == pedido:
                    print(f"{i[0]:<14}\033[34m{'/':<2}\033[m"
                          f"R${i[1]:<23.2f}\033[34m{'/':<2}\033[m".replace('.', ','), end='')
                    print(f"{i[2]:<40}\033[34m{'/':<2}\033[m"
                          f"{i[3]:<35}", end='')
                    print(f"\033[34m{'/':<2}\033[m{i[4]:<20}")
            print("\033[34m-=\033[m" * 80)

        # Caso a variável "pedido" continue com o valor -1, transmite uma mensagem de erro.
        else:
            print("\033[31m++"*13)
            print(" Informações inválidas!!!")
            print("++"*13, "\033[m")
    # Encerra o loop caso o usuário digite N.
    else:
        break

# Mostra na tela uma mensagem.
print("\nENCERRANDO...")
