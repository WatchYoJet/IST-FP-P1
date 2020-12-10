# 98962 Pedro Pereira
def eh_tabuleiro(tab):  # 2.1.1
    # eh_tabuleiro: universal -> booleano
    """
    Valida se o tab (tabuleiro) colocado e valido
    Esta funcao devolve false se nao for na forma:
    (x,x,x),(x,x,x),(x,x,x)
    sendo "x" = 1 (X), -1 (O) ou 0 (Vazio)
    Retorna:
        True/False
    """
    hipoteses = (-1, 0, 1)
    if not (isinstance(tab, tuple) and len(tab) == 3):
        return False
    tuplo1, tuplo2, tuplo3 = tab[0], tab[1], tab[2]
    if not (type(tuplo1) == tuple and type(tuplo2) == tuple and type(tuplo3) == tuple):
        return False
    if not (len(tuplo1) == 3 and len(tuplo2) == 3 and len(tuplo3) == 3):
        return False
    for i in range(len(tuplo1)):
        if not (
            tuplo1[i] in hipoteses and tuplo2[i] in hipoteses and tuplo3[i] in hipoteses
        ):
            return False
    return True


def tup_tem_tipo(tup, tipo):
    # tup_tem_tipo: tuple x integer -> boolean / NoneType
    # (tuplo X tipo -> True/None)
    """
    Recebe um tuplo e um tipo em forma de int,
    e verifica se esse int esta presente no tuplo
    Devolve True se for verificado e None se nao.
    Funcao auxiliar.
    Retorna:
        True / None
    """
    for x in tup:
        if x == tipo:
            return True


def eh_difi(dific):
    # eh_difi: string -> boolean / NoneType (dificuldade -> False/None)
    """
    Recebe uma string e verifica se ela e igual as predefenidas
    (basico, normal ou perfeito)
    Funcao auxiliar.
    Retorna:
        False/None
    """
    if dific != "basico" and dific != "normal" and dific != "perfeito":
        return False


def eh_tipo(tipo):
    # eh_tipo: integer -> boolean / NoneType (tipo -> False/None)
    """
    Recebe um integer e verifica o seu tipo, e se e 1, 0 ou -1
    Funcao auxiliar.
    Retorna:
        False/None
    """
    if type(tipo) != int or tipo < -1 or tipo > 1 or tipo == 0:
        return False


def eh_posicao(posi):  # 2.1.2
    # eh_posicao: universal -> boolean (posicao -> True/False)
    """
    Recebe um integer e verifica o seu tipo,
    e se pertence ao intervalo de [1,9] devolvendo entao True/False
    Retorna:
        True/False
    """
    x = True if type(posi) == int and posi >= 1 and posi <= 9 else False
    return x


def contrar_tipo(tipo):
    # contrar_tipo: integer -> integer (tipo -> tipo contrario)
    """
    Recebe um integer e devolve o seu simetrico.
    Como esta funcao apenas sera utilizada com os inteiros 1 e -1,
    foi simplificada desta forma
    funcao auxiliar
    Retorna:
        simetrico do argumento
    """
    if tipo == 1:
        return -1
    if tipo == -1:
        return 1


def obter_coluna(tab, colun):  # 2.1.3
    # obter_coluna: tabuleiro X integer -> vector
    # (tabuleiro X numero de coluna -> vector)
    """
    Recebe um tabuleiro e um inteiro. Valida o tabuleiro
    e o inteiro(tem de ser entre [1,3]).
    Retorna com a coluna correspondente ao inteiro introduzido
    indo da esquerda para a direita
    ValueError:
        se algum dos argumentos nao for valido
    """
    if type(colun) != int or colun < 1 or colun > 3 or (eh_tabuleiro(tab) == False):
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    else:
        colun = colun - 1
        tupColun = (tab[0][colun], tab[1][colun], tab[2][colun])
        return tupColun


