"""
ESTRUTURA DE REPETIÇÃO

For >>> Utilizada quando se sabe a quantidade de repetições que serão necessárias,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe >>> for item in iteravel:
                execução

* Range
    Ex. Contador 10 - 0
                 0 - 10
                  step

* Enumerate
     Ex. for valor in enumerate(frase)

* String (palavra, frase)
* Lista

"""


# Exemplo 1 >>> Solicitando nome e telefone de 10 usuários
# (Necessário uma lista para armazená-los)

for contador in range(11):
    nome = str(input('Digite seu nome: '))
    tel = int(input('Digite seu telefone: ')) 
    print('*' * 30)


# Exemplo 2 >>> Contando de 10 à 499, pulando de 2 em 2

    for contador in range(10, 500, 2):
    print(contador)


# Exemplo 3 >>> Print em cada dado de uma lista

frases = ['Python é vida', 'Python é legal']
for frase in frases:
    print(frase)


# Exemplo 4 >>> Passando variáveis inteiras para o range

inicio = 5
fim = 50
passo = 7
for contador in range(inicio, fim, passo):
    print(contador)


# Programa que vai calcular os rendimentos mensais. com taxa 10% ao mes.

valor = float(input('Digite o valor inicial: '))
mes = int(input('Digite em quantos meses quer retirar: '))
print()

taxa = 0.1
print(f'Valor inicial: {valor:.2f}')

for cont in range(1, mes+1):
    calc = valor * taxa
    valor += calc

    print(f'Rendimentos no {cont}º: R${valor:.2f}')


# Resposta com o print dentro do for e condicional

valor = float(input('Digite o valor inicial: '))
mes = int(input('Digite em quantos meses quer retirar: '))
print()

taxa = 0.1

for cont in range(mes):
    calc = valor * taxa
    if cont == 0:
        print(f'Valor inicial: {valor:.2f}')
    valor += calc

    print(f'Rendimentos no {cont+1}º: R${valor:.2f}')
