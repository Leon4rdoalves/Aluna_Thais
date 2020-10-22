def Parabens():
    print('\nParabens pra você\n'
          'Nesta data querida!\n'
          'Viva o aniversariantes!!!')


# -----------------------------  Programa Principal

dia = int(input('Dia: '))
mes = str(input('Mẽs: '))
ano = int(input('Ano: '))

hoje = [20, 'outubro', 2020]

if (dia == hoje[0]) and (mes == hoje[1]) and (ano == hoje[2]):
    Parabens()
else:
    print('Ok, volte no seu dia!')
