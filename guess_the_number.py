import random
number = random.randrange(1,50)
print("The computer had generated a number between 0 and 50 and you need to guess what the number is!")
guess = int(input("Enter your guess: "))
if guess == number:
    print("Well done! ")
elif guess < number:
    print("Your guess is too low")
else:
    print("Your guess is too high! ")
print("The number is :", number)