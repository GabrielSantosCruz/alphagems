'''/*******************************************************************************
Autor: Gabriel Santos Cruz
Componente Curricular: Algoritmos I
Concluido em: xx/10/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
O código e sua evolução pode ser encontrado em: https://github.com/GabrielSantosCruz/alphagens
******************************************************************************************/'''
from os import system
from biblioteca_de_funcoes import *

menu()

#size = check_number_matriz(input('Digite o tamanho da matriz: '))
size = 3
matriz = build_matriz(size)
'''matriz = [
['C', 'A', 'C'],
['C', 'B', 'A'],
['B', 'A', 'C']]'''
'''matriz = [
['B', 'C', 'B'],
['B', 'A', 'B'],
['A', 'A', 'C']]'''

    
print_matriz(matriz)
point = 0

a = tips(matriz, size)

while a:
    #system("cls")

    while check_points(matriz, size): 
        break_gens(matriz, size)
        point = punctuation(matriz, size, point)
        smash(matriz, size)
        gravity(matriz, size)
        generate_in_line(matriz, size)
        print(point)
        print_matriz(matriz)
    a = tips(matriz, size)
    
    option = validation_of_opition(str(input('Aperte M para mover ou D para dicas [M/D]: ').upper()))
    
    if option == 'D':
        c, linha, coluna = tips(matriz, size)
        print(f'Dica: {linha+1}.{coluna+1}')

    elif option == 'M':
        current_m = check_int(input("Digite a linha atual: "))
        current_n = check_int(input("Digite a coluna atual: "))
        finale_m = check_int(input("Digite a linha final: "))
        finale_n = check_int(input("Digite a coluna final: "))
        matriz = permutation(current_m, current_n, finale_m, finale_n, matriz, size)

print(f'''
░██████╗░░█████╗░███╗░░░███╗███████╗  
██╔════╝░██╔══██╗████╗░████║██╔════╝  
██║░░██╗░███████║██╔████╔██║█████╗░░  
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  

░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
Sua pontuação foi: {point}''')
    # me falaram um nome que em alguns momentos me deu vontade de colocar no jogo (Candy crise)