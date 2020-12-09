'''
Crie um programa com uma lista e 10 números reais e mostre-os na ordem inversa.
'''

num1 = [10.5, 10.3, 10.4, 10.8, 10.9, 10.7, 10.6, 10.1, 10.2, 11.0]
print(num1)
num1.sort(reverse=True)
print(num1)


# -------------------------------------------------------------------
from random import randint
num2 = []
for n in range(10):
    num2.append(randint(0, 100)/1)

print(num2)

