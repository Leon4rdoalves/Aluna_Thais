"""
Faça um programa cadastro. Ele deve solicitar o nome, idade e sexo de 10 pessoas.
Ao final mostre, a média de idade de todos dos homens e das mulheres,
assim como a média geral. O nome do homem mais velho e da mulher mais nova.
Obrigatório utilizar estrutura FOR.
"""

soma_id = cont_id = soma_idm = cont_idm = soma_idg = cont_idg = maior_id = menor_id = 0
nome_maior_id = nome_menor_id = ''

for cont in range(5):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip().upper()
    print('-' * 35)

    if cont == 0:
        menor_id = idade
        maior_id = idade

    soma_idg += idade
    cont_idg += 1

    if sexo == 'M':
        soma_id += idade
        cont_id += 1

        if idade > maior_id:
            maior_id = idade
            nome_maior_id = nome

    elif sexo == 'F':
        soma_idm += idade
        cont_idm += 1

        if idade < menor_id:
            menor_id = idade
            nome_menor_id = nome

    else:
        print('\033[31mFalha grave...resolvemos no próximo assunto do curso!\033[m')

media_m = soma_idm / cont_idm
media_h = soma_id / cont_id
media_g = soma_idg / cont_idg

print(f'\nMédia de idade dos homens cadastrados: {media_h:.2f}')
print(f'Média de idade das mulheres cadastradas: {media_m:.2f}')
print(f'Média de idade de todas as pessoas cadastradas: {media_g:.2f}')
print(f'\nHomem mais velho cadastrado foi o: Srº {nome_maior_id}')
print(f'Mulher mais nova cadastrada foi a: Srª {nome_menor_id}')
