# import random module
import random


# defined a function that actually rolls the dice
def roll_dice():
    # define a dictionary that will hold the drawings of the dice
    dice_drawings = {
        1: (
            "⚀"
        ),
        2: (
            "⚁"
        ),
        3: (
            "⚂"
        ),
        4: (
            "⚃"
        ),
        5: (
            "⚄"
        ),
        6: (
            "⚅"
        )
    }
    # asks if we want to roll dice
    roll = input("Roll Dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)
        dice5 = random.randint(1, 6)

        # prints out the random rolled dice numbers as well as the keyboard shortcut drawing
        print("Dice rolled: {} and {} and {} and {} and {}".format(dice1, dice2, dice3, dice4, dice5))
        print("\n".join(dice_drawings[dice1]))
        print("\n".join(dice_drawings[dice2]))
        print("\n".join(dice_drawings[dice3]))
        print("\n".join(dice_drawings[dice4]))
        print("\n".join(dice_drawings[dice5]))

        # asks if we want to roll dice again
        roll = input("Roll again? (Yes/No): ")


roll_dice()
