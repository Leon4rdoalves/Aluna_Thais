"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:

11% para o Imposto de Renda
8% para o INSS
5% para o sindicato

Faça um programa que nos dê:

a. Salário bruto.
b. Quanto pagou ao INSS.
c. Quanto pagou ao sindicato.
d. O salário líquido.
e. Calcule os descontos e o salário líquido.
"""


salario = float(input('Informe quanto você ganha por hora: '))

hora_mes = float(input('Informe quantas horas você trabalhou este mês: '))


salario_bruto = salario * hora_mes

imposto_renda = 11 * salario_bruto / 100
inss = 8 * salario_bruto / 100
sindicato = 5 * salario_bruto / 100


print(f'\nSeu Salário Bruto: R${salario_bruto:.2f}')
print(f'\nVocê pagou ao Imposto de Renda: {imposto_renda:.2f}')
print(f'Você pagou ao INSS: R${inss:.2f}')
print(f'Você pagou ao Sindicato: R${sindicato:.2f}')
print(f'Total de descontos: R${imposto_renda + inss + sindicato:.2f}')
print(f'\nSeu salário liquido é: R${salario_bruto - imposto_renda - inss - sindicato:.2f}')



