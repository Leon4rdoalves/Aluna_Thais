'''
Crie um programa que tenha uma lista com 20 números inteiros aleatórios no intervalo
1 - 50. Desta lista, separe em outras duas 'pares' e Ímpares' os números conforme
sua condição. Ao final, mostre os valores das 3 listas separados por vírgula.
'''

from random import randint

lista_total = []
lista_pares = []
lista_impar = []
temporario = ''

while True:
    if len(lista_total) < 20:

        temporario = randint(1, 50)

        if temporario not in lista_total:
            lista_total.append(temporario)
            if temporario % 2 == 0:
                lista_pares.append(temporario)
            else:
                lista_impar.append(temporario)

    else:
        break

print(f'\nTodos os número sorteados: {lista_total}')
print(f'Números pares: {lista_pares}')
print(f'Números ímpares: {lista_impar}')
