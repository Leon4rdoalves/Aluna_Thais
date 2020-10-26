from csv import DictWriter, DictReader, reader

parameter = sedentary = moderate = active = ''
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
        reading = DictReader(doc)
        print('| FIRST NAME |  LAST NAME   |  AGE  |    OCCUPATION     | HEIGHT  |  WEIGHT | '
              'SEDENTARY  |  MODERATE  |   ACTIVE   |')
        for line in reading:
            print(
                f"| {line['FIRST NAME']:<10} | {line['LAST NAME']:<12} | {line['AGE']:^5} | "
                f"{line['OCCUPATION']:<17} | {line['HEIGHT']:^7} | {line['WEIGHT']:^7} | "
                f"{line['SEDENTARY']:^10} | {line['MODERATE']:^10} | {line['ACTIVE']:^10} |")

        parameter = 'a'
        print()

except FileNotFoundError:
    parameter = 'w'

condition = str(input(f'Would you like to enter additional names? (Y/N): ')).upper()
if condition == "Y":
    amount = int(input('How many more names? '))

with open(file, parameter) as doc:
    header = ['FIRST NAME', 'LAST NAME', 'AGE', 'OCCUPATION', 'HEIGHT', 'WEIGHT',
              'SEDENTARY', 'MODERATE', 'ACTIVE']

    writing = DictWriter(doc, fieldnames=header)
    if parameter == 'w':
        writing.writeheader()

    while cont < amount:
        for cont in range(amount):
            print('\n', '{:-^34}'.format(f'Person {cont + 1}'))
            first_name = input('First Name or "EXIT" for closed: ').title()

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
                print('{:-^34}'.center(30).format('\033[32mPerson included\033[m'))
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
        cont += 1

with open(file_name + '.txt', 'w') as output_file:
    with open(file, 'r') as input_file:
        [output_file.write(" ".join(row) + '\n') for row in reader(input_file)]
    output_file.close()

print('\n', '{:-^60}'.format('\033[32mFile Saved\033[m'))
