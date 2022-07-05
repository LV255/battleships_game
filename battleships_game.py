import random
import time

gamerunning = False

# set size of grid
# current game is designed for 10 by 10, if changed code would need to be adapted
num_of_columns = 10
num_of_rows = 10

# alphabet for display
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# keep track of player variables
player_ship_location = []
computer_ship_location = []

number_of_ships = 0
number_of_computer_ships = 0

number_of_ships_sunk = 0
number_of_computer_ships_sunk = 0


# create player grid
def create_grid():
    global grid

    grid = []
    for r in range(num_of_rows):
        row = []
        for c in range(num_of_columns):
            row.append(". ")
        grid.append(row)

# print player grid
def print_grid():
    print("    ###   Player board   ###   ")
    print(" ", end=" ")
    for num in range(num_of_columns):
        print(str(num) + " ", end= " ")
    print()
    for x in range(num_of_columns):
        print(alphabet[x], end= " ")
        for y in range(num_of_rows):
            print(grid[y][x], end=" ")
        print(alphabet[x], end=" ")
        print()

    print(" ", end=" ")

    for num in range(num_of_columns):
        if num < 10:
            print(str(num) + " ", end=" ")
        else:
            print(str(num), end=" ")
    print()
    print()


# create computer grid
def create_computer_grid():
    global computer_grid

    computer_grid = []
    for r in range(num_of_rows):
        row = []
        for c in range(num_of_columns):
            row.append(". ")
        computer_grid.append(row)

# print computer grid
def print_computer_grid():
    print("   ###   Computer board   ###   ")
    print(" ", end=" ")
    for num in range(num_of_columns):
        print(str(num) + " ", end= " ")
    print()
    for x in range(num_of_columns):
        print(alphabet[x], end= " ")
        for y in range(num_of_rows):
            print(computer_grid[y][x], end=" ")
        print(alphabet[x], end=" ")
        print()

    print(" ", end=" ")

    for num in range(num_of_columns):
        if num < 10:
            print(str(num) + " ", end=" ")
        else:
            print(str(num), end=" ")
    print()
    print()


# create computer grid visible to player during gameplay
def create_visible_computer_grid():
    global visible_computer_grid

    visible_computer_grid = []
    for r in range(num_of_rows):
        row = []
        for c in range(num_of_columns):
            row.append(". ")
        visible_computer_grid.append(row)

# print visible computer grid
def print__visible_computer_grid():
    print("   ###   Computer board   ###   ")
    print(" ", end=" ")
    for num in range(num_of_columns):
        print(str(num) + " ", end= " ")
    print()
    for x in range(num_of_columns):
        print(alphabet[x], end= " ")
        for y in range(num_of_rows):
            print(visible_computer_grid[y][x], end=" ")
        print(alphabet[x], end=" ")
        print()

    print(" ", end=" ")

    for num in range(num_of_columns):
        if num < 10:
            print(str(num) + " ", end=" ")
        else:
            print(str(num), end=" ")
    print()
    print()


