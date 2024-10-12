"""
Teste de Seleção 1

Leia 4 valores inteiros A, B, C e D. A seguir, se B
for maior do que C e se D for maior do que A, e a 
soma de C com D for maior que a soma de A e B e se C e D,
ambos, forem positivos e se a variável A for par escrever
a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada	
5 6 7 8

Exemplo de Saída
Valores nao aceitos

Exemplo de Entrada	
2 3 2 6

Exemplo de Saída
Valores aceitos

"""

a, b, c, d = map(int, input().split())

soma_c_d = c + d
soma_a_b = a + b
a_par = a % 2

if b > c and d > a and soma_c_d > soma_a_b and c > 0 and d > 0 and a_par == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
