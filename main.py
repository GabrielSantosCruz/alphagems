'''*******************************************************************************
Autor: Gabriel Santos Cruz
Componente Curricular: Algoritmos I
Concluido em: xx/xx/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
O código e sua evolução pode ser encontrado em: https://github.com/GabrielSantosCruz/alphagens
******************************************************************************************/'''
from biblioteca_de_funcoes import *

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

m = check_number_matriz(input('Digite o tamanho da matriz: '))
n = check_number_matriz(input('Digite a quantidade de cores: '))
p = build_matriz(m, n)

while True:
    for i in range(m):
        quant = 1
        for j in range(m-1):
            if p[i][j] == p[i][j+1]:
                quant += 1
            if quant == 3:
                p[i][j-3] = p[i][j-2] = p[i][j-1] = 0
    print('='*50)
    print_matriz(p)

    atual_m = check_int(input("Digite a linha atual: "))
    atual_n = check_int(input("Digite a coluna atual: "))
    final_m = check_int(input("Digite a linha final: "))
    final_n = check_int(input("Digite a coluna final: "))
    print(f'iten selecionado: {p[atual_m][atual_n]}') # consigo printar o iten que eu quero

    x = p[atual_m][atual_n]
    y = p[final_m][final_n]
    p[atual_m][atual_n] = y
    p[final_m][final_n] = x
    print('='*50)
    print_matriz(p)
    print("Apos juntar 3: ")
    '''if p[0][0] == p[0][1] == p[0][2]:
        p[0][0] = p[0][1] = p[0][2] = 0'''
        
    print_matriz(p)
    #verificar se foi ponto

    '''colors = ['A','B','C','D','E','F','G','H','I','J']
    for i in range(m):
        for j in range(m):
            if p[i][j] == 0:
                p[i][j] = choice(colors)'''