def obter_linha(tab, lin):  # 2.1.4
    # obter_linha: tuple X integer -> vector
    # (tabuleiro X numero de linha -> vector)
    """
    Recebe um tabuleiro e um inteiro. Valida o tabuleiro
    e o inteiro(tem de ser entre [1,3]).
    Retorna com a linha correspondente ao inteiro introduzido
    indo de cima para baixo
    ValueError:
        se algum dos argumentos nao for valido
    """
    if type(lin) != int or lin < 1 or lin > 3 or eh_tabuleiro(tab) == False:
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    else:
        lin = lin - 1
        tupLin = (tab[lin][0], tab[lin][1], tab[lin][2])
        return tupLin


def obter_diagonal(tab, diag):  # 2.1.5
    # obter_diagonal: tuple X integer -> vector
    # (tabuleiro X numero da diagonal -> vector)
    """
    Recebe um tabuleiro e um inteiro. Valida o tabuleiro e
    o inteiro(tem de ser entre [1,2]).
    Retorna com a diagonal correspondente ao inteiro
    introduzido sendo 1 a diagonal a que vai das posicoes 1 a 9
    e 2 a diagonal que vai de 3 a 7
    ValueError:
        se algum dos argumentos nao for valido
    """
    if type(diag) != int or diag < 1 or diag > 2 or eh_tabuleiro(tab) == False:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    else:
        if diag == 1:
            digEsqDir = (tab[0][0], tab[1][1], tab[2][2])
            return digEsqDir
        else:
            digDirEsq = (tab[2][0], tab[1][1], tab[0][2])
            return digDirEsq


def tabuleiro_str(tab):  # 2.1.6
    # tabueliro_str: tabuleiro -> cadeia de carateres
    """
    Recebe um tabuleiro. Valida o tabuleiro.
    Transforma o tabuleiro numa string.
    Nesta funcao foi optado pela criacao da funcao
    tendo em conta ao tabuleiro dado.
    A funcao possui um ciclo que percorre o tablueiro e coloca um 'X'
    quando deteta um 1 e 'O' quando deteta um -1.
    A mesma tambem coloca um espaco em branco se for 0 e um '|'
    sempre que o mesmo acaba de percorrer as posicoes 1 e 2 de cada linha
    ValueError:
        se o argumento nao for valido
    """
    if eh_tabuleiro(tab) == False:
        raise ValueError("tabuleiro_str: o argumento e invalido")
    resul = ""
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])):
            if tab[i][j] == 1:
                resul = resul + (" X ")
            elif tab[i][j] == 0:
                resul = resul + ("   ")
            elif tab[i][j] == -1:
                resul = resul + (" O ")
            if j == 0 or j == 1:
                resul = resul + ("|")
        if i != 2:
            resul = resul + ("\n-----------\n")

    return resul


def eh_posicao_livre(tab, posi):  # 2.2.1
    # eh_posicao_livre: tabuleiro X posicao -> boolean
    """
    Recebe e valida um tabuleiro e uma posisao.
    A funcao verifica se a posisao colocada esta ou nao ocupada (True/False)
    Verificando entre que numeros ou seja, que linha e que esse mesmo numero
    esta presente, utiliza-se simples opercoes aritmeticas
    e verifica se nessa mesma posicao, esta um zero ou seja, uma casa livre
    ValueError:
        se algum dos argumentos nao for valido
    """
    if eh_tabuleiro(tab) == False or eh_posicao(posi) != True:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    elif posi <= 3:
        if tab[0][posi - 1] == 0:
            return True
    elif posi <= 6:
        if tab[1][posi - 4] == 0:
            return True
    elif posi <= 9:
        if tab[2][posi - 7] == 0:
            return True
    return False


