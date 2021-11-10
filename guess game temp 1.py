secret_number = 8
i = 0
k = 3
answer = False
list1 = ["1st","2nd","3rd"]
while int(i) < int(k) :
    message = f'First Game {list1[i]} chance : '
    guess = int(input(message))
    i +=1
    if 8 < int(guess) < 20 :
        if int(i) == 3 :
            break
        else:
            print('''
You Are Near To The Number Once Again Try
''')
    elif int(guess) is not int(secret_number) :
        if int(i) == 3 :
            break
        else :
            print('''
Wrong Number Let's Try Again
''')
    elif guess == secret_number :
        print('''
You Won First Game Lets Try Another Game And Prove That You Are Genius''')
        break
if int(i) >= int(k) :
    print('''
Your Chances Are Over Lets' Try A New Game''')
    
secret_number = 10
i = 0
k = 3
while int(i) < int(k) :
    guess = int(input('''
Second Game : '''))
    i +=1
    if int(guess) >10 :
        if int(i) == 3 :
            break
        else:
            print('Less Than That Once Again Try')
    elif int(guess) is not int(secret_number) :
        print("Wrong Number Let's Try Again")
    elif guess == secret_number :
        print('''
You Won''')
        break

print('''
❤ Copyright Deserves To Ajay Ganesh Only.
Thanks For Trying My Game.''')
