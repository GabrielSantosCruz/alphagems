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
n = check_number_matriz(input('Digite a quantidade de cores: '))
p = build_matriz(m, n)

while True:
    print('='*50)
    p = break_gens_line(p, m)
    p = break_gens_colune(p, m)
    print_matriz(p)
    current_m = check_int(input("Digite a linha atual: "))
    current_n = check_int(input("Digite a coluna atual: "))
    finale_m = check_int(input("Digite a linha final: "))
    finale_n = check_int(input("Digite a coluna final: "))
    p = permutation(current_m, current_n, finale_m, finale_n, p)
    system("cls") # limpar a tela do terminal a cada loop para não poluí-la