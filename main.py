import os
import subprocess

# Dictionary that maps game names to their corresponding .py file location
games = {
    "Game 1": "game1.py",
    "Game 2": "game2.py",
    "Game 3": "game3.py",
    "Game 4": "game4.py"
}

def display_menu():
    # Set the width and height of the menu
    width = 50
    height = len(games) + 4

    # Create the top and bottom borders
    border = "+" + "-"*(width-2) + "+\n"

    # Create the menu content
    content = ""
    content += border
    content += "|{:^48}|\n".format("Choose a game to play:")
    content += border
    for i, game in enumerate(games):
        content += "|{:^48}|\n".format(f"{i+1}. {game}")
    content += border
    content += "|{:^48}|\n".format("Q. Quit")
    content += border

    # Print the menu
    print("\n" * 5)
    print(content)
    choice = input("Enter your choice: ")
    return choice

while True:
    choice = display_menu()

    # Check if the user wants to quit
    if choice.lower() == "q":
        break

    # Check if the user's choice is valid
    if choice.isnumeric() and int(choice) in range(1, len(games)+1):
        # Get the selected game's .py file location
        game_file = games[list(games.keys())[int(choice)-1]]
        
        # Run the game in a new process
        subprocess.run(["python", game_file])
    else:
        print("Invalid choice. Please choose again.")