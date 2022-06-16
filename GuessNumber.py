import random

z, y = input("Enter the range of numbers to guess from: ").split(" ")
x = random.randint(int(z), int(y))
count = 0
while True:
    count += 1
    guess = eval(input("Guess the number: "))
    if guess == x:
        print("You are correct")
        print("You got it in {} tries".format(count))
        quit()
    elif guess > x:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
