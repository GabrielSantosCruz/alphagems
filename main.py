from biblioteca_de_funcoes import *
m =  check_int(input('Digite o tamanho da matriz: '))
n = check_int(input('Digite a quantidade de cores: '))
p = build_matriz(m, n)

print_m = check_int(input("Digite a linha que deseja printar: "))
print_n = check_int(input('Digite o iten que deseja printar: '))
print(p[print_m][print_n]) # consigo printar o iten que eu quero