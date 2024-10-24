
a, b, c, d = map(float, input().split())



media = ((2 * a) + (3 * b) + (4 * c) + (d)) / (2 + 3 + 4 + 1)
media2 = ((2 * a))

if media >= 7:
    print(f'Media:{media}')
    print(f'Aluno aprovado')
elif media < 5:
    exame = float(input())
    print(f'Media:{media}')
    print(f'Aluno reprovado')
    print(f'Media:{media}')

    

