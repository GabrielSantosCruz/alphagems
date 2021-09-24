def gerar_matriz(n, o): #gera uma matriz já preenchida com letras aleatórias
    # n é o tamanho da matriz
    # o é a quantidade de "cores"
    import string
    from random import choice
    cores = ['A','B','C','D','E','F','G','H','I','J']

    cores = cores[0:o] # lista com as cores

    linha = [0] * n # cria a quantidade de colunas
    matriz = [linha] * n # cria a quantidade de linhas

    for l in range(n):
        linha = []
        for c in range(n):
            x = choice(cores) # criar as letras aleatórias a partir de uma lista
            linha.append(x)
        matriz[l] = linha

    for i in range(n): # printa a matriz linha por linha
        print(matriz[i])
    return matriz

def verificacao_int_matriz(num): # verificar se o número digitado é inteiro
    while not num.isdigit() or len(num) == 0 or int(num) > 10 or int(num) < 3:
        num = input("Erro! Digite um valor válido: ")
    return int(num) # retorna o número já convertido

def verificar_int(num):
    while not num.isdigit() or len(num) == 0 or int(num) <= 0:
        num = input("Erro! Digite um valor válido: ")
    return int(num) # retorna o número já convertido
    
def quantidade_cores(num): # cria uma lista com letras
    letras = ['A','B','C','D','E','F','G','H','I','J']
    cores = []
    for i in range(num):
        cores.append(letras[i])
    print(cores)