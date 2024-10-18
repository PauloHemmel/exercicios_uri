# entrada = float(input())

# lista_notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]


# lista_resto = []
# lista_inteiro = []
# indice = 0
# valor_resto = entrada

# while indice < 12:

#     lista_resto.append(valor_resto % lista_notas[indice])
#     lista_inteiro.append(valor_resto // lista_notas[indice])
#     valor_resto = lista_resto[indice]
#     indice += 1

#     #print(lista_resto)
# #print(lista_inteiro)

# print(f'{entrada:0.0f}')
# indice2 = 0
# while indice2 < 6:
#     print(f'{lista_inteiro[indice2]:0.0f} nota(s) de R$ {lista_notas[indice2]},00')

#     indice2 += 1

entrada = int(input())

lista_notas = [100, 50, 20, 10, 5, 2, 1]


lista_resto = []
lista_inteiro = []
indice = 0
valor_resto = entrada

while indice < 7:

    lista_resto.append(valor_resto % lista_notas[indice])
    lista_inteiro.append(valor_resto // lista_notas[indice])
    valor_resto = lista_resto[indice]
    indice += 1

    #print(lista_resto)
#print(lista_inteiro)

print(f'{entrada}')
indice2 = 0
while indice2 < 7:
    print(f'{lista_inteiro[indice2]} nota(s) de R$ {lista_notas[indice2]},00')

    indice2 += 1