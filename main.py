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
from time import sleep
from biblioteca_de_funcoes import *

home_menu()
option_menu = validation_of_menu(input('Digite a opção desejada: '))

while option_menu != 3:

    if option_menu == 1:
        point = 0
        option = 'm'
        size = check_number_matriz(input('Digite o tamanho da matriz: '))
        matriz = build_matriz(size)
        sleep(1)
        system("cls")
        print_matriz(matriz)
        a = tips(matriz, size)
        while a:

            while check_points(matriz, size):
                
                break_gens(matriz, size)
                sleep(0.5)
                system("cls")
                print_matriz(matriz)
                point = punctuation(matriz, size, point)
                smash(matriz, size)
                sleep(0.5)
                system("cls")
                print_matriz(matriz)
                gravity(matriz, size)
                sleep(0.5)
                system("cls")
                print_matriz(matriz)
                generate_in_line(matriz, size)
                sleep(0.5)
                system("cls")
                print_matriz(matriz)
                print(f'Pontos: {point}')
                sleep(0.5)
                system("cls")
                print_matriz(matriz)
                print(f'Pontos: {point}')

            a = tips(matriz, size)

            if a: # para caso não houverem mais movimentos ele parar o loop de uma vez
                option = validation_of_opition(str(input('Aperte M para mover ou D para dicas [M/D]: ').upper()))

            if (option == 'D') and (point > 0) and a:
                c, linha, coluna = tips(matriz, size)
                sleep(0.5)
                system("cls")
                point -= 1
                print_matriz(matriz)
                print(f'Pontos: {point}')
                print(f'Dica: {linha+1}.{coluna+1}')

            elif (option == 'M') and a: # para caso não houverem mais movimentos ele parar o loop de uma vez
                current_m = check_permutation(input("Digite a linha atual: "),size)
                current_n = check_permutation(input("Digite a coluna atual: "), size)
                finale_m = check_permutation(input("Digite a linha final: "),size)
                finale_n = check_permutation(input("Digite a coluna final: "),size)
                matriz = permutation(current_m, current_n, finale_m, finale_n, matriz, size)
                #if not check_points(matriz, size):

        final_menu()
        print(f'Sua pontuação total foi: {point}')
        play_again = input('Deseja jogar novamente? [S/N]: ').upper()
        if play_again == 'S':
            option_menu = 1
            # me falaram um nome que em alguns momentos me deu vontade de colocar no jogo (Candy crise)

    elif option_menu == 2:
        sleep(0.5)
        system('cls')
        print('''
        A permutação do jogo funciona com base nas cordenadas das peças

                    1    2    3    4    5
                1 ['H', 'B', 'E', 'H', 'H']
                2 ['C', 'H', 'E', 'G', 'C']
                3 ['A', 'D', 'F', 'A', 'B']
                4 ['E', 'I', 'C', 'F', 'H']
                5 ['H', 'G', 'F', 'B', 'H']
                
        EX: 
        Digite a linha atual: 4
        Digite a coluna atual: 4
        Digite a linha final: 4
        Digite a coluna final: 3

                    1    2    3    4    5
                1 ['H', 'B', 'E', 'H', 'H']
                2 ['C', 'H', 'E', 'G', 'C']
                3 ['A', 'D', 'F', 'A', 'B']
                4 ['E', 'I', 'F', 'C', 'H']
                5 ['H', 'G', 'F', 'B', 'H']
                
        Dicas também podem ser solicitadas em troco de 1 ponto da pontuação total
        As dicas mostram a posição da peço que pode ser permutada para fazer pontos''')
        input('\n       Pressione Enter para voltar')
        sleep(0.5)
        system('cls')