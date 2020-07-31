"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. (A = r² • pi)
"""

from math import pi

raio = float(input('Digite o raio do círculo: '))

# A = r2 * pi


area = raio ** 2 * pi

print(f'Dado o raio {raio}, temos área de: {area:.3f}')

