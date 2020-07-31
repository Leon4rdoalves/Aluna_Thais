"""
Operadores unitários >>> Dependem de um único valor >>> not, is
Operadores binários >>> Dependem de mais que 1 valor >>> and, or
"""

'''
AND >>> Ambos os valores precisam ser TRUE
OR >>> Pelo menos um valor precisa ser TRUE
NOT >>> Negação, inverte a expressão
IS >>> Questiona se um dado é...
'''

nota = float(input('Digite a nota do aluno: '))

if (nota >= 7):
    print('Aluno APROVADO')


elif (nota >= 5) and (nota < 7):    # Ao utilizar o AND, as duas expressões precisam ser TRUE
    print('Aluno em RECUPERAÇÃO.')


else:
    print('Aluno REPROVADO.')