#Computer randomly Generate a number between 0 - 20
#Ask User to make a guest. if answer is wrong: say value too high or low try again
import random #import module random

usr_guess = 0

print('Hello, What is your name') #Getting input from the user
name = input() #Get value from the user

number = random.randint(1,20) # Getting random value

print("The number im thinking is between 1 and 20, " +name)

while usr_guess < 6:
    print("Take a guest ")
    guest = input()
    guest = int(guest)

    usr_guess = usr_guess + 1

    if guest < number:
        print("number is too low")

    if guest > number:
        print("Number is too high")

    if guest == number:
        break
if guest == number:
    usr_guess = str(usr_guess)
    print("Weldone, " +name ,"You guessed the number in:. " +usr_guess)