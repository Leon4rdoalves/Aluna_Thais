from csv import reader, DictWriter

sedentary = moderate = active = ''
cont = amount = 0
# ___________________________________________________Criando o nome o arquivo de dados

print('Hello!')
file_name = str(input('Please type the file name: '))
if file_name[-4:] == '.csv':
    file = file_name
else:
    file = file_name + '.csv'

# __________________________________________________Verificando se o arquivo já existe

try:
    with open(file) as arquivo:
        leitor = reader(arquivo)
        # next(leitor)   inicia a próxima linha
        for linha in leitor:
            print(
                f'| {linha[0]:<10} | {linha[1]:<12} | {linha[2]:^5} | {linha[3]:<17} | {linha[4]:^7} '
                f'| {linha[5]:^7} | {linha[6]:^10} | {linha[7]:^10} | {linha[8]:^10} |')
        parametro = 'a'
        print()

except FileNotFoundError:
    parametro = 'w'

# __________________________________________________Criando ou alterando o arquivo

condition = input(f'Would you like to enter additional names? (Y/N): ').upper()
if condition == "Y":
    amount = int(input('How many more names: '))

with open(file, parametro) as arquivo:
    header = ['FIRST NAME',
              'LAST NAME',
              'AGE',
              'OCCUPATION',
              'HEIGHT', 'WEIGTH',
              'SEDENTARY',
              'MODERATE',
              'ACTIVE']

    writing = DictWriter(arquivo, fieldnames=header)
    if parametro == 'w':
        writing.writeheader()
    first_name = None

    while cont < amount:
        for cont in range(amount):
            print('\n', '{:-^34}'.format(f'{cont + 1}ª Pessoa'))
            first_name = input('First Name: ').title()
            if first_name != 'Exit':
                last_name = str(input('Last name: ')).title()
                age = int(input('Age: '))
                occupation = str(input('Occupation: ')).title()
                height = float(input('Height: '))
                weigth = float(input('Weigth: '))
                lifestyle = int(input('[1] Sedentary or [2] Moderate or [3] Active: '))
                if lifestyle == 1:
                    sedentary = 'x'
                elif lifestyle == 2:
                    moderate = 'x'
                elif lifestyle == 3:
                    active = 'x'
                else:
                    sedentary = moderate = active = 'N/S'
                print('\n', '{:-^34}'.format('\033[32mSaved\033[m'))

                writing.writerow(
                    {
                        "FIRST NAME": first_name,
                        "LAST NAME": last_name,
                        "AGE": age,
                        "OCCUPATION": occupation,
                        "HEIGHT": height,
                        "WEIGTH": weigth,
                        "SEDENTARY": sedentary,
                        "MODERATE": moderate,
                        "ACTIVE": active
                    })
        cont += 1


