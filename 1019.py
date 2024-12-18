"""

Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração
em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos),
convertido para horas:minutos:segundos, conforme exemplo 
fornecido.

Exemplo de Entrada
556

Exemplo de Saída
0:9:16

"""

segundos = int(input())

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60

print(f'{horas}:{minutos}:{segundos_restantes}')