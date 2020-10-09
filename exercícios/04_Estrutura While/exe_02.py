"""
Crie um programa de operações matemáticas, ele deve receber 2 valores
informados pelo usuário e um menu com opções, onde o usuário possa
escolher: Somar, subtrair, dividir, multiplicar e sair.
"""

status = True

while True:
    if not status:
        break

    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

    print('''\nMENU PRINCIPAL\033[32m
    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Dividir
    [ 4 ] Multiplicar
    [ 5 ] Novos Números
    [ 6 ] Sair\033[m''')

    while True:
        op = int(input('OPÇÃO: '))

        if (op > 6) or (op < 1):
            print('\033[31mDado inválido!\033[m', end=' ')
        elif op == 1:
            print(f'\nCalculando... {v1} + {v2} = {v1 + v2}\n')
        elif op == 2:
            print(f'\nCalculando... {v1} - {v2} = {v1 - v2}\n')
        elif op == 3:
            print(f'\nCalculando... {v1} / {v2} = {v1 / v2}\n')
        elif op == 4:
            print(f'\nCalculando... {v1} + {v2} = {v1 * v2}\n')
        elif op == 5:
            print()
            break
        else:
            status = False
            break

print('\n\033[33mObrigado por utilizar o sistema...\033[m')