# place player ships on the grid
def check_and_decide_ship_location(length_of_ship):

    global grid
    global number_of_ships

    # a ship four in length will need 3 extra squares past its starting square
    squares_to_add = length_of_ship - 1

    placement_complete = False

    while placement_complete is False:

        try:
            start_location_input = input("choose start position of ship (eg. E5): ").strip().upper()
            if start_location_input[0].isalpha() and len(start_location_input) == 2:

                row = alphabet.find(start_location_input[0])
                column = int(start_location_input[1])

                if grid[column][row] == ". ":

                    # create list of possible ship end positions
                    total_positions = ""

                    can_go_right = True
                    can_go_left = True
                    can_go_up = True
                    can_go_down = True

                    # remove ship positions that cannot be used
                    for x in range(length_of_ship):
                        if not (column + x < num_of_columns) or (grid[column + x][row] != ". "):
                            can_go_right = False
                        if not (column - x > -1) or (grid[column - x][row] != ". "):
                            can_go_left = False
                        if not (row - x > -1) or (grid[column][row - x] != ". "):
                            can_go_up = False
                        if not (row + x < num_of_rows) or (grid[column][row + x] != ". "):
                            can_go_down = False

                    # save possible end locations and add to options list as strings
                    if can_go_right:
                        total_positions += alphabet[row] + str(column + squares_to_add) + " "
                        go_right_end = alphabet[row] + str(column + squares_to_add)
                    if can_go_left:
                        total_positions += alphabet[row] + str(column - squares_to_add) + " "
                        go_left_end = alphabet[row] + str(column - squares_to_add)
                    if can_go_up:
                        total_positions += alphabet[row - squares_to_add] + str(column) + " "
                        go_up_end = alphabet[row - squares_to_add] + str(column)
                    if can_go_down:
                        total_positions += alphabet[row + squares_to_add] + str(column) + " "
                        go_down_end = alphabet[row + squares_to_add] + str(column)

                    # if no options available pass and restart the placement loop
                    if can_go_right is False and can_go_left is False and can_go_up is False and can_go_down is False:
                        print("sorry, no options")
                        pass
                    # if positions exist, print options to terminal and ask for selection
                    else:
                        print("Possible end positions: " + total_positions)
                        end_input = input("choose end position of ship: ").strip().upper()

                        # add selected option to the grid, save location for future use, add to number of ships tally
                        if can_go_right and (end_input == go_right_end):
                            for x in range(length_of_ship):
                                grid[column + x][row] = "X "
                                placement_complete = True
                            end_row = row
                            end_column = column + (length_of_ship - 1)
                            player_ship_location.append([column, end_column, row, end_row])
                            number_of_ships += 1

                        if can_go_left and (end_input == go_left_end):
                            for x in range(length_of_ship):
                                grid[column - x][row] = "X "
                                placement_complete = True
                            end_row = row
                            end_column = column - (length_of_ship - 1)
                            # if moving left record end_colum (smaller value) first, needed for checking later
                            player_ship_location.append([end_column, column, row, end_row])
                            number_of_ships += 1

                        if can_go_up and (end_input == go_up_end):
                            for x in range(length_of_ship):
                                grid[column][row - x] = "X "
                                placement_complete = True
                            end_row = row - (length_of_ship - 1)
                            end_column = column
                            # if moving up record end_row (smaller value) first, needed for checking later
                            player_ship_location.append([column, end_column, end_row, row])
                            number_of_ships += 1

                        if can_go_down and (end_input == go_down_end):
                            for x in range(length_of_ship):
                                grid[column][row + x] = "X "
                                placement_complete = True
                            end_row = row + (length_of_ship - 1)
                            end_column = column
                            player_ship_location.append([column, end_column, row, end_row])
                            number_of_ships += 1

            # if input typed incorrectly, pass and reset process
            else:
                pass
        # if errors encountered, pass and reset process
        except (ValueError, IndexError, NameError):
            pass

        # print grid to show where ships have been placed
        # print_grid()

