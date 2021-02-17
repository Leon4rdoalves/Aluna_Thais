from csv import DictWriter, DictReader, reader

parameter = sedentary = moderate = active = ''
count = amount = 0
people_list = []
quantity = 0


def input_info(Type, number):
    a = False
    while a != True:
        info = input(f'Please enter the {Type}: ')
        if len(info) <= number:
            return (info)
        else:
            print(f'Invalid {Type}, please try again with up to {info} characters.')
            a = False


def input_int(Type, number):
    a = False
    while a != True:
        info = input(f'Please enter the {Type}: ')
        if len(info) <= number:
            try:
                info = int(info)
                return (info)

            except ValueError:
                print('Invalid value, please enter an integer: ')
        else:
            print(f'Invalid {Type}, please try again with up to {number} characters.')
            a = False


def input_ht(number):
    foot = int(number // 12)
    inch = int(number % 12)
    tt = '"'
    return (f"{foot}'{inch}{tt}")


def bmi(height, weight):
    return (weight / (height * height))


a = True
print('Hello!')
while a == True:

    file_name = input("Please enter a roster file: ")
    print(" ")
    if file_name[-4:] == '.csv':
        file = file_name
    else:
        file = file_name + '.csv'

    try:
        quantity = 0
        with open(file) as doc:
            reading = DictReader(doc)
            print('| FIRST NAME |  LAST NAME   |  AGE  |    OCCUPATION     | HEIGHT  |  WEIGHT | '
                  'SEDENTARY  |  MODERATE  |   ACTIVE   |')
            for line in reading:
                quantity = quantity + 1
                print(
                    f"| {line['FIRST NAME']:<10} | {line['LAST NAME']:<12} | {line['AGE']:^5} | "
                    f"{line['OCCUPATION']:<17} | {line['HEIGHT']:^7} | {line['WEIGHT']:^7} | "
                    f"{line['SEDENTARY']:^10} | {line['MODERATE']:^10} | {line['ACTIVE']:^10} |")

            parameter = 'a'
            a = False
            print("")

    except FileNotFoundError:
        new_name = input(
            'ERROR, FILE DOES NOT EXIST. Would you like to create a new file and save it under that name? (Y/N): ').upper()
        if new_name == "Y":
            parameter = "w"
            a = False
        else:
            print("You have opted for not saving it under a new file name.")
            print("")

condition = str(
    input(f'There are {quantity} names in this file. Would you like to enter additional names? (Y/N): ')).upper()
if condition == "Y":
    amount = int(input('How many more names? '))

with open(file, parameter) as doc:
    header = ['FIRST NAME', 'LAST NAME', 'AGE', 'OCCUPATION', 'HEIGHT', 'WEIGHT',
              'SEDENTARY', 'MODERATE', 'ACTIVE']

    writing = DictWriter(doc, fieldnames=header)
    if parameter == 'w':
        writing.writeheader()

    while count < amount:
        for count in range(amount):
            print('\n', '{:-^60}'.format(f'\033[32m Person {count + 1} \033[m'))
            print("")
            first_name = input_info('First Name or "Exit" to close', 9).title()

            if first_name != 'Exit':
                last_name = str(input_info('Last Name', 8)).title()
                age = int(input_int('Age', 3))
                occupation = str(input_info('Occupation', 10))
                height_1 = float(input_int('Height (in inches)', 5))
                height = input_ht(height_1)
                weight = int(input_int('Weight (in pounds)', 3))

                lifestyle = int(input_int("Lifestyle: [1] Sedentary [2] Moderate [3] Active", 9))
                if lifestyle == 1:
                    sedentary = 'x'
                elif lifestyle == 2:
                    moderate = 'x'
                elif lifestyle == 3:
                    active = 'x'
                else:
                    sedentary = moderate = active = 'Undefined'

                print('\n', '{:-^60}'.format('\033[32m Person Included \033[m'))
                print("")
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
            else:
                print('\n', '{:-^60}'.format(f'\033[32m Session Closed \033[m'))
        count += 1

file_txt = input('Save new roster file as: ')

with open(file_txt + '.txt', 'w') as output_file:
    with open(file, 'r') as input_file:
        [output_file.write(" ".join(row) + '\n') for row in reader(input_file)]
        output_file.close()

        print('\n', '{:-^60}'.format('\033[32m File Saved \033[m'))
