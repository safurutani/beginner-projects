import random
exit = False
cpu = 0
you = 0
while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ")
    computer_input = random.choice(options)
    if user_input == "exit":
        print("Game ended\n")
        if you > cpu:
            print(f"Congratulations you beat the computer! You won {you} times. The computer won {cpu} times.")
        elif you == cpu:
            print(f"You were evenly matched with the computer! You both won {you} times.")
        else:
            print(f"Too bad, the computer beat you. You won {you} times. The computer won {cpu} times.")
        exit = True
    if user_input.lower() == "rock":
        print("You: rock")
        if computer_input == "rock":
            print("CPU: rock")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("CPU: scissors")
            print("You win!")
            you += 1
        else:
            print("CPU: paper")
            print("CPU wins.")
            cpu += 1
        print("")
    if user_input.lower() == "paper":
        print("You: paper")
        if computer_input == "paper":
            print("CPU: paper")
            print("It's a tie!")
        elif computer_input == "rock":
            print("CPU: rock")
            print("You win!")
            you += 1
        else:
            print("CPU: scissors")
            print("CPU wins.")
            cpu += 1
        print("")
    if user_input.lower() == "scissors":
        print("You: scissors")
        if computer_input == "scissors":
            print("CPU: scissors")
            print("It's a tie!")
        elif computer_input == "paper":
            print("CPU: paper")
            print("You win!")
            you += 1
        else:
            print("CPU: rock")
            print("CPU wins.")
            cpu += 1
        print("")