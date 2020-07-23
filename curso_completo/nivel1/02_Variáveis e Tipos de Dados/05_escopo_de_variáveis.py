"""
Escopo >>> Limitação de espaço
Escopo de variáveis >>> Está variável vai ser reconhecida apenas dentro do escopo onde foi declarada

Variavel Global >>> Pode ser utilizada em qualquer parte do código
Variavel Local >>> Pode ser utilizada dentro da função
"""



def Cadastro():
    nome = 'Maria'
    return nome


while True:
    print('a')

nome = 'Leonardo'

print(nome)

print(Cadastro())