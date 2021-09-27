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
menu()

m = check_number_matriz(input('Digite o tamanho da matriz: '))
n = check_number_matriz(input('Digite a quantidade de cores: '))
p = build_matriz(m, n)

while True:
    print('='*50)
    p = permutation(p)
    print('='*50)
    print_matriz(p)
    print("Apos juntar 3: ")
    print_matriz(p)