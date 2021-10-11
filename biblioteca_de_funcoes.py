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
    linha = [0] * size
    matriz = [linha] * size

    for l in range(size):
        line = []
        for c in range(size):
            x = choice(colors) # sorteia as letras a partir de uma lista
            line.append(x) # adiciona a letra sorteada a lista
        matriz[l] = line # adiciona a lista a matriz

    return matriz

def check_number_matriz(number): # verificar se o número digitado é inteiro
    while not number.isdigit() or len(number) == 0 or int(number) > 10 or int(number) < 3:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido

def check_int(number):
    while not number.isdigit() or len(number) == 0 or int(number) < 0:
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido

def check_permutation(number, size):
    while not number.isdigit() or len(number) == 0 or int(number) < 0 or (int(number) > size):
        number = input("Erro! Digite um valor válido: ")
    return int(number) # retorna o número já convertido 

def print_matriz(matriz): # printa a matriz recebida
    for i in range(len(matriz)): # printa a matriz linha por linha
        print(matriz[i])
        
def permutation(current_m, current_n, finale_m, finale_n, matriz, size): # realiza a permutação dos itens da matriz
    while (finale_m != (current_m + 1)) and (finale_m != (current_m - 1)) and (current_m != finale_m):
        print("Erro! Permutação inválida!")
        current_m = check_permutation(number(input("Digite a linha atual: ")), size)
        current_n = check_permutation((input("Digite a coluna atual: ")), size)
        finale_m = check_permutation((input("Digite a linha final: ")), size)
        finale_n = check_permutation((input("Digite a coluna final: ")), size) 
        # Quando a linha incial e final são iguais da erro

    while (finale_n != (current_n + 1)) and (finale_n != (current_n - 1)) and (current_n != finale_n):
        print("Erro! Permutação inválida!")
        current_m = check_permutation((input("Digite a linha atual: ")), size)
        current_n = check_permutation((input("Digite a coluna atual: ")), size)
        finale_m = check_permutation((input("Digite a linha final: ")), size)
        finale_n = check_permutation((input("Digite a coluna final: ")), size) 
        # Quando a linha incial e final são iguais da erro
        
    x = matriz[current_m-1][current_n-1]
    y = matriz[finale_m-1][finale_n-1]
    matriz[current_m-1][current_n-1] = y
    matriz[finale_m-1][finale_n-1] = x
    # parte responsável por fazer as trocas das gemas
    return matriz

def break_gens(matriz, size): # quebra as gemas
    for i in range(size):
        quant = 1
        for j in range(size):
            if j > 0:   # para corrigir o erro de Index saindo do range
                if (matriz[i][j] == matriz[i][j-1]) or (matriz[i][j].lower() == matriz[i][j-1]): 
                    quant +=1
                    if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
                        for k in range(1, quant+1):                      
                            matriz[i][(j+1)-k] = matriz[i][(j+1)-k].lower()
                        quant = 1                    
                else:
                    if quant >= 3:
                        for k in range(1, quant+1):                            
                            matriz[i][j-k] = matriz[i][j-k].lower()
                        quant = 1
                    else:
                        quant = 1
    
    for i in range(size):
            quant = 1
            for j in range(size):

                if j > 0: # para corrigir o erro de Index saindo do range
                    if (matriz[j][i] == matriz[j-1][i]) or (matriz[j][i].lower() == matriz[j-1][i]):
                        quant +=1
                        if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
                            for k in range(1, quant+1):                      
                                matriz[(j+1)-k][i] = matriz[(j+1)-k][i].lower()
                            quant = 1
                   
                    else:
                        if quant >= 3:
                            for k in range(1, quant+1):                         
                                matriz[j-k][i] = matriz[j-k][i].lower()
                            quant = 1
                        else:
                            quant = 1
    return matriz

def punctuation(matriz, size, point): # calcula a pontuação do jogo
    for i in range(size):            
            for j in range(size):
                if matriz[i][j] == matriz[i][j].lower():
                    point += 1

    print(f'Pontos: {point}')
    return point

def smash(matriz, size): # quebra as gemas transformadas em letras minúsculas após a união de 3 ou mais
    for i in range(size):            
        for j in range(size):
            if matriz[i][j].islower(): # compara linha por linha se está minúscula
                matriz[i][j] = ' '
    
    return matriz

