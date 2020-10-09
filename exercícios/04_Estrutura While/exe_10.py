"""
Crie um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve
perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
    a. Maior e Menor Acerto;
    b. Total de Alunos que utilizaram o sistema;
    c. A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
"""
from time import sleep

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
resp = []
aluno = []
alunos = []
nota = cont = soma = maior = menor = 0
nome_menor = nome_maior = ''
status = True

print('*' * 40)
print('Boletim Escolar'.center(40), '\n', '*' * 39)

while True:
    nome = str(input('Aluno(a): ')).title()
    aluno.append(nome)
    print()

    for n in range(1, len(gabarito) + 1):
        resp.append(str(input(f'{n}ª Resposta: ')).upper())

    for c in range(len(gabarito)):
        if resp[c] == gabarito[c]:
            nota += 1

    if cont == 0:
        maior = nota
        menor = nota
        nome_menor = nome
        nome_maior = nome

    if nota > maior:
        maior = nota
        nome_maior = nome

    if nota < menor:
        menor = nota
        nome_menor = nome

    aluno.append(nota)
    alunos.append(aluno[:])
    aluno.clear()

    soma += nota
    cont += 1

    while True:
        novo = str(input('\nCadastrar notas de outro aluno? [S / N]: ')).upper().strip()

        if novo == 'S':
            print()
            break
        elif novo not in 'NS' or novo == '':
            print('\033[31mOps, dado inválido, tente [\033[32mS\033[31m] ou [\033[32mN\033[31m].\033[m')
        else:
            status = False
            break

    if not status:
        break


print('\n\033[34mUm momento, por favor...\033[m')
sleep(3)
print(f'\nTotal de alunos cadastrados: {cont}')
print(f'Média das notas da turma: {soma/cont:.2f}')
print(f'\033[32mAluno(a) com maior nota: {nome_maior}, nota: {maior}')
print(f'\033[31mAluno(a) com menor nota: {nome_menor}, nota: {menor}')



