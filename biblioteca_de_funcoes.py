def Build_Matriz(n, o): #gera uma matriz já preenchida com letras aleatórias
    # n é o tamanho da matriz
    # o é a quantidade de "colors"
    import string
    from random import choice
    colors = ['A','B','C','D','E','F','G','H','I','J']

    colors = colors[0:o] # lista com as cores

    line = [0] * n # cria a quantidade de colunas
    matriz = [line] * n # cria a quantidade de linhas

    for l in range(n):
        line = []
        for c in range(n):
            x = choice(colors) # criar as letras aleatórias a partir de uma lista
            line.append(x)
        matriz[l] = line

    for i in range(n): # printa a matriz linha por linha
        print(matriz[i])
    return matriz

def check_number_matriz(number): # verificar se o número digitado é inteiro
    while not number.isdigit() or len(number) == 0 or int(number) > 10 or int(number) < 3:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido

def check_int(number):
    while not number.isdigit() or len(number) == 0 or int(number) <= 0:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido
    
def amount_colors(number): # cria uma lista com letras
    letras = ['A','B','C','D','E','F','G','H','I','J']
    colors = []
    for i in range(number):
        colors.append(letras[i])
    print(colors)