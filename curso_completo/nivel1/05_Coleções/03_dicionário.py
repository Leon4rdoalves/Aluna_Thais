"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

cadastro = []
usuario = {}

for u in range(1):
    usuario['Cod_usuário'] = u
    usuario['Nome'] = str(input('Nome: ').title())
    usuario['Telefone'] = int(input('Telefone: '))
    usuario['E-mail'] = str(input('E-mail: ').lower())
    print()
    cadastro.append(usuario.copy())

print('''
    MENU DE VISUALIZAÇÃO
[ 1 ] Nome
[ 2 ] Código do Usuário
[ 3 ] Todos os Usuários
''')

opc = int(input('Opção: '))

if opc == 1:

    for usuario in cadastro:   # [ { leo, 123, leo@leo}, { leo, 123, leo@leo} ]
        for valor in usuario.values():
            pass







elif opc == 2:
    pass
else:
    for usuario in cadastro:
        for chave, valor in usuario.items():
            print(f'{chave} = {valor}')
        print()





