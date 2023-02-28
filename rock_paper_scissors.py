import random
computer_points = 0
user_points = 0

while True:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    if user_input == "exit":
        print("Game ended")
        print(f"Your points:{user_points}")
        print(f"Computer points:{computer_points}")
        break
    if user_input == "rock":
        if computer_input == "rock":
            print("Your choise is rock")
            print("Computer choise is rock")
            print("Its a tie")
        elif computer_input == "paper":
            print("Your choise is rock")
            print("Computer choise is paper")
            print("Computer won")
            computer_points +=1
        elif computer_input == "scissors":
            print("Your choise is rock")
            print("Computer choise is scissors")
            print("You won")
            user_points += 1
    elif user_input == "paper":
        if computer_input == "paper":
            print("Your choise is paper")
            print("Computer choise is paper")
            print("Its a tie")
        elif computer_input == "rock":
            print("Your choise is paper")
            print("Computer choise is rock")
            print("You won")
            user_points +=1
        elif computer_input == "scissors":
            print("Your choise is paper")
            print("Computer choise is scissors")
            print("Computer won")
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "scissors":
            print("Your choise is scissors")
            print("Computer choise is scissors")
            print("Its a tie")
        elif computer_input == "rock":
            print("Your choise is scissors")
            print("Computer choise is rock")
            print("Computer won")
            computer_points +=1
        elif computer_input == "paper":
            print("Your choise is scissors")
            print("Computer choise is paper")
            print("You won")
            user_points += 1
    elif user_input != " rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid Input")
