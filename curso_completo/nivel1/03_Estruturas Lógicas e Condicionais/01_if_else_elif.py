"""
IF, ELSE, ELIF
"""

resposta = input('Vc entendeu? [S para sim | N para não | T para Talves]: ').lower()


if resposta == 's':
    print('\n\033[32mOk, eu entendi!\033[m')
elif resposta == 't':
    print('Ok, aguardo vc pensar!')
elif resposta == 'j':
    print('Qualquer coisa')
else:
    print('\n\033[31mOk, vamos novamente!\033[m')


# Cores em python no terminal >>> print('\033[34m  skdhfkjshfjkdsfhksdjfjk    \033[m')