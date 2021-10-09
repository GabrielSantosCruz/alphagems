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

size = check_number_matriz(input('Digite o tamanho da matriz: '))
p = build_matriz(size)
'''p = [
['B', 'F', 'B', 'D', 'D', 'G', 'C'],
['E', 'E', 'E', 'F', 'F', 'C', 'D'],
['E', 'G', 'C', 'G', 'A', 'E', 'E'],
['F', 'A', 'G', 'F', 'B', 'E', 'A'],
['D', 'D', 'G', 'B', 'F', 'D', 'C'],
['A', 'E', 'G', 'E', 'A', 'C', 'E'],
['A', 'A', 'C', 'C', 'D', 'D', 'B']]'''
point = 0

while True:
    print_matriz(p)
    print('='*50)
    #system("cls")
    a = True
    b = True
    while (a and b):
        matriz = break_gens_line(p, size)
        matriz = break_gens_colune(p, size)
        point = punctuation(p, size, point)
        matriz = gravity(p, size)
        matriz = generate_in_line(p, size)
        a = verfication(p, size)
        b = check_points(p, size)

    print_matriz(p)
    current_m = check_int(input("Digite a linha atual: "))
    current_n = check_int(input("Digite a coluna atual: "))
    finale_m = check_int(input("Digite a linha final: "))
    finale_n = check_int(input("Digite a coluna final: "))
    p = permutation(current_m, current_n, finale_m, finale_n, matriz, size  )
    
    # me falaram um nome que em alguns momentos me deu vontade de colocar no jogo (Candy crise)