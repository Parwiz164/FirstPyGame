import random

# Define player starting point
player_position = 0

# Define list of locations of the player
locations = {
    0: "You're in a dark room.",
    1: "You're in a forrest.",
    2: "You're on a beach.",
    3: "You're in a cave."
}

# Define a list of the available actions
actions = {
    "go": "Go to another location.",
    "research": "Research the environment.",
    "pause": "Pause the game."
}


# Define the function to process actions from the player
def player_actions(player_action):
    global player_position
    if player_action == "go":
        player_position = random.choice(list(locations.keys()))
        print(locations[player_position])
    elif player_action == "research":
        print("You don't see anything special.")
    elif player_action == "pause":
        print("The game is paused.")
        exit()
    else:
        print("Invalid action. Please try again.")


# Structure of the game
while True:
    # Current location of the player
    print(locations[player_position])
    print()

    # Available actions of the player
    print("Available actions:")
    for action in actions:
        print(action + ":", actions[action])
    print()

    # Read player input
    player_input = input("What do you want to do? ")

    # Process actions of the player
    player_actions(player_input)
