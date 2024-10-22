a, b = map(int, input().split())


indice = 0
novo_nome = ''
lista2 = []
dois = 0

while a <= b:
    lista2.append(a) 
    novo_nome += f'{lista2[indice] } '
    dois += lista2[indice]
    indice += 1
    a += 1
novo_nome = novo_nome
print(f'{novo_nome}Sum={dois}')