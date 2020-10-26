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


from collections import Counter

texto = '''
Hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house (hold up)
I said certified freak, seven days a week
Wet-ass pussy, make that pullout game weak (ah)

[Cardi B]
Yeah, yeah, yeah, yeah
Yeah, you fuckin' with some wet-ass pussy
Bring a bucket and a mop for this wet-ass pussy
Give me everything you got for this wet-ass pussy

[Cardi B & Megan Thee Stallion]
Beat it up, nigga, catch a charge
Extra large and extra hard
Put this pussy right in your face
Swipe your nose like a credit card
Hop on top, I wanna ride
I do a kegel while it's inside
Spit in my mouth, look in my eyes
This pussy is wet, come take a dive
Tie me up like I'm surprised
Let's roleplay, I'll wear a disguise
I want you to park that big Mack truck right in this little garage
Make it cream, make me scream
Out in public, make a scene
I don't cook, I don't clean
But let me tell you, I got this ring (ayy, ayy)

[Megan Thee Stallion]
Gobble me, swallow me, drip down the side of me (yuh)
Quick, jump out 'fore you let you get inside of me (yuh)
I tell him where to put it, never tell him where I'm 'bout to be (huh)
I run down on him 'fore I have a nigga runnin' me (pow, pow, pow)
Talk your shit, bite your lip (yuh)
Ask for a car while you ride that dick (while you ride that dick)
You really ain't never gotta fuck him for a thing (yuh)
He already made his mind up 'fore he came (ayy, ah)
Now get your boots and your coat for this wet-ass pussy (ah, ah, ah)
He bought a phone just for pictures of this wet-ass pussy (click, click, click)
Pay my tuition just to kiss me on this wet-ass pussy (mwah, mwah, mwah)
Now make it rain if you wanna see some wet-ass pussy (yuh, yuh)

[Cardi B & Megan Thee Stallion]
Look, I need a hard hitter, need a deep stroker
Need a Henny drinker, need a weed smoker
Not a garter snake, I need a king cobra
With a hook in it, hope it lean over
He got some money, then that's where I'm headed
Pussy A1 just like his credit
He got a beard, well, I'm tryna wet it
I let him taste it, now he diabetic
I don't wanna spit, I wanna gulp
I wanna gag, I wanna choke
I want you to touch that lil' dangly thing that swing in the back of my throat
My head game is fire, punani Dasani
It's goin' in dry and it's comin' out soggy
I ride on that thing like the cops is behind me (yuh, ah)
I spit on his mic and now he tryna sign me, woo

[Megan Thee Stallion]
Your honor, I'm a freak bitch, handcuffs, leashes
Switch my wig, make him feel like he cheatin'
Put him on his knees, give him somethin' to believe in
Never lost a fight, but I'm lookin' for a beatin'
In the food chain, I'm the one that eat ya
If he ate my ass, he's a bottom-feeder
Big D stand for big demeanor
I could make ya bust before I ever meet ya
If it don't hang, then he can't bang
You can't hurt my feelings, but I like pain
If he fuck me and ask: Whose is it?
When I ride the dick, I'ma spell my name, ah

[Cardi B]
Yeah, yeah, yeah, yeah
Yeah, you fuckin' with some wet-ass pussy
Bring a bucket and a mop for this wet-ass pussy
Give me everything you got for this wet-ass pussy
Now from the top, make it drop, that's some wet-ass pussy
Now get a bucket and a mop, that's some wet-ass pussy
I'm talkin' WAP, WAP, WAP, that's some wet-ass pussy
Macaroni in a pot, that's some wet-ass pussy, huh

Hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
There's some hoes in this house
'''
palavras = texto.split()
print(len(palavras))
qtd = Counter(palavras)
qtd10 = qtd.most_common(10)

for qtd in qtd10:
    print(qtd)
