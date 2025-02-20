import random

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe: Player vs. Player Edition!")
    while True:
        player_1 = input("Player #1 - Please choose a symbol (X/O): ")
        player_1 = player_1.upper()
        if player_1 == "X":
            print("Player #1 will use the symbol X and player #2 will use the symbol O")
            break
        elif player_1 == "O":
            print("Player #1 will use the symbol O and player #2 will use the symbol X")
            break
        else:
            invalid_input = input("Invalid input, please try again or type STOP to stop the program. ")
            if invalid_input.upper() == "STOP":
                break
    
    print("\nRandomly choosing starting player...")
    choose_starting_player = random.randint(0, 1)
    if choose_starting_player == 0:
        print("Player #1 is the starting player!")
    else:
        print("Player #2 is the starting player!")



