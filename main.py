from biblioteca_de_funcoes import *
print('''

░█████╗░██╗░░░░░██████╗░██╗░░██╗░█████╗░░██████╗░███████╗███╗░░██╗░██████╗
██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔══██╗██╔════╝░██╔════╝████╗░██║██╔════╝
███████║██║░░░░░██████╔╝███████║███████║██║░░██╗░█████╗░░██╔██╗██║╚█████╗░
██╔══██║██║░░░░░██╔═══╝░██╔══██║██╔══██║██║░░╚██╗██╔══╝░░██║╚████║░╚═══██╗
██║░░██║███████╗██║░░░░░██║░░██║██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░
==========================================================================
    *   - *    |--------------------------|  # -   *   --     @ 
  *      #     | 1 - Jogar                |     *   -  #   
    @   *      | 2 - Tutorial             | @ -   #      ==   *
       #    *  | 3 - Sair                 |    #  -  *   %    -
 @  -   *   %  |--------------------------|   %   - @     #         
''')

m =  check_int(input('Digite o tamanho da matriz: '))
n = check_int(input('Digite a quantidade de cores: '))
p = build_matriz(m, n)

while True:

    atual_m = check_int(input("Digite a linha atual: "))
    atual_n = check_int(input('Digite a coluna atual: '))
    final_m = check_int(input("Digite a linha final: "))
    final_n = check_int(input("Digite a coluna final: "))
    print(f'iten selecionado: {p[atual_m][atual_n]}') # consigo printar o iten que eu quero

    x = p[atual_m][atual_n]
    y = p[final_m][final_n]
    p[atual_m][atual_n] = y
    p[final_m][final_n] = x

    print_matriz(p)
    print("Apos juntar 3: ")
    if p[0][0] == p[0][1] == p[0][2]:
        p[0][0] = p[0][1] = p[0][2] = 0
    print_matriz(p)