"""
Cédulas

Leia um valor inteiro. A seguir, calcule o menor 
número de notas possíveis (cédulas) no qual o valor
pode ser decomposto. As notas consideradas são de 
100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor 
lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N 
(0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade 
mínima de notas de cada tipo necessárias, conforme 
o exemplo fornecido. Não esqueça de imprimir o fim 
de linha após cada linha, caso contrário seu 
programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	
576

Exemplo de Saída
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""

# valor = int(input())

# nota_100 = valor // 100 
# resto_100 = valor % 100
# nota_50 = resto_100 // 50
# resto_50 = resto_100 % 50
# nota_20 = resto_50 // 20
# resto_20 = resto_50 % 20
# nota_10 = resto_20 // 10
# resto_10 = resto_20 % 10
# nota_5 = resto_10 // 5
# resto_5 = resto_10 % 5
# nota_2 = resto_5 // 2
# resto_2 = resto_5 % 2
# nota_1 = resto_2 // 1

# print(valor)
# print(f'{nota_100} nota(s) de R$ 100,00')
# print(f'{nota_50} nota(s) de R$ 50,00')
# print(f'{nota_20} nota(s) de R$ 20,00')
# print(f'{nota_10} nota(s) de R$ 10,00')
# print(f'{nota_5} nota(s) de R$ 5,00')
# print(f'{nota_2} nota(s) de R$ 2,00')
# print(f'{nota_1} nota(s) de R$ 1,00')

entrada = int(input())

lista_notas = [100, 50, 20, 10, 5, 2, 1]
lista_inteiro = []
indice = 0
valor_resto = entrada

while indice < 7:
    lista_inteiro.append(valor_resto // lista_notas[indice])
    valor_resto = valor_resto % lista_notas[indice]
    indice += 1

print(entrada)
indice2 = 0
while indice2 < 7:
    print(f'{lista_inteiro[indice2]} nota(s) de R$ {lista_notas[indice2]},00')
    indice2 += 1