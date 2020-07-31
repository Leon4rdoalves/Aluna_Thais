"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

a. O produto do dobro do primeiro com metade do segundo.
b. A soma do triplo do primeiro com o terceiro.
c. O terceiro elevado ao cubo.
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

print(f'\nO Resultado da letra A: {(num1 * 2) * (num2 / 2)}')

print(f'O Resultado da letra B: {num1 * 3 + num3}')

print(f'O Resultado da letra C: {num3 ** 3}')
