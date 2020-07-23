"""
Booleano >>> 2 constantes - Verdadeiro e falso.

Maneira direta de testar booleano >>>  print('a' in 'maria')
"""

''' 
Estudo de caso: Suponha que um app permite teste de 7 dias e pergunta ao usuário
se o pagamento para uso completo foi realizado, caso sim, libera em confiança a assinatura.
'''


usuario = False    # Ele ainda não pagou pela versão completa, portanto seu status é false

status = usuario   # Variável responsavel por guardar este e outros usuários.

# Solicitando resposta do usuário e alterando em letra maiúscula.
pg = input('O pagamento foi feito? [S para sim | N para não]: ').upper()


# testando se o pagamento foi feito, note que é necessário que a resposta esteja em letras maiúsculas.
if pg == 'S':
    status = (not usuario)


# Saída personalizada com o status do usuário.
print(f'Usuário com versão completa: {status}')



# Maneira direta de testar booleano >>>  print('a' in 'maria')

