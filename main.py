import random


def color_picked(number):
    if number == 1:
        choice = "Blue"
    elif number == 2:
        choice = "Yellow"
    elif number == 3:
        choice = "Orange"
    elif number == 4:
        choice = "Green"
    elif number == 5:
        choice = "Red"
    return choice


if __name__ == '__main__':
    computer_score = 0
    player_score = 0

    while True:
        # Instruction for play
        print(
            "Wining Rules of the CC Game : " + "\nEnter a number from 1-5 and match computer choice to beat the computer")

        print("Blue = 1 \nYellow = 2 \nOrange = 3 \nGreen = 4 \nRed = 5")
        # Input from player
        player_choice = int(input("Player turn: "))

        # Check until the input is correct
        while player_choice > 5 or player_choice < 1:
            player_choice = int(input("Enter valid input:"))

        choice_col = color_picked(player_choice)

        print("Player color choice is: " + choice_col)
        print("\nNow its computer turn to choose a color: ")

        # Computer choose randomly any color
        computer_choice = random.randint(1, 5)

        while computer_choice == player_choice:
            computer_choice = random.randint(1, 5)

        computer_choice_col = color_picked(computer_choice)

        print("Computer color choice is: " + computer_choice_col)

        # condition to win
        if choice_col == computer_choice_col:
            player_score += 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
        else:
            computer_score += 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))

        print("Do you want to play again? (Y/N)")
        answer = input()

        if answer == 'n' or answer == 'N':
            break