def obter_posicoes_livres(tab):  # 2.2.2
    # obter_posicoes_livre: tabuleiro -> vector
    """
    A funcao recebe um tabuleiro. Com 2 ciclos "for" que ira passar
    por todos os valores do tablueiro.
    Se o valor da posicao for 0, essa mesma posicao sera colocada num tuplo.
    Retorna:
        Tuplo com todas as posicoes livre no tabuleiro colocado no argumento
    ValueError:
        Se o argumento nao for valido
    """
    if eh_tabuleiro(tab) == False:
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    pot = ()
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])):
            if tab[i][j] == 0:
                if i == 0:
                    pot = pot + (j + 1,)
                if i == 1:
                    pot = pot + (j + 4,)
                if i == 2:
                    pot = pot + (j + 7,)
    return pot


def jogador_ganhador(tab):  # 2.2.3
    # jogador_ganhador: tabuleiro -> integer
    """
    Recebe um tabuleiro. E utilizado 2 ciclos while,
    um para as linhas e colunas,e outro para as diagonais.
    Verifica se existe um 3 em linha e se existir,
    retorna com tipo do jogador que ganhou.
    Se o jogo ainda nao tiver terminado, retorna com 0
    Retorna:
        O jogador que, naquele tabuleiro, ganhou o jogo
    ValueError:
        Se o argumento nao for valido
    """
    if eh_tabuleiro(tab) == False:
        raise ValueError("jogador_ganhador: o argumento e invalido")
    count = 1
    while count <= 3:
        lin = obter_linha(tab, count)
        col = obter_coluna(tab, count)
        if (lin[0] == 1 or lin[0] == -1) and lin[0] == lin[1] and (lin[1] == lin[2]):
            return lin[0]
        if (col[0] == 1 or col[0] == -1) and col[0] == col[1] and (col[1] == col[2]):
            return col[0]
        count += 1
    count = 1
    while count <= 2:
        dig = obter_diagonal(tab, count)
        if (dig[0] == 1 or dig[0] == -1) and dig[0] == dig[1] and (dig[1] == dig[2]):
            return dig[0]
        count += 1
    return 0


def marcar_posicao(tab, tipo, posi):  # 2.2.4
    # marcar_posicao: tabuleiro X integer X posicao -> tabuleiro
    """
    Valida os argumentos introduzidos.
    Esta funcao verifica em que linha a poiscao entroduzida se localiza.
    Se ela estiver na primeira linha, a posicao tem de estar
    entre os valores [1,3].
    E utilizado uma lista, que possui os valores de cada linha do tabuleiro.
    E entao modificado o 0 prensente nessa posicao com o tipo selecionado.
    Retorna:
        Um tabuleiro que foi alterado com o tipo introduzido nos argumentos,
        na posicao igualmente aprensentada
    ValueError:
        Se algum dos argumentos nao for valido
    """
    if (
        eh_tabuleiro(tab) == False
        or eh_tipo(tipo) == False
        or eh_posicao(posi) == False
        or eh_posicao_livre(tab, posi) == False
    ):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    if posi <= 3:
        poteTab = list(tab[0])
        poteTab[posi - 1] = tipo
        poteTab = tuple(poteTab)
        tab = (poteTab, tab[1], tab[2])
    elif posi <= 6:
        poteTab = list(tab[1])
        poteTab[posi - 4] = tipo
        poteTab = tuple(poteTab)
        tab = (tab[0], poteTab, tab[2])
    else:
        poteTab = list(tab[2])
        poteTab[posi - 7] = tipo
        poteTab = tuple(poteTab)
        tab = (tab[0], tab[1], poteTab)
    return tab


def escolher_posicao_manual(tab):  # 2.3.1
    # escolher_posicao_manual: tabuleiro -> posicao
    """
    Valida os argumentos introduzidos.
    Retorna:
        posicao escolhida
    ValueError:
        Se o tabuleiro for invalido
        Se a posisao colocada nao for valida
        ou se a casa escolhida nao for livre
    """
    if eh_tabuleiro(tab) == False:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")
    posi = eval(input("Turno do jogador. Escolha uma posicao livre: "))
    if eh_posicao(posi) != True or eh_posicao_livre(tab, posi) != True:
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    return posi


