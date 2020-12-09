'''
Crie um programa com uma lista de 5 número inteiros e mostre-os.
'''
from random import randint

num1 = [10, 20, 30, 40, 50]

num2 = list(range(10, 51, 10))

num3 = []
for n in range(5):
    num3.append(randint(0, 100))

print(f'Primeira lista: {num1}')
print(f'Segunda lista:  {num2}')
print(f'Terceira lista: {num3}')
