from time import sleep
print('-=-'*10)
print('Welcome to my computer quiz!')
score = 0
playing = input('Are you ready to play the Quiz Game?(S/N) ').strip().upper()
if playing != 'S':
    print('Huunf. As I thought, you are afraid.. Well, maybe next time')
    exit()
else:
    print('Nicee! So lets get started!')
print('Pay atention to what you type. One mistake and you might lose!')

# First Question
print('Fist Question! What country has won the most World Cups? ')
print('[A]Brasil  [B]Alemanha [C]Argentina  [D]França')
awnser1 = str(input('Your awnser: ')).strip().upper()
if awnser1 != 'A':
    print('Hahaha what a dummy! Even toddlers know this...Well I guess Im expecting too much of you.')
else:
    print('You are correct! Not bad, but it is only the fist question. Dont get ahead of yourself')
    score += 1
    
# Second Question
print('So here comes the second question: \nSecond question! What is the most common surname in the USA?')
print('[A]Johnson  [B]Willian  [C]Smith  [D]Jackson')
awnser2 = str(input('Your awnser: ')).strip().upper()
if awnser2 != 'C':
    print('Tsc tsc... I should have know...Incorrect!')
else:
    print('Good. You are correct!')
    score += 1
    
# Third Question
print('Let the third question come! \nThird question! Which planet has the most moons?')
print('[A]Saturn  [B]Mars  [C]Neptune  [D]Jupiter')
awnser3 = str(input('Your awnser: ')).strip().upper()
if awnser3 != 'A':
    print('And you awnser is....', end =' ')
    sleep(1)
    print('Incorrect of course!')
else:
    print('You are correct...It seems you got lucky this time')
    score += 1
    
# Forth Question
print('Dont get distracted! \nForth question! What country has the most islands? ')
print('[A]Canada  [B]Indonesia  [C]Norway  [D]Sweden')
awnser4 = str(input('Your awnser: ')).strip().upper()
if awnser4 != 'D':
    print('It is common for you humans to miss this question, dont fell to bad about yourself')
else:
    print('Wow! You got this? Not bad. I will give you a point for that')
    score += 1 

# Fifth Question
print('Wow this one is interesting! \nFifth question! In what year was python released? ')
print('[A]1987  [B]1989  [C]1991  [D]1994')
awnser5 = str(input('Your awnser: ')).strip().upper()
if awnser5 != 'C':
    print('Wrong! You are studying python, how do you even miss question like these...')
else:
    print('You are correct! Too easy? Maybe I should increase the difficult of the next question.')
    score += 1    

# Sixth Question
print('I love geography questions, so bear with me. \nSixth question! What is the smallest country in the world? ')
print('[A]San Marino  [B]Vatican City  [C]Butan  [D]Liechtenstein')
awnser6 = str(input('Your awnser: ')).strip().upper()
if awnser6 != 'B':
    print('The pope will get mad at you if you keep going like this. Wrong!')
else:
    print('Have you ever been there? Hm...Strange. You arent cheating are you? You arent allowed to search it up!')
    score += 1

# Seventh Question
print('How much do you know about yourself? \nSeventh question! What is the largest human bone? ')
print('[A]Fibula  [B]Tibia  [C]Humerus  [D]Femur ')
awnser7 = str(input('Your awnser: ')).strip().upper()
if awnser7 != 'D':
    print('I guess you dont know much about yourself...Wrong!')
else:
    print('Hunf. That was an easy question.')
    score += 1

# Eigth Question
print('We are almost in the end...\nEighth question! What is the hottest plannet in our solar systen?')
print('[A]Mars  [B]Venus  [C]Mercury  [D]Jupiter')
awnser8 = str(input('Your awnser: ')).strip().upper()
if awnser8 != 'B':
    print('You dont understand the basics? Do I really have to explain that for you? Ahhh! Just think about the greenhouse effect!')
else:
    print('Correct! Not many people know about this one. Not bad!')
    score += 1

# Ninth Question
print('The second last question! \nNinth question! What is the capital of Australia?')
print('[A]Sydney  [B]Melboune  [C]Brisbane  [D]Canberra')
awnser9 = str(input('Your awnser: ')).strip().upper()
if awnser9 != 'D':
    print('...Wrong')
else:
    print('You are...', end = ' ')
    sleep(2)
    print('Correct!')
    score += 1

# Tenth Question
print('And finally the tenth and last question! What is the nation sport of Japan? ')
print('[A]Baseball  [B]Sumo  [C]Karate  [D]Kendo')
awnser10 = str(input('Your awnser: ')).strip().upper()
if awnser10 != 'B':
    print('You are co- Wrong! I fooled you right? Hahaha! Dummy.')
else:
    print('You are correct. Dont waste more of my time and just keep going.')
    score += 1
    
# Result
print('That was the final question! Now, lets calculate your score!')
print('Calculating...')
sleep(2)
if score == 0:
    print(f'Your score is {score}! Can someone really be this dumb?! \nLife must be hard for you... poor you I guess.')
elif score < 6:
    print(f'Your score is {score}! You are really not smart, right?! \nIt should be normal for humans although')
elif score < 10:
    print(f'Your score is {score}! Not that bad huh. But that it, you will never be able to compare to my greatself!')
else:
    print(f'Your score is {score}! 10??? Did you really get the 10 questions right? No...This must be a bug! \nHahaha this coder is really an idiot, he cant even right a few lines right')
print('YOU GOT {}% OF THE QUIZ RIGHT. '.format((score/10)*100))
print('-=-'*10)
   
