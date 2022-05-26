from random import randint
import random
t = ["Rock", "Paper", "Scissors"]
count = 0
win = 0
loss = 0
while (count <= 2):
    comp = t[random.randint(0,2)]
    play = input("Rock, Paper, Scissors?: ")
    print("Computer played ", comp)
    if play == t[0]:
        if comp == play:
            print("It is a tie.\n")
        elif comp == t[1]:
            print("Paper covers rock, you loose\n")
            loss = loss + 1
        else:
            print("Rock beats scissors, you win\n")
            win = win + 1
    elif play == t[1]:
        if comp == play:
            print("It is a tie.\n")
        elif comp == t[0]:
            print("Paper covers rock, you win\n")
            win = win + 1
        else:
            print("Scissors cuts paper, you loose\n")
            loss = loss + 1
    elif play == t[2]:
        if comp == play:
            print("It is a tie.\n")
        elif comp == t[1]:
            print("Scissors cuts paper, you win\n")
            win = win + 1
        else:
            print("Rock beats scissors, you loose\n")
            loss = loss + 1
    count = count + 1
print("Computer -", loss, "   :   You -", win)
    
