'''
Crie um programa 'Boletim Escolar'. Ele deve:
- Cadastrar nome e 4 notas de cada aluno
- Perguntar ao usuário se deseja cadastrar outro aluno
- Calcular a média de cada aluno.
- Manter todos os dados do aluno em uma lista separando por alunos

Menu com opções de impressão:
- Alunos com média superior ou igual a 7
- Alunos com média entre 5 e 6.9
- Alunos com média abaixo de 5
- Todos os dados sobre um determinado aluno
'''

notas = []
aluno = []
turma = []
status = True

print('\n', '\033[7;36m  B O L E T I M  E S C O L A R  \033[m'.center(70))

while True:

    nome = str(input('\nNome do(a) aluno(a): ')).title().strip()
    for n in range(4):
        notas.append(float(input(f'\033[36m{n + 1}ª\033[m Nota: ')))

    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(sum(notas) / len(notas))
    turma.append(aluno[:])

    notas.clear()
    aluno.clear()

    while True:
        resp = str(input('\n\033[7;36m Cadastrar outro aluno(a) [S / N]:\033[m '))

        if (resp.upper() not in 'NS') or (resp == ''):
            print('\033[7;31m Resposta inválida! \033[m'.center(43))
        elif resp.upper() == 'N':
            print()
            print('''\033[7;37m M E N U  P R I N C I P A L \033[m

    [ 1 ] Alunos com média superior ou igual a 7.0
    [ 2 ] Alunos com média entre 5.0 e 6.9
    [ 3 ] Alunos com média abaixo de 4.9
    [ 4 ] Voltar ao menu anterior.
    [ 5 ] Sair sem impressão!
    ''')

            while True:
                opc = int(input('Opção: '))

                if (opc <= 0) or (opc > 5):
                    print('Opção inválida!')

                elif opc == 1:
                    print()
                    print('\033[7;32m  APROVADOS  \033[m')

                    for aluno in range(len(turma)):
                        if turma[aluno][2] >= 7:
                            print(f'{turma[aluno][0]:<.50}')
                    print('\033[32m-\033[m' * 64)






                elif opc == 2:
                    break
                elif opc == 3:
                    break
                elif opc == 4:
                    break

                elif opc == 5:
                    status = False
                    break
                else:
                    print('\033[7;31m Resposta inválida! \033[m'.center(43))
                if not status:
                    break

        else:
            break

        if not status:
            break

    if not status:
        break
