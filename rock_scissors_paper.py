import random

exit = False
my_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose: Rock, Scissors, Paper or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("GAME OVER!1!")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is a rock")
            print("computer's input is a rock")
            print("IT'S TIE BABY!")
            my_points = my_points
            computer_points = computer_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "paper":
            print("Your input is a rock")
            print("Computer's input is paper")
            print("YOU LOSE MOTHER FUCKER!!!")
            computer_points +=1
            my_points = my_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "scissors":
            print("Your input is a rock")
            print("Computer's input is scissors")
            print("YOU WIN!!!")
            computer_points = computer_points
            my_points += 1
            print(f' Me: {my_points} - Computer: {computer_points}')

    if user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer's input is a rock")
            print("YOU WIN MF!!!")
            my_points += 1
            computer_points = computer_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "paper":
            print("Your input is a paper")
            print("Computer's input is paper")
            print("IT'S S TIE BABY!!!")
            my_points = my_points
            computer_points = computer_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "scissors":
            print("Your input is a paper")
            print("Computer's input is scissors")
            print("YOU LOSE MOTHER FUCKER!!!")
            computer_points += 1
            my_points = my_points
            print(f' Me: {my_points} - Computer: {computer_points}')

    if user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer's input is a rock")
            print("YOU LOSE MOTHER FUCKER!!!")
            computer_points += 1
            my_points = my_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "paper":
            print("Your input is a scissors")
            print("computer's input is paper")
            print("YOU WIN BITCH!!!")
            my_points += 1
            computer_points = computer_points
            print(f' Me: {my_points} - Computer: {computer_points}')

        elif computer_input == "scissors":
            print("Your input is a scissors")
            print("computer's input is scissors")
            print("IT'S A TIE BABY!!!")
            my_points = my_points
            computer_points = computer_points
            print(f' Me: {my_points} - Computer: {computer_points}')

    if my_points == 5:
        print("YOU WIN!!!")

    elif computer_points == 5:
        print("YOU LOSE!!!")

    if my_points == 5 or computer_points == 5:
        break