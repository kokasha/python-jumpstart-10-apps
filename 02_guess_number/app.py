import random

print('-' * 30)
print('         Guess the Number')
print('-' * 30)

number = random.randint(0,100)

user = input('What is you name Mate! ')

# initial guess to set the variable
guess = -1

while guess != number:
    guess_text = input('Please Guess a Number between 0 and 100: ')
    guess = int(guess_text)

    if guess < number:
        print('Sorry {}, your guess of {} was Too Low'.format(user, guess))
    elif guess > number:
        print('Sorry {}, your guess of {} was Too HIGH'.format(user, guess))
    else:
        print('Excellent Work {}, the right guess was {}'.format(user, guess))

print('You Win!')