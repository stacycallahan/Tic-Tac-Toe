import random
import grid

if __name__ == "__main__":
    # Game setup
    print("Welcome to Tic Tac Toe: Player vs. Player Edition!\n")
    player_to_symbol = {}
    while True:
        player_1 = input("Player #1 - Please choose a symbol (X/O): ")
        player_1 = player_1.upper()
        if player_1 == "X":
            player_to_symbol[1] = 'X'
            player_to_symbol[2] = 'O'
            break
        elif player_1 == "O":
            player_to_symbol[1] = 'O'
            player_to_symbol[2] = 'X'
            break
        else:
            print("Invalid input, please try again.")
    
    print(f"Player #1 will use the symbol {player_to_symbol[1]} and player #2 will use the symbol {player_to_symbol[2]}")
    
    print("\nRandomly choosing starting player...")
    player_to_starting = {}
    starting_player = random.randint(0, 1)
    if starting_player == 0:
        player_to_starting['starting'] = 1
        player_to_starting['not starting'] = 2
    else:
        player_to_starting['starting'] = 2
        player_to_starting['not starting'] = 1
    print(f"Player #{player_to_starting['starting']} is the starting player!\n")
    
    tracker = {}
    for i in range(0, 3):
        for j in range(0, 3):
            position_tuple = (i + 1, j + 1)
            tracker[position_tuple] = f'{i + 1},{j + 1}'

    grid.print_grid(tracker)
    print("Welcome to the Tic Tac Toe Grid!\n")

    winning_positions = {}
    winning_position = 0
    
    # Horizontal winning positions
    for i in range(3):
        winning_positions[winning_position] = []
        for j in range(3):
            winning_positions[winning_position].append((i + 1, j + 1))
        winning_position += 1
    
    # Vertical winning positions
    for i in range(3):
        winning_positions[winning_position] = []
        for j in range(3):
            winning_positions[winning_position].append((j + 1, i + 1))
        winning_position += 1
    
    # Diagonal winning position #1
    winning_positions[winning_position] = []
    for i in range(3):
        winning_positions[winning_position].append((i + 1, i + 1))
    winning_position += 1

    # Diagonal winning position #2
    winning_positions[winning_position] = []
    row = 3
    for i in range(3):
        winning_positions[winning_position].append((row, i + 1))
        row += -1

    # Gameplay
    current_player = 'starting'
    move_number = 1
    while True:
        while True:
            mark = input(f"Player #{player_to_starting[current_player]} - Type a string of the form #,# to make your move: ")
            if len(mark) == 3:
                if mark[0].isnumeric() and mark[1] == ',' and mark[2].isnumeric():
                    if int(mark[0]) >= 1 and int(mark[0]) <= 3 and int(mark[2]) >= 1 and int(mark[2]) <= 3:
                        if tracker[int(mark[0]), int(mark[2])] == f"{mark[0]},{mark[2]}":
                            break
                        else:
                            print("Position taken, please try again.")
                    else:
                        print("Invalid input, please try again.")
                else:
                    print("Invalid input, please try again.")
            else:
                print("Invalid input, please try again.")
        tracker[int(mark[0]), int(mark[2])] = f" {player_to_symbol[player_to_starting[current_player]]} "
        grid.print_grid(tracker)
        print()

        # Check for winner
        winner = False
        if move_number >= 5:
            for i in range(8):
                flag = True
                for j in range(3):
                    if tracker[winning_positions[i][j]] != f' {player_to_symbol[player_to_starting[current_player]]} ':
                        flag = False
                if flag == True:
                    winner = True
                    break
        
        if winner == True:
            print(f"Player #{player_to_starting[current_player]} wins!")
            break
        elif move_number == 9:  # Check for tie
            print('Tie!')
            break

        if current_player == 'starting':
            current_player = 'not starting'
        else:
            current_player = 'starting'
        move_number += 1