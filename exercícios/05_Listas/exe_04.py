'''
Crie um programa que solicita uma categoria, em seguida pergunte quantos valores desta
categoria o usuário deseja armazenar, então solicite que o usuário digite
os valores, ao final permita que o usuário consulte um valor que foi informado.
Trabalhe a questão do plural na categoria e singular ao solicitar o valor. (EM INGLêS)
'''


name = []
new_category = ''

category = str(input("What category of things should we store? ")).title()

many = int(input('\nHow many are there? '))

if 'ies' in category[-3:]:
    new_category = category.replace('ies', 'y')

elif 'es' in category[-2:]:
    new_category = category.replace('es', '')

elif 's' in category[-1]:
    new_category = category.replace('s', '')

else:
    new_category = category

for i in range(many):
    name_list = str(input(f'{new_category} {i + 1}: '))
    name.append(name_list)

number = int(input(f'\nPick a number between 1 and {many}: '))
number = number -1

print(f'You picked {name[number]}!')
