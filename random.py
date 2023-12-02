# a game for selecting numbers within a range and checking if the values entered match the random number.
import random
secret_number = random.randint(0,50)

number1 = int(input('Enter a number between 0 and 50: '))
number2 = int(input('Enter a number between 0 and 50: '))
number3 = int(input('Enter a number between 0 and 50: '))
number4 = int(input('Enter a number between 0 and 50: '))
number5 = int(input('Enter a number between 0 and 50: '))
number6 = int(input('Enter a number between 0 and 50: '))

if (secret_number == number1 ):
    print(f'{number1},You win!')
elif (secret_number == number2 ):
    print(f'{number2},You win!')
elif (secret_number == number3 ):
    print(f'{number3},You win!')
elif (secret_number == number4 ):
    print(f'{number4},You win!')
elif (secret_number == number5 ):
    print(f'{number5},You win!')
elif (secret_number == number6 ):
    print(f'{number6},You win!')
else:
    print(f'{secret_number} is the number' )