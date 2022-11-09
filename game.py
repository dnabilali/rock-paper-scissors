def validate_input(input):
    valid_input = ["rock", "paper", "scissors"]
    if input.lower() in valid_input:
        return True
    return False

def winner():
    player_1 = ""
    player_2 = ""

    while not validate_input(player_1):
        player_1 = input("Please choose rock, paper or scissors for the first player: ")
        player_1 = player_1.lower()
    
    while not validate_input(player_2):
        player_2 = input("Please choose rock, paper or scissors for the second player: ")
        player_2 = player_2.lower()

    inputs = [player_1, player_2]

    if player_1 == player_2:
        return "It's a tie!"

    if ("scissors" in inputs) and ("rock" in inputs):
        if "rock" == inputs[0]:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    if ("scissors" in inputs) and ("paper" in inputs):
        if "scissors" == inputs[0]:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    if ("paper" in inputs) and ("rock" in inputs):
        if "paper" == inputs[0]:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

print(winner())
