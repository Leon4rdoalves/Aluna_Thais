"""
Crie um programa que peça para n alunos a sua idade, ao final o programa deverá verificar
se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se
a turma é jovem, adulta ou idosa, conforme a média calculada. Flag = idade 0
"""

cont = soma = 0
while True:
    idade = int(input('Informe sua idade ou 0 para sair: '))
    cont += 1
    soma += idade

    if idade == 0:
        break

media = soma/cont

if (media > 0) and (media <= 25):
    status = 'Jovem'

elif (media >= 26) and (media < 60):
    status = 'Adulta'
else:
    status = 'Idosa'

print(f'\nCom média de idade de {media:.2f} anos, esta turma é considerada {status}.')

