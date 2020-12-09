"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""

# Pedindo 3 nomes com for
for n in range(3):
    nome = str(input('Nome: '))

# Pedindo 3 nomes com While
cont = 0
while cont < 3:
    nome = str(input('Nome: '))
    cont += 1


# Enquanto a resposta for diferente de S
resposta = ''

while resposta != 'S':
    resposta = str(input('Digite S para sair: ')).upper()


# Contando de 0 a 10 com for
for cont in range(11):
    print(cont, end=' ')

print()

# contando de 0 a 10 com while
cont1 = 0
while cont1 < 11:
    print(cont1, end=' ')
    cont1 += 1


# Validando nome, enquanto não for númerico, o programa será executado...
nome = ''

while not nome.isnumeric():
    nome = input('Nome: ')

    if not nome.isnumeric():
        print(f'Muito prazer, {nome}')
    else:
        print('Ops, dado inválido!')

print('fim da execução')
