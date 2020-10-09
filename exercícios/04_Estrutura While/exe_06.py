"""
Crie um programa que receba quatro notas de um único aluno, calcule e mostre a média, a soma das notas,
a maior e menor nota. Sendo o valor mínimo para nota: 0 e máximo: 10 (O não deve aceitar valores de
nota fora deste intervalo)
"""

soma = cont = maior = menor = 0

while cont < 4:
    nota = float(input(f'Insira a {cont + 1}ª nota: '))

    if (nota >= 0) and (nota <= 10):
        soma += nota
        cont += 1

        if cont == 0:
            maior = nota
            menor = nota

        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

    else:
        print('\033[31mOps, nota inválida!\033[m', end=' ')

print(f'\nMédia: {soma / 4:.2f}')
print(f'Soma das notas: {soma}')