def escolher_posicao_auto_12(tab, tipo):
    # escolher_posicao_auto_12: tabuleiro X tipo -> posicao
    """
    Esta funcao serve para retornar os criterios 1 e 2.
    A funcao esta dividida em 2 partes: 1(ataque) e 2(defesa)
    Dentro dessas duas partes, existem as linhas, colunas e diagonais
    A funcao verifica se e possivel criar / defender um 3 em linha
    Retorna:
        posicao que impede/cria 3 em linha
    """
    pote = 0
    posi = 0
    posi1 = 1
    j = 1
    l = 1
    contr = contrar_tipo(tipo)
    for i in tab:
        poteTab = list(i)
        if pote == 1:
            posi = 3
            posi1 = 2
        elif pote == 2:
            posi = 6
            posi1 = 3
        if (
            eh_posicao_livre(tab, posi + 1) == True
            or eh_posicao_livre(tab, posi + 2) == True
            or eh_posicao_livre(tab, posi + 3) == True
        ):  # 1 linhas ataque
            if (
                poteTab[0] == tipo
                and poteTab[0] == poteTab[1]
                and eh_posicao_livre(tab, posi + 3) == True
            ):
                return posi + 3
            elif (
                poteTab[1] == tipo
                and poteTab[1] == poteTab[2]
                and eh_posicao_livre(tab, posi + 1) == True
            ):
                return posi + 1
            elif (
                poteTab[2] == tipo
                and poteTab[0] == poteTab[2]
                and eh_posicao_livre(tab, posi + 2) == True
            ):
                return posi + 2
        if (
            eh_posicao_livre(tab, posi1) == True
            or eh_posicao_livre(tab, posi1 + 3) == True
            or eh_posicao_livre(tab, posi1 + 6) == True
        ):  # 1 coluna ataque
            poteTab1 = obter_coluna(tab, pote + 1)
            if (
                poteTab1[0] == tipo
                and poteTab1[0] == poteTab1[1]
                and eh_posicao_livre(tab, posi1 + 6) == True
            ):
                return posi1 + 6
            elif (
                poteTab1[1] == tipo
                and poteTab1[1] == poteTab1[2]
                and eh_posicao_livre(tab, posi1) == True
            ):
                return posi1
            elif (
                poteTab1[2] == tipo
                and poteTab1[0] == poteTab1[2]
                and eh_posicao_livre(tab, posi1 + 3) == True
            ):
                return posi1 + 3
        if (
            eh_posicao_livre(tab, 1) == True
            or eh_posicao_livre(tab, 5) == True
            or eh_posicao_livre(tab, 9) == True
            or eh_posicao_livre(tab, 3) == True
            or eh_posicao_livre(tab, 7) == True
        ):
            # 1 diagonal ataque
            while j <= 2:
                dig = obter_diagonal(tab, j)
                if dig[0] == tipo and dig[0] == dig[1]:
                    if j == 1 and eh_posicao_livre(tab, 9) == True:
                        return 9
                    elif j == 2 and eh_posicao_livre(tab, 3) == True:
                        return 3
                if dig[1] == tipo and dig[1] == dig[2]:
                    if j == 1 and eh_posicao_livre(tab, 1) == True:
                        return 1
                    elif j == 2 and eh_posicao_livre(tab, 7) == True:
                        return 7
                if (
                    dig[2] == tipo
                    and dig[0] == dig[2]
                    and eh_posicao_livre(tab, 5) == True
                ):
                    return 5
                j += 1
        pote += 1
    pote = 0
    posi = 0
    posi1 = 1
    j = 1
    l = 1
    for k in tab:
        poteTab = list(k)
        if pote == 1:
            posi = 3
            posi1 = 2
        elif pote == 2:
            posi = 6
            posi1 = 3
        if (
            eh_posicao_livre(tab, posi + 1) == True
            or eh_posicao_livre(tab, posi + 2) == True
            or eh_posicao_livre(tab, posi + 3) == True
        ):  # 2 linhas defesa
            if poteTab[0] == contr and poteTab[0] == poteTab[1]:
                return posi + 3
            if poteTab[1] == contr and poteTab[1] == poteTab[2]:
                return posi + 1
            if poteTab[2] == contr and poteTab[0] == poteTab[2]:
                return posi + 2
        if (
            eh_posicao_livre(tab, 1) == True
            or eh_posicao_livre(tab, 5) == True
            or eh_posicao_livre(tab, 9) == True
            or eh_posicao_livre(tab, 3) == True
            or eh_posicao_livre(tab, 7) == True
        ):
            # 2 diagonal defesa
            while l <= 2:
                dig = obter_diagonal(tab, l)
                if (
                    dig[0] == contr
                    and dig[0] == dig[1]
                    and eh_posicao_livre(tab, 9) == True
                    and eh_posicao_livre(tab, 3) == True
                ):
                    if l == 1:
                        return 9
                    else:
                        return 3
                if (
                    dig[1] == contr
                    and dig[1] == dig[2]
                    and eh_posicao_livre(tab, 1) == True
                    and eh_posicao_livre(tab, 7) == True
                ):
                    if l == 1:
                        return 1
                    else:
                        return 7
                if (
                    dig[2] == contr
                    and dig[0] == dig[2]
                    and eh_posicao_livre(tab, 5) == True
                ):
                    return 5
                l += 1
        if (
            eh_posicao_livre(tab, posi1) == True
            or eh_posicao_livre(tab, posi1 + 3) == True
            or eh_posicao_livre(tab, posi1 + 6) == True
        ):  # 2 coluna defesa
            poteTab1 = obter_coluna(tab, pote + 1)
            if (
                poteTab1[0] == contr
                and poteTab1[1] == contr
                and eh_posicao_livre(tab, posi1 + 6) == True
            ):
                return posi1 + 6
            if (
                poteTab1[1] == contr
                and poteTab1[1] == poteTab1[2]
                and eh_posicao_livre(tab, posi1) == True
            ):
                return posi1
            if (
                poteTab1[2] == contr
                and poteTab1[0] == poteTab1[2]
                and eh_posicao_livre(tab, posi1 + 3) == True
            ):
                return posi1 + 3
        pote += 1
    return False


