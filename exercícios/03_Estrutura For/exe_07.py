"""
Faça um programa que leia um número inteiro e na sequencia mostre se ele é ou não um número primo.
(Números primos são divisíveis por 1 e eles mesmos apenas).
"""

num = int(input('Digite um número: '))
primo = 0

for cont in range(1, num + 1):

    if num % cont == 0:
        print('\033[32m', end=' ')
        primo += 1
    else:
        print('\033[31m', end=' ')
    print(cont, end=' ')


if primo <= 2:
    print(f'\n\033[m\nO número {num} é um número PRIMO!')
else:
    print(f'\n\033[m\nO número {num} não é um número PRIMO!')