# place computer ships on the grid
def computer_check_and_decide_ship_location(length_of_ship):

    global computer_grid
    global number_of_computer_ships

    # a ship four in length will need 3 extra squares past its starting square
    squares_to_add = length_of_ship - 1

    placement_complete = False

    while placement_complete == False:

        # randomly choose starting location for ship
        num_a = random.randint(0, 9)
        num_b = random.randint(0, 9)
        row = num_a
        column = num_b

        if computer_grid[column][row] == ". ":

            # create list of possible ship end positions
            options_list = []

            can_go_right = True
            can_go_left = True
            can_go_up = True
            can_go_down = True

            # remove ship positions that cannot be used
            for x in range(length_of_ship):
                if not (column + x < num_of_columns) or (computer_grid[column + x][row] != ". "):
                    can_go_right = False
                if not (column - x > -1) or (computer_grid[column - x][row] != ". "):
                    can_go_left = False
                if not (row - x > -1) or (computer_grid[column][row - x] != ". "):
                    can_go_up = False
                if not (row + x < num_of_rows) or (computer_grid[column][row + x] != ". "):
                    can_go_down = False

            if can_go_right:
                go_right_end = alphabet[row] + str(column + squares_to_add)
                options_list.append("right")
            if can_go_left:
                go_left_end = alphabet[row] + str(column - squares_to_add)
                options_list.append("left")
            if can_go_up:
                go_up_end = alphabet[row - squares_to_add] + str(column)
                options_list.append("up")
            if can_go_down:
                go_down_end = alphabet[row + squares_to_add] + str(column)
                options_list.append("down")

            if can_go_right is False and can_go_left is False and can_go_up is False and can_go_down is False:
                pass
            else:
                rannum = random.randint(0, len(options_list) - 1)
                choice = options_list[rannum]

                # add selected option to computer grid, save location for future use, add to number of ships tally
                if can_go_right and (choice == "right"):
                    for x in range(length_of_ship):
                        computer_grid[column + x][row] = "X "
                        placement_complete = True
                    end_row = row
                    end_column = column + (length_of_ship - 1)
                    computer_ship_location.append([column, end_column, row, end_row])
                    number_of_computer_ships += 1

                if can_go_left and (choice == "left"):
                    for x in range(length_of_ship):
                        computer_grid[column - x][row] = "X "
                        placement_complete = True
                    end_row = row
                    end_column = column - (length_of_ship - 1)
                    # if moving left record end_colum (smaller value) first, needed for checking later
                    computer_ship_location.append([end_column, column, row, end_row])
                    number_of_computer_ships += 1

                if can_go_up and (choice == "up"):
                    for x in range(length_of_ship):
                        computer_grid[column][row - x] = "X "
                        placement_complete = True
                    end_row = row - (length_of_ship - 1)
                    end_column = column
                    # if moving up record end_row (smaller value) first, needed for checking later
                    computer_ship_location.append([column, end_column, end_row, row])
                    number_of_computer_ships += 1

                if can_go_down and (choice == "down"):
                    for x in range(length_of_ship):
                        computer_grid[column][row + x] = "X "
                        placement_complete = True
                    end_row = row + (length_of_ship - 1)
                    end_column = column
                    computer_ship_location.append([column, end_column, row, end_row])
                    number_of_computer_ships += 1

            # show computer ship placement, can remove in final version
            # print_computer_grid()

# Player shoots at the computer
def shoot():
    global number_of_computer_ships_sunk

    shot_complete = False

    while shot_complete is False:

        try:
            start_location_input = input("choose position to shoot at: ").strip().upper()
            if start_location_input[0].isalpha() and len(start_location_input) == 2:

                row = alphabet.find(start_location_input[0])
                column = int(start_location_input[1])

                # if shot hits a ship
                if computer_grid[column][row] == "X ":
                    print("hit!")
                    computer_grid[column][row] = "# "
                    visible_computer_grid[column][row] = "# "
                    # check if the shot sunk a ship
                    if check_computer_ship_sunk(column, row):
                        number_of_computer_ships_sunk += 1
                    shot_complete = True

                # return to top if location already hit a boat
                elif computer_grid[column][row] == "# ":
                    pass

                # return to top if location already hit the water
                elif computer_grid[column][row] == "O ":
                    pass

                # if shot misses a ship
                else:
                    print("Miss!")
                    computer_grid[column][row] = "O "
                    visible_computer_grid[column][row] = "O "
                    shot_complete = True

            # restart process if coordinates typed in incorrectly
            else:
                pass

        # reset process if errors are encountered
        except (ValueError, IndexError):
            continue


#variables for computer shooting AI
computer_first_hit_location = []
computer_second_hit_location = []
hunting_mode = False
second_stage_hunt = False

