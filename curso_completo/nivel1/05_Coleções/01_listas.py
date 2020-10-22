'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison as multi


# Ex01

semana = [
    ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
    [10, 15.89, 30, 58.69, 14, 250, 899.59]
]

plt.plot(semana[0], semana[1], 'r')
plt.xlabel('Dias da Semana.')
plt.ylabel('Dinheiro gasto.')
plt.show()

# ----------------------------------------------

# Ex02

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)
}

data['b'] = data['a'] + 10 * np.random.randint(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('Entry a')
plt.ylabel('Entry b')
plt.show()
'''



def parrot(talk, hour):
    return (talk and (hour < 7 or hour > 20))

parrot(False, 5)

