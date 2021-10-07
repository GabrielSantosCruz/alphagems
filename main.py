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

m = check_number_matriz(input('Digite o tamanho da matriz: '))
p = build_matriz(m)

point = 0

while True:
    print_matriz(p)
    print('='*50)
    system("cls")
    a = True
    while a:
        matriz = break_gens_line(p, m)
        matriz = break_gens_colune(p, m)
        print_matriz(p)
        print('='*50)        
        punctuation(p, m, point)
        matriz = gravity(p, m)
        matriz = generate_in_line(p, m)
        print_matriz(p)
        print('='*50)
        a = verfication(p, m)

    print_matriz(p)
    current_m = check_int(input("Digite a linha atual: "))
    current_n = check_int(input("Digite a coluna atual: "))
    finale_m = check_int(input("Digite a linha final: "))
    finale_n = check_int(input("Digite a coluna final: "))
    p = permutation(current_m, current_n, finale_m, finale_n, matriz)