def obter_3_criterio(tab, tipo):
    dig1 = obter_diagonal(tab, 1)  # 3
    dig2 = obter_diagonal(tab, 2)
    linha1 = obter_linha(tab, 1)
    linha2 = obter_linha(tab, 2)
    linha3 = obter_linha(tab, 3)
    i = 1
    tupote = ()
    while i <= 3:
        colunas = obter_coluna(tab, i)
        if (
            tup_tem_tipo(colunas, tipo) == True
            and tup_tem_tipo(colunas, contrar_tipo(tipo)) != True
        ):
            # coluna x linha 1
            if (
                eh_posicao_livre(tab, i) == True
                and tup_tem_tipo(linha1, tipo) == True
                and tup_tem_tipo(linha1, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (i,)
            # coluna x linha 2
            if (
                eh_posicao_livre(tab, i + 3) == True
                and tup_tem_tipo(linha2, tipo) == True
                and tup_tem_tipo(linha2, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (i + 3,)
            # coluna x linha 3
            if (
                eh_posicao_livre(tab, i + 6) == True
                and tup_tem_tipo(linha3, tipo) == True
                and tup_tem_tipo(linha3, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (i + 6,)
            # diagonais
            if (
                i == 1
                and eh_posicao_livre(tab, 1) == True
                and tup_tem_tipo(dig1, tipo) == True
                and tup_tem_tipo(dig1, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (1,)
            if (
                i == 1
                and eh_posicao_livre(tab, 7) == True
                and tup_tem_tipo(dig2, tipo) == True
                and tup_tem_tipo(dig2, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (7,)
            if (
                i == 2
                and eh_posicao_livre(tab, 5) == True
                and (
                    tup_tem_tipo(dig1, tipo) == True or tup_tem_tipo(dig2, tipo) == True
                )
                and tup_tem_tipo(dig1, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (5,)
            if (
                i == 3
                and eh_posicao_livre(tab, 3) == True
                and tup_tem_tipo(dig2, tipo) == True
                and tup_tem_tipo(dig2, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (3,)
            if (
                i == 3
                and eh_posicao_livre(tab, 9) == True
                and tup_tem_tipo(dig1, tipo) == True
                and tup_tem_tipo(dig1, contrar_tipo(tipo)) != True
            ):
                tupote = tupote + (9,)
        i += 1
    tupote = list(tupote)
    tupote.sort()
    return tupote


def obter_dois_linha(tab, tipo):
    # obter_dois_linha: tabuleiro X tipo -> posicao
    """
    Esta funcao serve para retornar o criterio 4.
    A funcao esta dividida em 2 partes: 1(diagonais) e 2(linhas e colunas)
    Utilizando lincolun, um tuplo constituido por outros tuplos
    de todas as linhas e colunas,verifica se e possivel a criacao de um 2 em
    linha para impedir a biforcacao inimiga.
    Se a defesa a essa posicao criar uma nova biforcacao,
    nao funcao nao a deve retornar
    Retorna:
        posicao que cria um 2 em linha
    """
    i = 1
    pote = 1
    dig = (obter_diagonal(tab, 1), obter_diagonal(tab, 2))
    lincolun = (
        obter_linha(tab, 1),
        obter_linha(tab, 2),
        obter_linha(tab, 3),
        obter_coluna(tab, 1),
        obter_coluna(tab, 2),
        obter_coluna(tab, 3),
    )
    tupote = ()
    for h in dig:
        if h[0] == tipo and h[1] == 0 and h[2] == 0:
            tupote = tupote + (5,)
        if h[0] == 0 and h[1] == tipo and h[2] == 0:
            if i == 1:
                tupote = tupote + (2,)
            if i == 2:
                tupote = tupote + (7,)
        if h[0] == 0 and h[1] == 0 and h[2] == tipo:
            tupote = tupote + (5,)
        i += 1
    for j in lincolun:
        if j[0] == tipo and j[1] == 0 and j[2] == 0:
            if pote == 1:
                tupote = tupote + (3,)
            if pote == 2 or pote == 5:
                tupote = tupote + (5,)
            if pote == 3 or pote == 6:
                tupote = tupote + (9,)
            if pote == 4:
                tupote = tupote + (4,)
        if j[0] == 0 and j[1] == tipo and j[2] == 0:
            if pote == 1 or pote == 4:
                tupote = tupote + (1,)
            if pote == 2:
                tupote = tupote + (2,)
            if pote == 3 or pote == 6:
                tupote = tupote + (9,)
        if j[0] == 0 and j[1] == 0 and j[2] == tipo:
            if pote == 1 or pote == 4:
                tupote = tupote + (1,)
            if pote == 2 or pote == 5:
                tupote = tupote + (5,)
            if pote == 3:
                tupote = tupote + (8,)
            if pote == 4 or pote == 6:
                tupote = tupote + (3,)
        pote += 1
    tupotelist = list(tupote)
    tupotelist.sort()
    if len(obter_3_criterio(tab, contrar_tipo(tipo))) == 1:
        return tupotelist[0]
    if len(obter_3_criterio(tab, contrar_tipo(tipo))) > 1:
        pote = 0
        for i in tupotelist:
            while pote < len(tupotelist):
                potab = tab
                potab = marcar_posicao(potab, tipo, tupotelist[pote])
                if len(obter_3_criterio(potab, contrar_tipo(tipo))) < len(
                    obter_3_criterio(tab, contrar_tipo(tipo))
                ):
                    return tupotelist[pote]
                pote += 1
    return tupotelist[0]


def escolher_posicao_auto_78(tab, tipo):
    # escolher_posicao_auto_78: tabuleiro X tipo -> posicao
    """
    Esta funcao serve para retornar os criterios 7 e 8.
    A funcao esta dividida em 2 partes: criterio 7 e criterio 8.
    Na primeira parte, e utilizada um loop "while" que verifica se
    algum canto se encontra livre.
    Na segunda parte, a funcao verifica se alguma posicao que nao
    e o meio nem os cantos se encontra livre.
    Retorna:
        posicao livre dos cantos / posicao livre de 2, 4, 6 ou 8
    """
    cont = 1
    while eh_posicao(cont) == True:  # 7
        if eh_posicao_livre(tab, cont) == True:
            return cont
        if cont == 1 or cont == 7:
            cont += 2
        else:
            cont += 4
    if eh_posicao_livre(tab, 2) == True:  # 8
        return 2
    elif eh_posicao_livre(tab, 4) == True:  # 8
        return 4
    elif eh_posicao_livre(tab, 6) == True:  # 8
        return 6
    elif eh_posicao_livre(tab, 8) == True:
        return 8
    return False


def escolher_posicao_auto(tab, tipo, dific):  # 2.3.2
    # escolher_posicao_auto: tabuleiro X tipo X cad. caracteres -> posicao
    """
    Esta funcao recebe um tabuleiro, o tipo que joga (X ou O) e dependendo
    de uma dificuldade, ira escolher uma posicao tendo em conta aos criterios
    associados.
    A mesma esta dividida em 3:
    dificuldade basica (criterios 5,7 e 8)
    dificuldade normal (criterios 1,2,5,6,7,8)
    dificuldade perfeita (criterios 1,2,3,4,5,6,7,8)
    Retorna:
        posicao que melhor se adequa ao tabuleiro tendo em conta a dificuldade
    """
    if eh_difi(dific) == False or eh_tabuleiro(tab) == False or eh_tipo(tipo) == False:
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")
    if dific == "basico":  # basico
        if eh_posicao_livre(tab, 5) == True:  # 5
            return 5
        if escolher_posicao_auto_78(tab, tipo) != False:  # 7,8
            return escolher_posicao_auto_78(tab, tipo)
    if dific == "normal":  # normal
        if escolher_posicao_auto_12(tab, tipo) != False:  # 1,2
            return escolher_posicao_auto_12(tab, tipo)
        if eh_posicao_livre(tab, 5) == True:  # 5
            return 5
        if tab[0][0] == contrar_tipo(tipo) and eh_posicao_livre(tab, 9) == True:  # 6
            return 9
        if tab[0][2] == contrar_tipo(tipo) and eh_posicao_livre(tab, 7) == True:
            return 7
        if tab[2][0] == contrar_tipo(tipo) and eh_posicao_livre(tab, 3) == True:
            return 3
        if tab[2][2] == contrar_tipo(tipo) and eh_posicao_livre(tab, 1) == True:
            return 1
        if escolher_posicao_auto_78(tab, tipo) != False:  # 7,8
            return escolher_posicao_auto_78(tab, tipo)
    if dific == "perfeito":  # perfeito
        if escolher_posicao_auto_12(tab, tipo) != False:  # 1,2
            return escolher_posicao_auto_12(tab, tipo)
        if len(obter_3_criterio(tab, tipo)) != 0:  # 3
            return (obter_3_criterio(tab, tipo))[0]
        if len(obter_3_criterio(tab, contrar_tipo(tipo))) != 0:
            return obter_dois_linha(tab, tipo)  # 4
        if eh_posicao_livre(tab, 5) == True:  # 5
            return 5
        if tab[0][0] == contrar_tipo(tipo) and eh_posicao_livre(tab, 9) == True:  # 6
            return 9
        if tab[0][2] == contrar_tipo(tipo) and eh_posicao_livre(tab, 7) == True:
            return 7
        if tab[2][0] == contrar_tipo(tipo) and eh_posicao_livre(tab, 7) == True:
            return 3
        if tab[2][2] == contrar_tipo(tipo) and eh_posicao_livre(tab, 1) == True:
            return 1
        if escolher_posicao_auto_78(tab, tipo) != False:  # 7,8
            return escolher_posicao_auto_78(tab, tipo)


def eh_terminado(tab):
    # escolher_posicao_auto: tabuleiro X tipo X cad. caracteres -> posicao
    """
    A funcao recebe um tablueiro e, utilizando a funcao jogador_ganhador e
    a escolher_posicao_auto_78, devolve em string o significado do inteiro.
    Se o jogador vencedor for 1, devolve X. Se for -1, devolve O e se for 0,
    devolve Empate
    Retorna:
        Representacao em string do resultado do jogo quando terminado
    Funcao auxiliar
    """
    if jogador_ganhador(tab) == 0:
        return "EMPATE"
    elif jogador_ganhador(tab) == 1:
        return "X"
    elif jogador_ganhador(tab) == -1:
        return "O"


def jogo_do_galo(tipo, dific):
    # jogo_do_galo: cad. caracteres X cad. caracteres -> posicao
    """
    Esta funcao recebe duas cadeias de caracteres.
    A primeira, sendo o tipo representada em forma de string,
    e mudada para integer.
    A segunda, e a dificuldade escolhida pelo utilizador.
    A funcao e dividida em 2, se o tipo for 'X' ou '0'
    Foi assim escolhido pois, no jogo, o 'X' comeca a jogar
    Foi introduzido tambem um ciclo 'while'.
    E importante explicar o uso de while i < 4:
    Em ambas as partes desta funcao, a primeira jogada e sempre fora
    do while. Num jogo, o maximo par de jogadas possivel e 4
    ate chegar ao empate.
    Retorna:
        jogo funcional do jogo do galo
    """
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    i = 0
    if tipo == "X":
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.")
        tipo = 1
        tab = marcar_posicao(tab, tipo, escolher_posicao_manual(tab))
        print(tabuleiro_str(tab))
        while i < 4:
            tab = marcar_posicao(
                tab,
                contrar_tipo(tipo),
                escolher_posicao_auto(tab, contrar_tipo(tipo), dific),
            )
            if dific == "basico":
                print("Turno do computador (basico):")
            elif dific == "normal":
                print("Turno do computador (normal):")
            elif dific == "perfeito":
                print("Turno do computador (perfeito):")
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) != 0:
                return eh_terminado(tab)
            tab = marcar_posicao(tab, tipo, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) != 0:
                return eh_terminado(tab)
            i += 1
        return eh_terminado(tab)
    if tipo == "O":
        print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.")
        tipo = -1
        tab = marcar_posicao(
            tab,
            contrar_tipo(tipo),
            escolher_posicao_auto(tab, contrar_tipo(tipo), dific),
        )
        if dific == "basico":
            print("Turno do computador (basico):")
        elif dific == "normal":
            print("Turno do computador (normal):")
        elif dific == "perfeito":
            print("Turno do computador (perfeito):")
        print(tabuleiro_str(tab))
        while i < 4:
            tab = marcar_posicao(tab, tipo, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) != 0:
                return eh_terminado(tab)
            tab = marcar_posicao(
                tab,
                contrar_tipo(tipo),
                escolher_posicao_auto(tab, contrar_tipo(tipo), dific),
            )
            if dific == "basico":
                print("Turno do computador (basico):")
            elif dific == "normal":
                print("Turno do computador (normal):")
            elif dific == "perfeito":
                print("Turno do computador (perfeito):")
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) != 0:
                return eh_terminado(tab)
            i += 1
        return eh_terminado(tab)


tab = ((False, False, 0), (0, 0, 0), (0, 0, 0))
print(eh_tabuleiro(tab))