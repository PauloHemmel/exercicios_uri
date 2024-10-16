"""

Fórmula de Bhaskara

Leia 3 valores de ponto flutuante e efetue o 
cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre
a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes,
apresente a mensagem "Impossivel calcular". Caso
contrário, imprima o resultado das raízes com 5
dígitos após o ponto, com uma mensagem correspondente
conforme exemplo abaixo. Imprima sempre o final de
linha após cada mensagem.

Exemplos de Entrada	
10.0 20.1 5.1

Exemplos de Saída
R1 = -0.29788
R2 = -1.71212
"""

a, b, c = map(float, input().split())

delta = (b ** 2) - 4 * a * c
raiz_quadrada = delta ** 0.5
divisao = (2 * a)

try:
    if delta < 0:
        print('Impossivel calcular')

    else:
        
        raiz1 = (-b + raiz_quadrada)/ (2 * a)
        raiz2 = (-b - raiz_quadrada)/ (2 * a)

        print(f'R1 = {raiz1:0.5f}')
        print(f'R2 = {raiz2:0.5f}')
except:
    print('Impossivel calcular')

