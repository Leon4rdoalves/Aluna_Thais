import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import pandas as pd

'''
# Ex01 gráfico

semana = [
    ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
    [10, 15.89, 30, 58.69, 14, 250, 899.59]
]

plt.plot(semana[0], semana[1], 'r')
plt.xlabel('Dias da Semana.')
plt.ylabel('Dinheiro gasto.')
plt.show()


# Ex02 Gráfico

data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('Entry a')
plt.ylabel('Entry b')
plt.show()


# Acessando dados em bd excel
import pandas as pd


file_name = '/home/ebony/git/Alunos Python/Thais/babies.xlsx'
df = pd.read_excel(file_name)
print(df)

# x1 x2 Age

file_name = '/home/ebony/git/Alunos Python/Thais/babies.xlsx'
df = pd.read_excel(file_name)


df['x1'] # .replace({1: "x1", 2: "x2", 3: "Age"}, inplace=True)

rdf = st.f_oneway(df["Score"][df["Babies"] == "x1"], df["Score"][df["Babies"] == "x2"],df["Score"][df["Babies"] == "Age"])

print("ANOVA Results: ", rdf)
'''



