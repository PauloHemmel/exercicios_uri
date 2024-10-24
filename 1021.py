
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
