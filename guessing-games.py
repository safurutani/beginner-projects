import random
def computerGuess(x):
    low = 1
    high = x
    response = ""
    while response != "c":
        num = random.randint(low,high)
        print("My guess is " + str(num))
        response = input("Is my guess too low (L), too high (H), or correct (C)?\n").lower()
        if response == "l":
            low = num + 1
        elif response == "h":
            high = num - 1
        elif response != "c":
            print("Invalid input")
    print("Hooray! I guessed the right number!\n Thanks for playing :)")

def userGuess(x):
    secret = random.randint(1, x)
    guess = 0
    print("I have randomly picked a number from 1 through " + str(x))
    while int(guess) != secret:
        guess = input("Please enter your guess: ")
        if int(guess) < secret:
            print("Your guess is too low. Try again.\n")
        elif int(guess) > secret:
            print("Your guess is too high. Try again.\n")
    print("That's correct! You win!\nThanks for playing :)\n")

#gives the option to replay games
def playAgain():
    again = input("Would you like to play another game?(Y/N)\n").lower()
    if again == "y":
        return True
    elif again == "n":
        return False
    else:
        print("Invalid response")

#choose which game to play
playing = True
while playing:
    game = input("Which game would you like to play?\n(1) Computer Guesses\n(2) User guesses\n")
    if game == "1":
        max = input("Okay! What would you like the number limit to be?\n")
        computerGuess(int(max))
        playing = playAgain()
    elif game == "2":
        max = input("Okay! What would you like the number limit to be?\n")
        userGuess(int(max))
        playing = playAgain()
    else:
        print("Invalid option")
print("See you next time.")
