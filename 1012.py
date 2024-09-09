# Área

# Escreva um programa que leia três valores
# com ponto flutuante de dupla precisão: A, 
# B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem 
# A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por 
# bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.
# Entrada
# O arquivo de entrada contém três valores 
# com um dígito após o ponto decimal.

# Saída
# O arquivo de saída deverá conter 5 linhas 
# de dados. Cada linha corresponde a uma das
# áreas descritas acima, sempre com mensagem
# correspondente e um espaço

a, b, c = map(float, input().split())

triangulo = (a * c)/2
circulo = (c ** 2) * 3.14159
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print("TRIANGULO: "f'{triangulo:.3f}')
print("CIRCULO: "f'{circulo:.3f}')
print("TRAPEZIO: "f'{trapezio:.3f}')
print("QUADRADO: "f'{quadrado:.3f}')
print("RETANGULO: "f'{retangulo:.3f}')

