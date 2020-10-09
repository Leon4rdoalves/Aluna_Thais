"""
Crie um programa que solicita vários números inteiros ao usuário,
pergunte se ele quer continuar digitando e caso responda não,
informe o total de números digitados, o menor, o maior e a
média entre eles.
"""
from time import sleep
total = soma = 0
status = True

while True:
    num = int(input('Digite um número: '))
    total += 1
    soma += num

    while True:
        resp = str(input('Continuar? [S / N]: ')).strip().upper()
        if resp == 'S':
            print(f'\033[32mO número {num} foi adicionado...\033[m\n')
            break
        elif resp not in 'SN':
            print('\033[31mDado Inválido...\033[m\n')
        else:
            print('\033[34mPor favor, aguarde...\033[m\n')
            status = False
            sleep(2)
            break
    if not status:
        break


print(f'Total de números inseridos: {total}')
print(f'Somando os números inseridos, temos: {soma}')