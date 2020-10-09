"""
Crie um programa que peça vários números ao usuário e interrompa
quando o usuário digitar 999, ao final, mostre a soma de todos
os valores digitados, sem o FLAG.
"""
soma = total = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    soma += num
    total += 1

print(f'\nTotal de número inseridos: {total}')
print(f'Soma de todos os valores inseridos: {soma}')
