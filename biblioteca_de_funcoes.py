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
colors = ['A','B','C','D','E','F','G','H','I','J']
def build_matriz(size): #gera uma matriz já preenchida com letras aleatórias

    from random import choice
    colors = ['A','B','C','D','E','F','G','H','I','J']

    colors = colors[0:size] # lista com as cores

    line = [0] * size # cria a quantidade de colunas
    matriz = [line] * size # cria a quantidade de linhas

    for l in range(size):
        line = []
        for c in range(size):
            x = choice(colors) # sorteia as letras a partir de uma lista
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
    return colors

def print_matriz(matriz): # printa matruz recebida como parâmetro
    for i in range(len(matriz)): # printa a matriz linha por linha
        print(matriz[i])
        
def permutation(current_m, current_n, finale_m, finale_n, matriz): # realiza a permutação dos itens da matriz
    '''while ((finale_m - current_m != 0) and (finale_n - current_n != 0)) or ((abs(current_m - finale_m) != 1) and (current_m != current_n)) or ((abs(current_n - finale_n != 1) and (current_n != finale_n))):
        print("Erro! Permutação inválida!")
        finale_m = check_int(input("Digite a linha final: "))
        finale_n = check_int(input("Digite a coluna final: "))''' # como essa parte da verificação ainda está dando erro eu não ativei
        # Quando a linha incial e final são iguais da erro

    x = matriz[current_m][current_n]
    y = matriz[finale_m][finale_n]
    matriz[current_m][current_n] = y
    matriz[finale_m][finale_n] = x
    return matriz

def break_gens_line(matriz, tamanho):
    for i in range(tamanho):
            quant = 1
            for j in range(tamanho):
                if j > 0:   # para corrigir o erro de Index saindo do range
                    if matriz[i][j] == matriz[i][j-1]: 
                        quant +=1
                        if quant >= 3 and (j == (tamanho-1)): # para quando houver de quebrar gemas nas bordas
                            for k in range(1, quant+1):                      
                                matriz[i][(j+1)-k] = ' '
                            quant = 1                    
                    else:
                        if quant >= 3:
                            for k in range(1, quant+1):                            
                                matriz[i][j-k] = ' '
                            quant = 1
                        else:
                            quant = 1
    return matriz

def break_gens_colune(matriz, size):
    for i in range(size):
            quant = 1
            for j in range(size):

                if j > 0: 
                    if matriz[j][i] == matriz[j-1][i]:
                        quant +=1
                        if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
                            for k in range(1, quant+1):                      
                                matriz[(j+1)-k][i] = ' '
                            quant = 1
                   
                    else:
                        if quant >= 3:
                            for k in range(1, quant+1):                         
                                matriz[j-k][i] = ' '
                            quant = 1
                        else:
                            quant = 1
    return matriz

def punctuation(matriz, size, point):
    for i in range(size):            
            for j in range(size):
                if matriz[i][j] == ' ':
                    point += 1

    print(f'Pontos: {point}')
    return matriz

def fall(matriz, size):
    for i in range(size):
        for j in range(size-1, 0, -1):
            for k in range(size-1, -1, -1):
                if matriz[j][k] == ' ':
                    matriz[j][k], matriz[j-1][k] = matriz[j-1][k], matriz[j][k]
    
    return matriz

def generate(matriz, size):
    
    from random import choice

    for i in range(size):
        if matriz[0][i] == ' ':
            y = choice(colors[0:size])
            matriz[0][i] = y
    
    return matriz