name = []
new_category = ''

category = str(input("Let's create a list of 5 things. Think of a general category.\n "
               "What category of things should we store? ")).title()

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

character = input('\nPick a character: ')
list_boo = []
for i in name:
    boolean = character in i

    list_boo.append(boolean)

print(list_boo)