# computer shoots at the player
def computer_shoot():

    global computer_first_hit_location
    global computer_second_hit_location
    global hunting_mode
    global second_stage_hunt
    global number_of_ships_sunk

    shot_complete = False
    hunting_runs = 0

    while shot_complete is False:

        # if ship hit, enter hunting mode
        if hunting_mode is True:

            # if ship hit twice enter second stage hunt
            if second_stage_hunt is True:

                first_hit_column = computer_first_hit_location[0][0]
                first_hit_row = computer_first_hit_location[0][1]

                if computer_first_hit_location[0][1] == computer_second_hit_location[0][1]:
                    # row is the same
                    # loop through choices until we get an answer
                    coordinate_change_list = [+1, -1, +2, -2, +3, -3, +4, -4, +5]
                    for x in range(len(coordinate_change_list)):

                        if coordinate_change_list[x] == +5:
                            hunting_mode = False
                            second_stage_hunt = False
                            computer_first_hit_location = []
                            computer_second_hit_location = []
                            break

                        elif ((first_hit_column + coordinate_change_list[x] >= 0) and
                                (first_hit_column + coordinate_change_list[x] <= 9)):
                            print(first_hit_column, first_hit_row)

                            if grid[first_hit_column + coordinate_change_list[x]][first_hit_row] == "X ":
                                print("Computer hits your ship!")
                                grid[first_hit_column + coordinate_change_list[x]][first_hit_row] = "# "
                                if check_ship_sunk(first_hit_column + coordinate_change_list[x], first_hit_row):
                                    number_of_ships_sunk += 1
                                    hunting_mode = False
                                    second_stage_hunt = False
                                    computer_first_hit_location = []
                                    computer_second_hit_location = []
                                shot_complete = True
                                break
                            if grid[first_hit_column + coordinate_change_list[x]][first_hit_row] == ". ":
                                print("computer misses!")
                                grid[first_hit_column + coordinate_change_list[x]][first_hit_row] = "O "
                                shot_complete = True
                                break
                            if grid[first_hit_column + coordinate_change_list[x]][first_hit_row] == "# ":
                                pass
                            if grid[first_hit_column + coordinate_change_list[x]][first_hit_row] == "O ":
                                pass
                            else:
                                pass

                elif computer_first_hit_location[0][0] == computer_second_hit_location[0][0]:
                    # column is the same
                    # loop through choices until we get an answer
                    coordinate_change_list = [+1, -1, +2, -2, +3, -3, +4, -4, +5]
                    for x in range(len(coordinate_change_list)):

                        if coordinate_change_list[x] == +5:
                            hunting_mode = False
                            second_stage_hunt = False
                            computer_first_hit_location = []
                            computer_second_hit_location = []
                            break

                        elif ((first_hit_row + coordinate_change_list[x] >= 0) and
                                (first_hit_row + coordinate_change_list[x] <= 9)):

                            if grid[first_hit_column][first_hit_row + coordinate_change_list[x]] == "X ":
                                print("Computer hits your ship!")
                                grid[first_hit_column][first_hit_row + coordinate_change_list[x]] = "# "
                                if check_ship_sunk(first_hit_column, first_hit_row + coordinate_change_list[x]):
                                    number_of_ships_sunk += 1
                                    hunting_mode = False
                                    second_stage_hunt = False
                                    computer_first_hit_location = []
                                    computer_second_hit_location = []
                                shot_complete = True
                                break
                            if grid[first_hit_column][first_hit_row + coordinate_change_list[x]] == ". ":
                                print("computer misses!")
                                grid[first_hit_column][first_hit_row + coordinate_change_list[x]] = "O "
                                shot_complete = True
                                break
                            if grid[first_hit_column][first_hit_row + coordinate_change_list[x]] == "# ":
                                pass
                            if grid[first_hit_column][first_hit_row + coordinate_change_list[x]] == "O ":
                                pass
                            else:
                                pass


            else:
                hunting_runs += 1

                if hunting_runs > 15:
                    hunting_mode = False
                    hunting_runs = 0

                else:
                    first_hit_column = computer_first_hit_location[0][0]
                    first_hit_row = computer_first_hit_location[0][1]

                    next_shot_options = ["right", "left", "up", "down"]
                    randomnum = random.randint(0, len(next_shot_options) - 1)
                    choice = next_shot_options[randomnum]

                    if (choice == "right") and (first_hit_column + 1 <= 9):
                        if grid[first_hit_column + 1][first_hit_row] == "X ":
                            print("Computer hits your ship!")
                            # save this to the second hit location
                            computer_second_hit_location.append([first_hit_column + 1, first_hit_row])
                            grid[first_hit_column + 1][first_hit_row] = "# "
                            second_stage_hunt = True
                            if check_ship_sunk(first_hit_column + 1, first_hit_row):
                                number_of_ships_sunk += 1
                                hunting_mode = False
                                second_stage_hunt = False
                                computer_first_hit_location = []
                                computer_second_hit_location = []
                            shot_complete = True
                        if grid[first_hit_column + 1][first_hit_row] == ". ":
                            print("computer misses!")
                            grid[first_hit_column + 1][first_hit_row] = "O "
                            shot_complete = True
                        if grid[first_hit_column + 1][first_hit_row] == "# ":
                            pass # you already hit him there
                        if grid[first_hit_column + 1][first_hit_row] == "O ":
                            pass # you already missed and hit water there

                    elif (choice == "left") and (first_hit_column - 1 >= 0):
                        if grid[first_hit_column - 1][first_hit_row] == "X ":
                            print("Computer hits your ship!")
                            # save this to the second hit location
                            computer_second_hit_location.append([first_hit_column - 1, first_hit_row])
                            grid[first_hit_column - 1][first_hit_row] = "# "
                            second_stage_hunt = True
                            if check_ship_sunk(first_hit_column - 1, first_hit_row):
                                number_of_ships_sunk += 1
                                hunting_mode = False
                                second_stage_hunt = False
                                computer_first_hit_location = []
                                computer_second_hit_location = []
                            shot_complete = True
                        if grid[first_hit_column - 1][first_hit_row] == ". ":
                            print("computer misses!")
                            grid[first_hit_column - 1][first_hit_row] = "O "
                            shot_complete = True
                        if grid[first_hit_column - 1][first_hit_row] == "# ":
                            pass  # you already hit him there
                        if grid[first_hit_column - 1][first_hit_row] == "O ":
                            pass  # you already missed and hit water there

                    elif (choice == "up") and (first_hit_row - 1 >= 0):
                        if grid[first_hit_column][first_hit_row - 1] == "X ":
                            print("Computer hits your ship!")
                            # save this to the second hit location
                            computer_second_hit_location.append([first_hit_column, first_hit_row - 1])
                            grid[first_hit_column][first_hit_row- 1] = "# "
                            second_stage_hunt = True
                            if check_ship_sunk(first_hit_column, first_hit_row - 1):
                                number_of_ships_sunk += 1
                                hunting_mode = False
                                second_stage_hunt = False
                                computer_first_hit_location = []
                                computer_second_hit_location = []
                            shot_complete = True
                        if grid[first_hit_column][first_hit_row - 1] == ". ":
                            print("computer misses!")
                            grid[first_hit_column][first_hit_row - 1] = "O "
                            shot_complete = True
                        if grid[first_hit_column][first_hit_row - 1] == "# ":
                            pass  # you already hit him there
                        if grid[first_hit_column][first_hit_row - 1] == "O ":
                            pass  # you already missed and hit water there

                    elif (choice == "down") and (first_hit_row + 1 <= 9):
                        if grid[first_hit_column][first_hit_row + 1] == "X ":
                            print("Computer hits your ship!")
                            # save this to the second hit location
                            computer_second_hit_location.append([first_hit_column, first_hit_row + 1])
                            grid[first_hit_column][first_hit_row + 1] = "# "
                            second_stage_hunt = True
                            if check_ship_sunk(first_hit_column, first_hit_row + 1):
                                number_of_ships_sunk += 1
                                hunting_mode = False
                                second_stage_hunt = False
                                computer_first_hit_location = []
                                computer_second_hit_location = []
                            shot_complete = True
                        if grid[first_hit_column][first_hit_row + 1] == ". ":
                            print("computer misses!")
                            grid[first_hit_column][first_hit_row + 1] = "O "
                            shot_complete = True
                        if grid[first_hit_column][first_hit_row + 1] == "# ":
                            pass  # you already hit him there
                        if grid[first_hit_column][first_hit_row + 1] == "O ":
                            pass  # you already missed and hit water there

        else:
            # randomly select shot location
            num_a = random.randint(0, 9)
            num_b = random.randint(0, 9)

            column = num_b
            row = num_a

            # if shot hits a ship
            if grid[column][row] == "X ":
                print("Computer hits your ship!")
                grid[column][row] = "# "
                # check if the shot sunk a ship
                if check_ship_sunk(column, row):
                    number_of_ships_sunk += 1
                    hunting_mode = False
                    second_stage_hunt = False
                    computer_first_hit_location = []
                    computer_second_hit_location = []
                else:
                    computer_first_hit_location.append([column, row])
                    hunting_mode = True

                shot_complete = True

            # repeat process if location already hit a boat
            elif grid[column][row] == "# ":
                pass

            # repeat process if location already hit the water
            elif grid[column][row] == "O ":
                pass

            # if shot misses a ship
            else:
                print("computer misses!")
                grid[column][row] = "O "
                print()
                shot_complete = True


