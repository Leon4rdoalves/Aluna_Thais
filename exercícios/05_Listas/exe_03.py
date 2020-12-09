'''
Crie um programa que leia 4 notas, mostre as notas e a média. (As notas devem ser
armazenadas em uma lista antes dos cálculos).
'''

notas = [[], []]

for n in range(4):
    notas[0].append(float(input(f'{n + 1}ª Nota: ')))

notas[1].append(sum(notas[0]) / 4)

print(f'\nNotas do aluno: {notas[0]}')
print(f'Média do aluno: {notas[1]}')


