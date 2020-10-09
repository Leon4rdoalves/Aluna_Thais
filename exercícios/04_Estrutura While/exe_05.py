"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
menor peso e maior peso, para isto você deve fazer um programa que pergunte a cada um dos clientes
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dado quando
o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informado os
códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes.
"""
# 5
quant = cont_alt = cont_peso = 0
maior = peso_m = cod_m = 0
menor = peso_me = cod_me = 0
mais_g = alt_g = cod_g = 0
menor_g = altm_g = codm_g = 0

while True:
    print('\n\033[36mDigite 0 (zero) para encerrar!\033[m')
    cod = int(input('Informe seu código: '))

    if cod == 0:
        print()
        break
    else:
        altura = float(input('Informe sua altura: '))
        peso = float(input('Informe seu peso: '))
        print('-' * 30)

        quant += 1
        cont_alt += altura
        cont_peso += peso

        if quant == 1:
            maior = altura
            menor = altura
            mais_g = peso
            menor_g = peso

        if altura >= maior:
            maior = altura
            cod_m = cod
            peso_m = peso
        elif altura < menor:
            menor = altura
            cod_me = cod
            peso_me = peso
        if peso >= mais_g:
            mais_g = peso
            alt_g = altura
            cod_g = cod
        elif peso < menor_g:
            menor_g = peso
            altm_g = altura
            codm_g = cod

print('*' * 30, '\nDADOS DO USUÁRIO MAIS ALTO.')
print(f'Código: {cod_m}\nAltura: {maior}m\nPeso: {peso_m}Kg.\n')

print('*' * 30, '\nDADOS DO USUÁRIO MAIS BAIXO.')
print(f'Código: {cod_me}\nAltura: {menor}m\nPeso: {peso_me}Kg.\n')

print('*' * 30, '\nDADOS DO USUÁRIO DE MAIOR PESO.')
print(f'Código: {cod_g}\nAltura: {alt_g}m\nPeso: {mais_g}Kg.\n')

print('*' * 30, '\nDADOS DO USUÁRIO DE MENOR PESO.')
print(f'Código: {codm_g}\nAltura: {altm_g}m\nPeso: {menor_g}Kg.\n')

print('*' * 30, '\nTOTAIS E MÉDIAS.')
print(f'Usuários cadastrados: {quant}\nMédia de alturas: {cont_alt / quant:.2f}m\n'
      f'Média de pesos: {cont_peso / quant:.2f}Kg')
