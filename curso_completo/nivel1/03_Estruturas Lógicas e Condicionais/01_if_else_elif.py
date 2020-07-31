"""
IF, ELSE, ELIF

Estrutura condicional.
Permite que o código siga por caminhos diferentes de acordo com as decisões que são tomadas.

Vale ressaltar que ELIF só existe em PYTHON
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''


nota = float(input('Digite a nota do aluno: '))

if (nota >= 7):
    print('Aluno APROVADO')


elif (nota >= 5) and (nota < 7):
    print('Aluno em RECUPERAÇÃO.')


else:
    print('Aluno REPROVADO.')
