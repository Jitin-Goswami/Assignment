# Dice Roll Simulator

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the die...")  # Wait for user input
    print(f"You rolled a {roll_dice()}! 🎲")
    
    play_again = input("Roll again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
