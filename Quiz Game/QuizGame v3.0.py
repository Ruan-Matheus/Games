from time import sleep
from tools import leiaResposta
from random import shuffle
contador = money = hit = miss =  0
cont = 1

perguntas = [
['How many elements are in the periodic table?',[100, 108, 112, 118], 'd'], 
['Which city is known as the "Eternal City?"',['Rome', 'New York', 'Paris', 'Londom'],'a'], 
['Which country won the most World Cup? ', ['Argentina', 'France', 'Brazil', 'Germany'], 'c'],
['Which planet have the most moons?', ['Mercury', 'Saturn', 'Neptune', 'Jupiter'], 'b'], 
['How many bones do we have in the ear?', ['None', 'One', 'Two', 'Three'], 'd'], 
['What is the capital of New Zeland', ['Sydney', 'Wellington', 'Auckland', 'Canberra'], 'b'],
["On what continent would you find the world’s largest desert?", ['Africa', 'Asia', 'Antartica', 'America'], 'c'], 
['What is the language spoken in Brazil?', ['Spanish', 'English', 'Portuguese', 'Brazilian'], 'c'], 
['What is the capital of Finland?', ['Helsinki', 'Stockholm', 'Oslo', 'Copenhagen'], 'a'], 
['In which part of your body would you find the cruciate ligament?', ['Elbow', 'Knee', 'Fist', 'Ankle'], 'b'], 
['What is the currency of Denmark?', ['Dolar', 'Euro', 'Dutch Guilder', 'Krone'], 'd']
]

shuffle(perguntas)

def pergunta(pergunta, a, b, c, d, resp):
    global resposta, cont
    print(f'\n{cont}){pergunta}')
    print(f'A){a}    B){b}    C){c}    D){d}')
    resposta = leiaResposta('Your awnser? ')
    check_awnser(resp)
    premio()
    cont += 1


def check_awnser(a):
    global resposta
    if resposta == a:
        correct_awnser()
    else:
        wrong_awnser()


def correct_awnser():
    global contador, money, hit
    contador += 1
    print('Correct awnser!')
    money = contador * 100000
    hit += 1


def wrong_awnser():
    global miss
    print('Wrong Awnser!')
    miss += 1


def premio():
    global money
    print(f'Final reward: {money}$')

print(f'\n{"=============== QUIZ TIME ===============":^20}')

for m in range(5):
    pergunta(perguntas[m][0], perguntas[m][1][0], perguntas[m][1][1], perguntas[m][1][2], perguntas[m][1][3], perguntas[m][2])
