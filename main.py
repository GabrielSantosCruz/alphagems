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
#size = 5
#matriz = build_matriz(size)
'''matriz = [
['C', 'D', 'D', 'A', 'D'],
['A', 'A', 'A', 'C', 'D'],
['A', 'B', 'D', 'A', 'A'],
['E', 'A', 'D', 'D', 'D'],
['D', 'A', 'B', 'E', 'C']]'''
'''matriz = [
['C', 'C', 'E', 'E', 'B'],
['C', 'D', 'E', 'A', 'D'],
['A', 'B', 'D', 'C', 'D'],
['E', 'A', 'C', 'A', 'A'],
['D', 'A', 'B', 'E', 'C']]'''

point = 0

while True:
    print_matriz(matriz)
    print('=~'*25)
    #system("cls")
    b = check_points(matriz, size)
    while b: # tenho que fazer entrar nesse loop
        break_gens(matriz, size)
        point = punctuation(matriz, size, point)
        smash(matriz, size)
        gravity(matriz, size)
        generate_in_line(matriz, size)
        print_matriz(matriz)
        print('=~'*25)
        b = check_points(matriz, size)

    print_matriz(matriz)
    current_m = check_int(input("Digite a linha atual: "))
    current_n = check_int(input("Digite a coluna atual: "))
    finale_m = check_int(input("Digite a linha final: "))
    finale_n = check_int(input("Digite a coluna final: "))
    matriz = permutation(current_m, current_n, finale_m, finale_n, matriz, size)
    
    # me falaram um nome que em alguns momentos me deu vontade de colocar no jogo (Candy crise)