# check if a player ship has been sunk
def check_ship_sunk(col, row):

    # check ship locations
    for location in player_ship_location:
        start_col = location[0]
        end_col = location[1]
        start_row = location[2]
        end_row = location[3]

        # find which ship was hit by the shot
        if start_col <= col <= end_col and start_row <= row <= end_row:

            # if X is found and ship not sunk, return False
            for c in range(start_col, end_col + 1):
                for r in range(start_row, end_row + 1):
                    if grid[c][r] == "X ":
                        return False

    # if no X is found return true - ship is sunk
    return True

# check if computer ship has been sunk
def check_computer_ship_sunk(col, row):

    # check ship locations
    for location in computer_ship_location:
        start_col = location[0]
        end_col = location[1]
        start_row = location[2]
        end_row = location[3]

        # find which ship was hit by the shot
        if start_col <= col <= end_col and start_row <= row <= end_row:

            # if X is found and ship not sunk, return False
            for c in range(start_col, end_col + 1):
                for r in range(start_row, end_row + 1):
                    if computer_grid[c][r] == "X ":
                        return False

    # if no X is found return true - ship is sunk
    return True

# check if someone has won
def check_win():

    global gamerunning
    global player_ship_location
    global computer_ship_location
    global number_of_ships
    global number_of_computer_ships
    global number_of_ships_sunk
    global number_of_computer_ships_sunk
    global computer_first_hit_location
    global computer_second_hit_location
    global hunting_mode
    global second_stage_hunt

    if number_of_computer_ships_sunk >= number_of_computer_ships:
        print("player wins!")
        gamerunning = False
        while gamerunning is False:
            play_again = input("Play again? (y/n)")
            if play_again == "y":

                gamerunning = True

                # reset starting values
                player_ship_location = []
                computer_ship_location = []

                number_of_ships = 0
                number_of_computer_ships = 0

                number_of_ships_sunk = 0
                number_of_computer_ships_sunk = 0

                computer_first_hit_location = []
                computer_second_hit_location = []
                hunting_mode = False
                second_stage_hunt = False

                set_up_game()

            else:
                pass

    elif number_of_ships_sunk >= number_of_ships:
        print("computer wins!")
        gamerunning = False
        while gamerunning is False:
            play_again = input("Play again? (y/n)")
            if play_again == "y":

                gamerunning = True

                # reset starting values
                player_ship_location = []
                computer_ship_location = []

                number_of_ships = 0
                number_of_computer_ships = 0

                number_of_ships_sunk = 0
                number_of_computer_ships_sunk = 0

                computer_first_hit_location = []
                computer_second_hit_location = []
                hunting_mode = False
                second_stage_hunt = False

                set_up_game()

            else:
                pass

