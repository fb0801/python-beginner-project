import random



def guess(x):
    random_num =random.randint(1,x)
    guess=0

    while guess != random_num:
        guess =int(input(f"guess a number between 1 and {x}: "))
        if guess < random_num:
            print("your guess is too low")
        elif guess > random_num:
            print ("Guess is too high")
    print(f"Great work you have guessed the number:{random_num}")



def computer_guess(x):
    low=1
    high=x
    feedback=' '
    while feedback !='c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess = low
        feedback =input(f'Is {guess} too high (H) , too low (L) or correct (c)?').lower()
        if feedback =='h':
            high= guess-1
        elif feedback =='l':
            low = guess +1

    print(f'Yay i guessed your number human, {guess}')
            
        
    



computer_guess(10)
#feed the function a number range
