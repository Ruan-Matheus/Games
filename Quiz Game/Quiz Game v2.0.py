from time import sleep
from tools import leiaResposta
contador = money = hit = miss = 0
perguntas = [['How many elements are in the periodic table?',[100, 108, 112, 118], 118]]


def pergunta(a, b, c, d):
    for i in perguntas:
    print(f'A){a}    B){b}    C){c}    D){d}')
    

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


print(f'\n{"=========== QUIZ TIME ===========":^20}')

print('\n1) How many elements are in the periodic table? ')
pergunta(100, 108, 112, 118)
resposta = leiaResposta('Your awnser? ')
check_awnser('d')
premio()


print(f'\n2) Which city is known as the "Eternal City?"')
pergunta('Rome', 'New York', 'Paris', 'Londom')
resposta = leiaResposta('Your awnser? ')
check_awnser('a')
premio()

print(f'\n3) Which country win the most World Cup? ')
pergunta('Argentina', 'France', 'Brazil', 'Germany')
resposta = leiaResposta('Your awnser? ')
check_awnser('c')
premio()

print(f'\n4) Which planet have the most moons?')
pergunta('Mercury', 'Saturn', 'Neptune', 'Jupiter')
resposta = leiaResposta('Your awnser? ')
check_awnser('b')
premio()

print(f'\n5) How many bones do we have in the ear?')
pergunta('None', 'One', 'Two', 'Three')
resposta = leiaResposta('Your awnser? ')
check_awnser('d')
premio()

print(f'\n6) What is the capital of New Zeland')
pergunta('Sydney', 'Wellington', 'Auckland', 'Canberra')
resposta = leiaResposta('Your awnser? ')
check_awnser('b')
premio()

print(f"\n7)On what continent would you find the world’s largest desert?")
pergunta('Africa', 'Asia', 'Antartica', 'America')
resposta = leiaResposta('Your awnser? ')
check_awnser('c')
premio()

print(f'\n8) What is the language spoken in Brazil?')
pergunta('Spanish', 'English', 'Portuguese', 'Brazilian')
resposta = leiaResposta('Your awnser? ')
check_awnser('c')
premio()

print(f'\n9) What is the capital of Finland?')
pergunta('Helsinki', 'Stockholm', 'Oslo', 'Copenhagen')
resposta = leiaResposta('Your awnser? ')
check_awnser('a')
premio()

print(f'\n10) In which part of your body would you find the cruciate ligament?')
pergunta('Elbow', 'Knee', 'Fist', 'Ankle')
resposta = leiaResposta('Your awnser? ')
check_awnser('b')
premio()

# print(f'\nWhat is the currency of Denmark??')
# pergunta('Dolar', 'Euro', 'Dutch Guilder', 'Krone')
# resposta = leiaResposta('Your awnser? ')
# check_awnser('d')
# premio()

print(f'\nCongratulations for finishig the Quiz!!! \nYou got {hit} questios right, and you missed {miss}. \nYour final reward is ${money}\n\n') 