def gravity(matriz, size): # faz as gemas cairem
    quant = 0

    for i in range(size):
        for j in range(size-1, 0, -1):
            for k in range(size-1, -1, -1):
                if matriz[j][k] == ' ':
                    matriz[j][k], matriz[j-1][k] = matriz[j-1][k], matriz[j][k]
    
def validation_in_matriz(matriz, size):
    for i in range(size): # para conferir se há mais permutações para fazer
        for j in range(size):
            if matriz[i][j] == ' ':
                quant += 1

    return matriz

def generate_in_line(matriz, size): # preenche todo o tabuleiro após a gravidade agir
    from random import choice
    colors = ['A','B','C','D','E','F','G','H','I','J']
    
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            if matriz[i][j] == ' ':
                y = choice(colors[0:size])
                matriz[i][j] = y
    
    return matriz

def verfication(matriz, size): # verifica se há espaços em branco na matriz
    quant = 0
    for i in range(size):
        for j in range(size):
            if matriz[i][j] == ' ':
                quant += 1
    if quant > 0:
        return True
    else:
        return False

def check_points(matriz, size):
    for i in range(size):
        quant = 1
        for j in range(size):
            if j > 0:   # para corrigir o erro de Index saindo do range
                if (matriz[i][j] == matriz[i][j-1]) or (matriz[i][j].lower() == matriz[i][j-1]): 
                    quant +=1
                    if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
                        for k in range(1, quant+1):                      
                            quant = 1 
                            return True
                                           
                else:
                    if quant >= 3:
                        for k in range(1, quant+1):                            
                            quant = 1
                            return True
                            
                    else:
                        return False
    
    for i in range(size):
            quant = 1
            for j in range(size):

                if j > 0: # para corrigir o erro de Index saindo do range
                    if (matriz[j][i] == matriz[j-1][i]) or (matriz[j][i].lower() == matriz[j-1][i]):
                        quant +=1
                        if quant >= 3 and (j == (size-1)): # para quando houver de quebrar gemas nas bordas
                            for k in range(1, quant+1):                      
                                matriz[(j+1)-k][i] = matriz[(j+1)-k][i].lower()
                            quant = 1
                   
                    else:
                        if quant >= 3:
                            for k in range(1, quant+1):                         
                                matriz[j-k][i] = matriz[j-k][i].lower()
                            quant = 1
                        else:
                            quant = 1

def tips(matriz, size): # diz as dicas do jogo
    for i in range(size):
        quant = 1
        for j in range(size):
            if ((i == 0) and (j > 0)) and (j < (size - 2)): # para quebras na primeira linha da horizontal na frente
                if matriz[i][j] == matriz[i][j-1]:
                    if matriz[i][j] == matriz[i+1][j+1]:
                        print(f'Dica: {i+2}.{j+2}')  
                    if matriz[i][j] == matriz[i][j+2]: # erro de index
                        print(f'Dica: {i+1}.{j+3}')                                          
            if (j > 0) and (j < (size-1)) and ((i > 0) and (i < (size-1))): # quebras no meio da horizontal na frente
                if matriz[i][j] == matriz[i][j-1]: 
                    if matriz[i][j] == matriz[i-1][j+1]:
                        print(f'Dica: {i}.{j+2}')
                    if matriz[i][j] == matriz[i+1][j+1]:
                        print(f'Dica: {i+2}.{j+2}')
                    if matriz[i][j] == matriz[i][j+2]:
                        print(f'Dica: {i+1}.{j+3}')
            if ((i == (size - 1)) and (j > 0)) and (j < (size - 1)): # quebras na linha final da horizontal na frente
                if matriz[i][j] == matriz[i][j-1]:
                    if matriz[i][j] == matriz[i-1][j+1]:
                        print(f'Dica: {i}.{j+2}')
                    if matriz[i][j] == matriz[i][j+2]:
                        print(f'Dica: {i+1}.{j+3}')
            if (j > 0) and (i == 0): # para quebras na primeira linha da horizontal atrás
                if matriz[i][j] == matriz[i][j-1]:
                    if matriz[i][j-1] == matriz[i+1][j-2]:
                        print(f'Dica: {i+2}.{j-1}')