"""
Crie um programa tabuada que permita ao usuário solicitar quantas vezes ele quiser, encerrando quando
o mesmo responder não querer mais utilizar o programa, então finalize o programa com uma mensagem de
agradecimento.
"""

resp = ''

while True:
    num = int(input('Com qual número quer criar: '))
    for cont in range(1, 11):
        print(f'{num} x {cont:<2} = {num*cont}')

    while True:
        resp = str(input('\nTecle N para nova consulta ou S para sair: ')).upper().strip()

        if resp not in 'NS':
            print(f'Dado inválido...', end=' ')

        if resp == 'S':
            break

        if resp == 'N':
            break

    if resp == 'N':
        break

print('\nObrigado por utilizar o sistema...')