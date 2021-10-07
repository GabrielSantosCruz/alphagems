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

    x = matriz[current_m-1][current_n-1]
    y = matriz[finale_m-1][finale_n-1]
    matriz[current_m-1][current_n-1] = y
    matriz[finale_m-1][finale_n-1] = x
    
    return matriz

def break_gens_line(matriz, size): # quebra de gemas nas linhas
    for i in range(size):
            quant = 1
            for j in range(size):
                if j > 0:   # para corrigir o erro de Index saindo do range
                    if matriz[i][j] == matriz[i][j-1]: 
                        quant +=1
                        if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
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

def break_gens_colune(matriz, size): # quebra de gemas na coluna
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

def punctuation(matriz, size, point): # calcula a pontuação do jogo
    for i in range(size):            
            for j in range(size):
                if matriz[i][j] == ' ':
                    point += 1

    print(f'Pontos: {point}')
    # provavelmente quando a gravidade for adicionada corretamente deve ter que retornar "point"

def gravity(matriz, size): # só faz uma verificação
    from random import choice
    condition = True
    quant = 0
    
    for i in range(size): # faz as gemas cairem
        for j in range(size-1, 0, -1):
            for k in range(size-1, -1, -1):
                if matriz[j][k] == ' ':
                    #condition = True
                    matriz[j][k], matriz[j-1][k] = matriz[j-1][k], matriz[j][k]
    
def validation_in_matriz(matriz, size):
    for i in range(size): # para conferir se há mais permutações para fazer
        for j in range(size):
            if matriz[i][j] == ' ':
                quant += 1

    return matriz

def generate_in_line(matriz, size):
    from random import choice

    for i in range(size):
        if matriz[0][i] == ' ':
            y = choice(colors[0:size])
            matriz[0][i] = y
    
    return matriz

def verfication(matriz, size):
    quant = 0
    for i in range(size):
        for j in range(size):
            if matriz[i][j] == ' ':
                quant += 1
    if quant > 0:
        return True
    else:
        return False

def parar_de_cair(matriz, size, point):
    a = True
    while a:
        matriz = break_gens_line(matriz, size)
        matriz = break_gens_colune(matriz, size)
        punctuation(matriz, size, point)
        matriz = gravity(matriz, size)
        matriz = generate_in_line(matriz, size)
        a = verfication(matriz, size)
    return matriz