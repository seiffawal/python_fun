import os
import random

# Global variables
chance = 6
random_line = ''
listtemp = []

def endgame(won):
    print("The word was:", random_line)
    if won:
        print("Congratulations, you won!")
    else:
        print("Game Over! Better luck next time.")
    exit()  # Exit the program

def print_stickman(chance):
    red = '\033[31m'
    reset = '\033[0m'
    stages = [
        f"""
           -----
           |   |
           {red}O   |{reset}
          {red}/|\\  |{reset}
          {red}/ \\  |{reset}
               |
        --------
        """,
        f"""
           -----
           |   |
           {red}O   |{reset}
          {red}/|\\  |{reset}
          {red}/    |{reset}
               |
        --------
        """,
        f"""
           -----
           |   |
           {red}O   |{reset}
          {red}/|\\  |{reset}
               |
               |
        --------
        """,
        f"""
           -----
           |   |
           {red}O   |{reset}
          {red}/|   |{reset}
               |
               |
        --------
        """,
        f"""
           -----
           |   |
           {red}O   |{reset}
           {red}|   |{reset}
               |
               |
        --------
        """,
        f"""
           -----
           |   |
           {red}O   |{reset}
               |
               |
               |
        --------
        """,
        f"""
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[chance]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game():
    clear_screen()
    stickman = print_stickman(chance)
    print(random_line)
    print(f"Chances left: {chance}")
    print("Word:", " ".join(listtemp))
    print("\n" * (20 - len(stickman.splitlines())), end="")  # Adjust spacing to align stickman on the right
    print("\n".join(stickman.splitlines()))

def give_hint(word):
    # Reveal a random letter that has not been guessed yet
    unrevealed_indices = [i for i, char in enumerate(word) if listtemp[i] == '_']
    if unrevealed_indices:
        hint_index = random.choice(unrevealed_indices)
        listtemp[hint_index] = word[hint_index]
        return f"Hint: One of the letters is '{word[hint_index]}'"
    else:
        return "No more hints available."

filepath = "text.txt"

# Read the file and get all lines
with open(filepath, 'r') as file:
    lines = file.readlines()

# Select a random line and strip any leading/trailing whitespace
random_line = random.choice(lines).strip().lower()
listtemp = ['_' if ch != ' ' else ' ' for ch in random_line]  # Use underscore for unknown letters

# Provide an initial hint
hint = give_hint(random_line)
print(hint)

# Initial display
display_game()

# Initialize complete as the number of underscores in listtemp
complete = len([ch for ch in listtemp if ch == '_'])

# Main game loop
while chance > 0:
    guess = input("Guess a character: ").strip().lower()

    if guess in random_line:
        for index, charel in enumerate(random_line):
            if guess == charel:
                if listtemp[index] == '_':  # Check if the position is not already revealed
                    listtemp[index] = guess
                    complete -= 1
        display_game()
        if complete == 0:
            endgame(True)
    else:
        chance -= 1
        display_game()

if chance == 0:
    endgame(False)
