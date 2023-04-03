print("***Welcome to the guessing game***")

import random #to get random number for guessing

def play_game(): # a function is created to start the game
    
    lowest = 1
    highest = 100
    print("I'm thinking of a number between", lowest, "and", highest,".")
    print("Do you want to play?")
    chances = int(input("Choose the number of chances you would like to try: "))
    answer = generate_random_number(lowest, highest) 
    
    guesses = 0
    while True:
        guess = input("Take a guess (or Q to quit it): ") # it will take input from the user to paly or quit the game
        if guess == "Q": # here Q to show the user quiting the game
            print("***Game quitted***")
            break
        guess = int(guess)
        guesses += 1 #this variable will show how many times we tried guessing to guess the number
        if guess == answer:
            print("!!!Congratulations!!! You guessed the number in", guesses, "guesses.")
            break
        elif guess < answer:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        if guesses == chances: # if guessing is equal to the required tries or chances it will show this output
            print("Sorry, you ran out of chances. The number was", answer)
            break

def generate_random_number(low, high):
    return random.randint(low, high)

play_game()
