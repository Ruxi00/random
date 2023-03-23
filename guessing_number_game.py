import random

while True:
    n = random.randrange(1,5)
    guess = int(input("Enter any number: "))
    while n != guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))
    else:
        print("you guessed it right!")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
