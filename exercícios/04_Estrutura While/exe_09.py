"""
Crie um programa que leia uma quantidade indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
deverá terminar quando for lido um número negativo.
"""

cont_1 = cont_2 = cont_3 = cont_4 = 0
print('Digite um número negativo para encerrar.')

while True:
    num = int(input('Número: '))

    if num >= 0:
        if (num >= 0) and (num <= 25):
            cont_1 += 1
        elif (num >= 26) and (num <= 50):
            cont_2 += 1
        elif (num >= 51) and (num <= 75):
            cont_3 += 1
        elif (num >= 76) and (num <= 100):
            cont_4 += 1

    else:
        break

print(f'\nTotais de números inseridos:\nIntervalo entre 0 e 25: {cont_1}\nIntervalo entre 26 e 50: {cont_2}\n'
      f'Intervalo entre 51 e 75: {cont_3}\nIntervalo entre 76 e 100: {cont_4}')