# randomly choose a player to go first
current_player = None

def choose_first_player():
    global current_player

    x = random.randint(0, 1)

    if x == 1:
        current_player = "player"
    else:
        current_player = "computer"

# change player
def change_player():
    global current_player

    if current_player == "player":
        current_player = "computer"
    else:
        current_player = "player"



# set up game by placing ships on the board
def set_up_game():
    global gamerunning
    print(" ### Welcome to Battleships ### ")
    time.sleep(1)
    print("Choose the location of your ships: ")
    create_grid()
    create_computer_grid()
    create_visible_computer_grid()
    print_grid()

    check_and_decide_ship_location(2)
    # check_and_decide_ship_location(3)
    # check_and_decide_ship_location(4)

    computer_check_and_decide_ship_location(2)
    # computer_check_and_decide_ship_location(2)
    # computer_check_and_decide_ship_location(3)

    choose_first_player()
    print_grid()
    print__visible_computer_grid()
    gamerunning = True

# starting function call
set_up_game()

# game loop
while gamerunning:
    print("player ships: " + str(number_of_ships) + "  player ships sunk: " + str(number_of_ships_sunk))
    print("computer ships: " + str(number_of_computer_ships) + "  computer ships sunk: " + str(number_of_computer_ships_sunk))

    if current_player == "player":
        print("Player turn")
        time.sleep(1)
        shoot()
    if current_player == "computer":
        print("Computer turn")
        time.sleep(1)
        computer_shoot()
    time.sleep(2)
    print_grid()
    print__visible_computer_grid()
    print("Key: X=Ship #=Hit O=Miss")
    check_win()
    change_player()
