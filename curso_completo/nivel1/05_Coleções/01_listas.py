"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* CLEAR >>> Limpa a lista.

** LIMITAÇÃO >>> Busca deve ser feita sempre por índices...
"""
'''
lista = []
lista1 = list()

lista2 = ['leo', 10, 10.8, True]

print(lista2)


numeros = [0,1,2,3,4]

numeros1 = [range(101)]
numero2 = list(range(101))

print(numeros1)
print(numero2)


nome = ['Leonardo', 'maria']
sobrenome = ['Alves']

nome_completo = [nome, sobrenome]


#print(nome_completo[0][1])

print(nome[1])


frase = """Cê tá achando que vai
Não vai me esquecer não
Eu ainda tô aí
Dentro do seu coração
Na foto que cê não apagou
Na legenda que falava de amor
Escuta teu coração, por favor
Se não sou eu, vai ser quem
O amor teu?
Só você não percebeu
Que só tem eu
Se não sou eu, vai ser quem
O amor teu?
Só você não percebeu
Que só tem eu
Volta, pelo amor de Deus
Na foto que cê não apagou
Na legenda que falava dе amor
Escuta seu coração, por favor
Se não sou eu, vai sеr quem
O amor teu?
Só você não percebeu
Que só tem eu
Se não sou eu, vai ser quem
O amor teu?
Só você não percebeu
Que só tem eu
Volta, pelo amor de Deus
Você sabe que eu te amo
Ninguém te ama mais que eu
Pode tentar me esquecer
Mas o teu coração é meu
Nem o brilho das estrelas
Nem a Lua, nem o mar
Nada disso se compara
Ao amor que sei te dar
E no toque do beat, é o Rafinha RSQ
Volta, pelo amor de Deus"""

palavras = frase.split()
print(palavras.count('Que'))


numeros = [10, 20, 30, 40, 50]

# numeros.sort(reverse=True) # colocando em ordem

#numeros.sort()  # colocando em ordem crescente
#numeros.reverse()  # invertendo a ordem para decrescente

numeros.append(50)
numeros.append(60)
numeros.append(70)
numeros.append(80)
numeros.append('Teste1')


numeros.insert(0, 0)
numeros.insert(-1, 90)
numeros.insert(-1, 'Teste')

#numeros.sort()


numeros.pop(1)

numeros.remove(20)
numeros.remove('Teste')

print(numeros)


numeros = []

for n in range(1, 4):
    #num = int(input(f'{n}º Número: '))
    #numeros.append(num)

    numeros.append(str(input(f'{n}º Número: ')))
    
print(numeros)




from time import sleep
nomes = []

for n in range(3):
    nomes.append(str(input(f'{n+1}º Nome: ')).title())



print()
for nome in nomes:
    print(f'Muito prazer, {nome}.')
    sleep(2)



a = [1, 2, 3]

b = [4, 5, 6]

c = a + b

print(type(c))
print(c)



a = [1, 2, 3]

# b = a
b = a[:]

b.append(4)
b.append(5)


print('Lista A: ', a)
print('Lista B: ', b)




semana = []
dinheiro = []
dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')


for dia in dias:
    dinheiro.append(float(input(f'valor gasto na {dia}: ')))

semana.append(dias[:])
semana.append(dinheiro[:])


print()
print(semana)
print()
print(semana[0][0])
print(semana[1][0])

'''










