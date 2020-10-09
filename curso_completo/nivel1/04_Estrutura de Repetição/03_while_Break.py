"""
While com Break

while True: >>> este laço será executado enquanto não encontrar o Break pelo caminho.

Break >>> Condição de parada de um loop.

"""

while True:
    nome = str(input('Nome: '))

    sair = str(input('Digitar mais um nome? [S / N]: ')).upper()

    if sair == 'N':
        break


