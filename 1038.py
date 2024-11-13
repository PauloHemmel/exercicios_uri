# Lanche

# Com base na tabela abaixo, escreva um programa que
# leia o código de um item e a quantidade deste item.
# A seguir, calcule e mostre o valor da conta a pagar.

# Entrada
# O arquivo de entrada contém dois valores inteiros
# correspondentes ao código e à quantidade de um item
# conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ "
# seguido pelo valor a ser pago, com 2 casas após o ponto
# decimal.

# Exemplo de Entrada
# 3 2

# Exemplo de Saída
# Total: R$ 10.00

# Exemplo de Entrada
# 4 3
# Exemplo de Saída
# Total: R$ 6.00


lista_quantidade = [4.00, 4.50, 5.00, 2.00, 1.50]

codigo, quantidade = map(int, input().split())

if codigo == 1:
    print('Total: R$ ' f'{quantidade * (lista_quantidade[0]):.2f}')
elif codigo == 2:
    print('Total: R$ ' f'{quantidade * (lista_quantidade[1]):.2f}')
elif codigo == 3:
    print('Total: R$ ' f'{quantidade * (lista_quantidade[2]):.2f}')
elif codigo == 4:
    print('Total: R$ ' f'{quantidade * (lista_quantidade[3]):.2f}')
elif codigo == 5:
    print('Total: R$ ' f'{quantidade * (lista_quantidade[4]):.2f}')
