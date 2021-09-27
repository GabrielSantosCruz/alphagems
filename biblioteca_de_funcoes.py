def menu():
    print('''
░█████╗░██╗░░░░░██████╗░██╗░░██╗░█████╗░░██████╗░███████╗███╗░░██╗░██████╗
██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔══██╗██╔════╝░██╔════╝████╗░██║██╔════╝
███████║██║░░░░░██████╔╝███████║███████║██║░░██╗░█████╗░░██╔██╗██║╚█████╗░
██╔══██║██║░░░░░██╔═══╝░██╔══██║██╔══██║██║░░╚██╗██╔══╝░░██║╚████║░╚═══██╗
██║░░██║███████╗██║░░░░░██║░░██║██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░
==========================================================================
  #     ==     *    -      @       __    #       **     -_     %     $   %      
      *     -    *    |--------------------------|  #  -    *   --      @ 
   *        #         |     1 - Jogar            |      *       -    #   
      @       *       |     2 - Tutorial         | @     -   #      ==   *
          #       *   |     3 - Sair             |     #   -  *    %    -
    @     -    *   %  |--------------------------|   %     -    @      #    
''')

def build_matriz(size, quant_colors): #gera uma matriz já preenchida com letras aleatórias
    # n é o tamanho da matriz
    # o é a quantidade de "colors"
    import string
    from random import choice
    colors = ['A','B','C','D','E','F','G','H','I','J']

    colors = colors[0:quant_colors] # lista com as cores

    line = [0] * size # cria a quantidade de colunas
    matriz = [line] * size # cria a quantidade de linhas

    for l in range(size):
        line = []
        for c in range(size):
            x = choice(colors) # criar as letras aleatórias a partir de uma lista
            line.append(x)
        matriz[l] = line

    for i in range(size): # printa a matriz linha por linha
        print(matriz[i])
    return matriz

def check_number_matriz(number): # verificar se o número digitado é inteiro
    while not number.isdigit() or len(number) == 0 or int(number) > 10 or int(number) < 3:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido

def check_int(number):
    while not number.isdigit() or len(number) == 0 or int(number) < 0:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido
    
def amount_colors(number): # cria uma lista com letras
    letras = ['A','B','C','D','E','F','G','H','I','J']
    colors = []
    for i in range(number):
        colors.append(letras[i])
    return colors
    print(colors)

def print_matriz(matriz): # printa matruz recebida como parâmetro
    for i in range(len(matriz)): # printa a matriz linha por linha
        print(matriz[i])

def permutation(matriz): # realiza a permutação dos itens da matriz
    current_m = check_int(input("Digite a linha atual: "))
    current_n = check_int(input("Digite a coluna atual: "))
    finale_m = check_int(input("Digite a linha final: "))
    finale_n = check_int(input("Digite a coluna final: "))
    x = matriz[current_m][current_n]
    y = matriz[finale_m][finale_n]
    matriz[atual_m][atual_n] = y
    matriz[finale_m][finale_n] = x
    return matriz
#def validate_moviment():

def break_gens(matriz, tamanho):
    for i in range(tamanho+1):
            quant = 1
            for j in range(tamanho+1):
  
                if j > 0:
                    if matriz[i][j] == matriz[i][j-1]:
                        quant +=1
                    else:
                        if quant >= 3:
                            for k in range(1, quant+1):                            
                                matriz[i][j-k] = ' '
                            quant = 1
    return matriz