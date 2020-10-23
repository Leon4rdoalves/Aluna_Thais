from csv import reader, DictWriter, DictReader

parametro = sedentary = moderate = active = ''
cont = amount = 0
people_list = []

print('Hello!')
file_name = input("Please type the file name here: ")
if file_name[-4:] == '.csv':
    file = file_name
else:
    file = file_name + '.csv'

try:
    with open(file) as doc:
        leitor = DictReader(doc)
        print()
        for linha in leitor:
            print(
                f"| {linha['FIRST NAME']:<10} | {linha['LAST NAME']:<12} | {linha['AGE']:^5} | {linha['OCCUPATION']:<17}"
                f" | {linha['HEIGHT']:^7} | {linha['WEIGHT']:^7} | {linha['SEDENTARY']:^10} | {linha['MODERATE']:^10} | "
                f"{linha['ACTIVE']:^10} |")

        parametro = 'a'
        print()

except FileNotFoundError:
    parametro = 'w'

condition = str(input(f'Would you like to enter additional names? (Y/N): ')).upper()
if condition == "Y":
    amount = int(input('How many more names? '))

with open(file, parametro) as doc:
    header = ['FIRST NAME',
              'LAST NAME',
              'AGE',
              'OCCUPATION',
              'HEIGHT',
              'WEIGHT',
              'SEDENTARY',
              'MODERATE',
              'ACTIVE']

    writing = DictWriter(doc, fieldnames=header)

    if parametro == 'w':
        writing.writeheader()

    first_name = None

    while cont < amount:
        for cont in range(amount):
            print('\n', '{:-^34}'.format(f'Person {cont + 1}'))
            first_name = input('First Name: ').title()

            if first_name != 'Exit':
                last_name = str(input('Last Name: ')).title()
                age = int(input('Age: '))
                occupation = str(input('Occupation: ')).title()
                height = float(input('Height: '))
                weight = float(input('Weight: '))

                lifestyle = int(input('[1] Sedentary [2] Moderate [3] Active: '))
                if lifestyle == 1:
                    sedentary = 'x'
                elif lifestyle == 2:
                    moderate = 'x'
                elif lifestyle == 3:
                    active = 'x'
                else:
                    sedentary = moderate = active = 'Undefined'
                print('{:-^34}'.format('\033[32mPerson included\033[m'))
                print()

                writing.writerow(
                    {
                        "FIRST NAME": first_name,
                        "LAST NAME": last_name,
                        "AGE": age,
                        "OCCUPATION": occupation,
                        "HEIGHT": height,
                        "WEIGHT": weight,
                        "SEDENTARY": sedentary,
                        "MODERATE": moderate,
                        "ACTIVE": active
                    }
                )

            people_list.append(first_name)
            people_list.append(last_name)
            people_list.append(age)
            people_list.append(occupation)
            people_list.append(height)
            people_list.append(weight)
            people_list.append(sedentary)
            people_list.append(moderate)
            people_list.append(active)

        cont += 1

with open(f'{file_name}.txt', 'w') as data:
    for i in people_list:
        data.writelines(str(i))
print('{:-^50}'.format('\033[32mFile Saved\033[m'))
