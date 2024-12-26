import random as rnd
import math as mt

lower = int(input('Enter Lower Number :\t'))
upper = int(input('Enter Upper Number :\t'))

number = rnd.randint(lower,upper)
chance = round(mt.log(upper-lower+1))
print(f'\nyou have {chance} chances to guess the right numberbetween {lower} and {upper}\n')

for i in range(chance):
    guess = int(input('Enter your guess :\t'))
    if guess == number:
        print(f'\n\tCongratulations! You found the number {number} in {i+1} chances')
        break
    elif guess < number :
        print('\tYour guess is too low')
    else:
        print('\tYour guess is too high')
    
    if i == chance-1:
        print(f'\nthe numbe is {number}\n\tyou have reatch your limit better try again!')