import copy
import time

tabuleiro = [
    [0,0,0,7,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,4,3,0,2,0,0],
    [0,0,0,0,0,0,0,0,6],
    [0,0,0,5,0,9,0,0,0],
    [0,0,0,0,0,0,4,1,8],
    [0,0,0,0,8,1,0,0,0],
    [0,0,2,0,0,0,0,5,0],
    [0,4,0,0,0,0,3,0,0],
]


tabuleiro_fixo = copy.deepcopy(tabuleiro)

COMPRIMENTO = 9
COMPRIMENTO_QUADRANTE = 3

INICIO_QUADRANTES = [
    (0,0), (0,3), (0,6),
    (3,0), (3,3), (3,6),
    (6,0), (6,3), (6,6),
]

conjuntos_linhas = [set() for i in range(COMPRIMENTO)]
conjuntos_colunas = [set() for i in range(COMPRIMENTO)]
conjuntos_quadrantes = [set() for i in range(COMPRIMENTO)]

soma_total = 0

def inicializa_auxiliares():
    global soma_total

    for linha in range(COMPRIMENTO):
        for coluna in range(COMPRIMENTO):
            numero = tabuleiro_fixo[linha][coluna]
            if numero > 0:
                soma_total += numero

                conjuntos_linhas[linha].add(numero)
                conjuntos_colunas[coluna].add(numero)
                quadrante = pega_quadrante(linha, coluna)
                conjuntos_quadrantes[quadrante-1].add(numero)

def imprime_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        campo_string = ''
        for campo in linha:
            if campo == 0:
                campo_string = f'{campo_string}|___'
            else:
                campo_string = f'{campo_string}|_{str(campo)}_'
        print (campo_string+'|')
    print ('_______________')

def le_comando():
    comando = input("Jogada (ex: linha,coluna,numero): ")
    if ',' not in comando:
        return None

    x, y, numero = comando.split(',')
    return int(x), int(y), int(numero)

def pega_quadrante(x, y):
    if x < 3 and y < 3:
        return 1
    if x < 3 and y < 6:
        return 2
    if x < 3 and y < 9:
        return 3
    if x < 6 and y < 3:
        return 4
    if x < 6 and y < 6:
        return 5
    if x < 6 and y < 9:
        return 6
    if x < 9 and y < 3:
        return 7
    if x < 9 and y < 6:
        return 8
    if x < 9 and y < 9:
        return 9

def valida_jogada(x, y, numero):
    if numero == 0:
        return True

    # verificação de linha
    if numero in conjuntos_linhas[x]:
        return False

    # verificação de coluna
    if numero in conjuntos_colunas[y]:
        return False

    quadrante = pega_quadrante(x, y)

    # verificação de quadrante:
    if numero in conjuntos_quadrantes[quadrante-1]:
        return False

    return True

def executa_jogada(x, y, numero):
    if x >= COMPRIMENTO or y >= COMPRIMENTO:
        return False
    if x < 0 or y < 0:
        return False

    if tabuleiro_fixo[x][y] > 0:
        return False
    if numero < 0 or numero > 9:
        return False

    if not valida_jogada(x, y, numero):
        return False

    tabuleiro[x][y] = numero
    return True


def verifica_fim_jogo():
    return soma_total == 405

def inicia_jogo():
    while True:
        imprime_tabuleiro(tabuleiro)

        comando = le_comando()
        if comando is None:
            print ('Comando inválido. Tente novamente...')
            continue

        x, y, numero = comando
        if not executa_jogada(x, y, numero):
            print ('Jogada inválida! Tente novamente...')

        if verifica_fim_jogo() == True:
            print ('Parabens você ganhou o jogo!')
            break

def decide_jogada(valor_atual):
    if valor_atual >= 9:
        return None
    return valor_atual + 1

def pega_posicao_anterior(linha, coluna):
    if coluna == 0:
        linha, coluna = linha - 1, 8
    else:
        linha, coluna = linha, coluna - 1

    if tabuleiro_fixo[linha][coluna] > 0:
        return pega_posicao_anterior(linha, coluna)
    return linha, coluna

def pega_proxima_posicao(linha, coluna):
    if coluna == 8:
        linha, coluna = linha + 1, 0
    else:
        linha, coluna = linha, coluna + 1

    if tabuleiro_fixo[linha][coluna] > 0:
        return pega_proxima_posicao(linha, coluna)
    return linha, coluna

def desfaz_jogada(tabuleiro, linha, coluna):
    tabuleiro[linha][coluna] = 0
    return pega_posicao_anterior(linha, coluna)

def resolve_jogo():
    global soma_total
    inicializa_auxiliares()

    turno = 1
    nivel = 1
    max_nivel = 1

    linha, coluna = 0,0
    valor_atual = 0

    while True:
        if nivel > max_nivel:
            max_nivel = nivel
            print (f'Turno {turno} | Nivel {nivel} | Max Nivel {max_nivel}')
            imprime_tabuleiro(tabuleiro)

        numero = decide_jogada(valor_atual)
        if numero is None:
            nivel -= 1
            linha, coluna = desfaz_jogada(tabuleiro,linha, coluna)
            valor_atual = tabuleiro[linha][coluna]

            soma_total -= valor_atual

            quadrante = pega_quadrante(linha, coluna)
            conjuntos_linhas[linha].discard(valor_atual)
            conjuntos_colunas[coluna].discard(valor_atual)
            conjuntos_quadrantes[quadrante-1].discard(valor_atual)

            continue

        valor_atual = numero

        # print (f'jogada: {linha}, {coluna}, {numero}')

        if not executa_jogada(linha, coluna, numero):
            continue

        soma_total += numero

        quadrante = pega_quadrante(linha, coluna)
        conjuntos_linhas[linha].add(valor_atual)
        conjuntos_colunas[coluna].add(valor_atual)
        conjuntos_quadrantes[quadrante-1].add(valor_atual)

        # imprime_tabuleiro(tabuleiro)
        if verifica_fim_jogo() == True:
            print (f'Turno {turno} | Nivel {nivel} | Max Nivel {max_nivel}')
            imprime_tabuleiro(tabuleiro)
            print ('Parabens você ganhou o jogo!')
            break

        linha, coluna = pega_proxima_posicao(linha, coluna)
        # print (f'proxima posiçao: {linha},{coluna}')
        valor_atual = 0
        turno += 1
        nivel += 1


        if turno == 30000000:
            break

if __name__ == '__main__':
    print ("Começando o jogo...")

    # inicia_jogo()

    tempo_inicio = time.time()
    resolve_jogo()
    print (time.time() - tempo_inicio)