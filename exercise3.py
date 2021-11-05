import random

number=random.randint(1,101)
guess = None
while guess != number:
    guess = int(input('your guess: '))
    if guess > number:
        print('decrease your number')
    elif guess < number:
        print('increase your number')
    else:
        print('you guessed right')
  

    

    
