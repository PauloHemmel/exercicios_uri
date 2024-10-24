# Notas e Moedas - 1021
# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário. A seguir, calcule
# o menor número de notas e moedas possíveis no qual o valor
# pode ser decomposto. As notas consideradas são de 100, 50, 20,
# 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05
# e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias
# para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

# Exemplo de Entrada	
# 576.73

# Exemplo de Saída
# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01

# entrada = float(input())

# lista_notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
# lista_inteiro = []
# indice = 0
# valor_resto = entrada

# while indice < 12:
#     lista_inteiro.append(valor_resto // lista_notas[indice])
#     valor_resto = valor_resto % lista_notas[indice]
#     indice += 1

# print('NOTAS:')
# indice2 = 0
# while indice2 < 6:
#     print(f'{lista_inteiro[indice2]:0.0f} nota(s) de R$ {lista_notas[indice2]:0.2f}')
#     indice2 += 1
# print('MOEDAS:')
# indice3 = 6
# while indice3 < 12:
#     print(f'{lista_inteiro[indice3]:0.0f} moeda(s) de R$ {lista_notas[indice3]:0.2f}')
#     indice3 += 1

entrada = float(input()) * 100  # Trabalhar com valores inteiros (centavos)

lista_notas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]  # Tudo em centavos
lista_inteiro = []
indice = 0
valor_resto = int(round(entrada))  # Arredondar para evitar problemas de precisão

while indice < 12:
    lista_inteiro.append(valor_resto // lista_notas[indice])
    valor_resto = valor_resto % lista_notas[indice]
    indice += 1

print('NOTAS:')
indice2 = 0
while indice2 < 6:
    print(f'{lista_inteiro[indice2]:0.0f} nota(s) de R$ {lista_notas[indice2] / 100:0.2f}')
    indice2 += 1

print('MOEDAS:')
indice3 = 6
while indice3 < 12:
    print(f'{lista_inteiro[indice3]:0.0f} moeda(s) de R$ {lista_notas[indice3] / 100:0.2f}')
    indice3 += 1
