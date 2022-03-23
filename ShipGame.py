# Author: Piseth Chhoeuy
# GitHub ID: PisethC92
# Date: 2/18/2022
# Description: Creating the battleship game that allows two players to place their ships down and fire at one another.
# will return false if invalid ship placement or torpedo shot.

# With the approach i'm taking, a board is not needed but if the requirement asked us to print the board with
# ship placement, below is where I would start.
#
# class board_setup:
#     """Class used to setup the board that will be used in the ShipGame class"""
#
#     def __init__(self, _grid=None):
#         """Constructor for the board setup class. No parameters. Initializes \
#         the required data member. All data members are private"""
#         size = 10  # size of board
#         if _grid is None:  # immutable list
#             self._grid = []
#         for x in range(1, size + 1):  # Creating a nested list for the battleship board
#             grid_inner = []
#             for y in range(1, size + 1):
#                 grid_inner.append(y)
#             self._grid.append(grid_inner)


class ShipGame:
    """ShipGame class that represents the battleship game, played by two players. Player 1 always starts first.
    Allows players to place ship as long as it’s a valid placement (True), otherwise return False. Allows players to
    fire torpedo as long as it's their turn and the game has not finished."""

    def __init__(self, _player_one_grid=None, _player_two_grid=None):
        self._status = 'UNFINISHED'  # default value to unfinished game
        self._which_turn = "first"  # first player starts first
        if _player_one_grid is None:
            self._player_one_grid = []  # immutable list
        if _player_two_grid is None:
            self._player_two_grid = []  # immutable list
        self._convert_letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
                                       'G': 7, 'H': 8, 'I': 9,
                                       'J': 10}  # converting letters to number to help determine coordinates

    def place_ship(self, player, length, coord, orient, _is_valid=None):
        """Takes 4 parameters and allows the players to place ships on the grid"""
        if _is_valid is None:
            self._is_valid = True
        pos_y = self._convert_letter_to_num.get(coord[0])  # slicing string, converting from letter to num and
        # assigning to variable
        num_coord = int(coord[1])  # slicing string and assigning to variable

        # Each person will have a board (i.e. a list). Within the list, stores their ship (another list)
        # and each ship has the coordinates (x,y paired stored in a list). End result should look something like
        # player_one_grid = [[[1,1], [1,2]], [[3,4], [4,4], [5,4]]]
        # above example shows first player with 2 ships, one of size 2 and another of size 3. Each of the ship has
        # coordinates that we can easily check to see if a torpedo has hit or if it overlaps with another ship placement

        if player == 'first':  # check which player to make sure we're adding to correct grid
            if orient == 'C':  # check which axis to increase (x vs y axis)
                temp_pos = pos_y  # placeholder to avoid mutating pos_y
                temp_ship_list = []  # will be used to store coordinates of ship if the move is valid
                if length > 10 or pos_y + length > 11 or length < 2:  # check for bounds and ship sizes
                    return False
                elif pos_y < 1 or num_coord < 1:  # if the starting position is out of bounds
                    return False
                if not self._player_one_grid:  # empty list, add coordinates since it won't overlap
                    for step in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        pos_y += 1
                    self._player_one_grid.append(temp_ship_list)
                    return True
                for step in range(length + 1):  # checking to see if ship  is overlapping with another
                    for ship in self._player_one_grid:
                        if [num_coord, temp_pos] in ship:  # using "in" function to check if coordinate exists
                            self._is_valid = False
                            return self._is_valid
                    temp_pos += 1  # incrementing up to the length of the ship
                if self._is_valid:
                    for elem in range(length):  # adding ship + coordinates to player's board
                        temp_ship_list.append([num_coord, pos_y])
                        pos_y += 1
                    self._player_one_grid.append(temp_ship_list)
                    return True

            if orient == 'R':  # repeat of above but change for horizontal movement
                temp_pos = num_coord  # X-axis will be changing, adjust from pos_y > num_coord
                temp_ship_list = []
                if length > 10 or num_coord + length > 11 or length < 2:
                    return False
                elif pos_y < 1 or num_coord < 1:
                    return False
                if not self._player_one_grid:
                    for step in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        num_coord += 1
                    self._player_one_grid.append(temp_ship_list)
                    return True
                for step in range(length + 1):
                    for ship in self._player_one_grid:
                        if [temp_pos, pos_y] in ship:
                            self._is_valid = False
                            return self._is_valid
                    temp_pos += 1
                if self._is_valid:
                    for elem in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        num_coord += 1
                    self._player_one_grid.append(temp_ship_list)
                    return True

        if player == 'second':  # repeat of above but for player 2
            if orient == 'C':
                temp_pos = pos_y
                temp_ship_list = []
                if length > 10 or pos_y + length > 11 or length < 2:
                    return False
                elif pos_y < 1 or num_coord < 1:
                    return False
                if not self._player_two_grid:
                    for step in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        pos_y += 1
                    self._player_two_grid.append(temp_ship_list)
                    return True
                for step in range(length + 1):
                    for ship in self._player_two_grid:
                        if [num_coord, temp_pos] in ship:
                            self._is_valid = False
                            return self._is_valid
                    temp_pos += 1
                if self._is_valid:
                    for elem in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        pos_y += 1
                    self._player_two_grid.append(temp_ship_list)
                    return True

            if orient == 'R':  # repeat of above but for player 2
                temp_pos = num_coord
                temp_ship_list = []
                if length > 10 or num_coord + length > 11 or length < 2:
                    return False
                elif pos_y < 1 or num_coord < 1:
                    return False
                if not self._player_two_grid:
                    for step in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        num_coord += 1
                    self._player_two_grid.append(temp_ship_list)
                    return True
                for step in range(length + 1):
                    for ship in self._player_two_grid:
                        if [temp_pos, pos_y] in ship:
                            self._is_valid = False
                            return self._is_valid
                    temp_pos += 1
                if self._is_valid:
                    for elem in range(length):
                        temp_ship_list.append([num_coord, pos_y])
                        num_coord += 1
                    self._player_two_grid.append(temp_ship_list)
                    return True

    def get_current_state(self):
        """Returns the state of the game"""
        return self._status

    def fire_torpedo(self, player, coord):
        """Allows the users to fire a torpedo at the opposing player. Turn enforced. If all ship is sunk, set
        status to the winner. Return true if shot is valid and return false if it's not player's turn or the
        game has finished"""
        pos_y = self._convert_letter_to_num.get(coord[0])
        num_coord = int(coord[1])
        shot = [num_coord, pos_y]
        if player != self._which_turn or self._status != 'UNFINISHED':
            return False
        else:
            break_out = False  # used to break out of for loop if shot hits a ship to save on run-time
            if player == 'first':
                for ship in self._player_two_grid:
                    for target in ship:
                        if shot == target:  # find shot in second player's grid
                            ship.remove(shot)
                            break_out = True  # set to true to break out of loop
                            break
                        if break_out:
                            break
                    if break_out:
                        break
                self._player_two_grid = [ship for ship in self._player_two_grid if ship != []]  # remove sunken ship
                if not self._player_two_grid:  # empty list = no more ships
                    self._status = 'FIRST_WON'  # first player wins
                    return True
                else:
                    self._which_turn = "second"  # updating turn
                    return True
            if player == 'second':
                for ship in self._player_one_grid:
                    for target in ship:
                        if shot == target:  # find shot in first player's grid
                            ship.remove(shot)
                            break_out = True  # set to true to break out of loop
                            break
                        if break_out:
                            break
                    if break_out:
                        break
                self._player_one_grid = [ship for ship in self._player_one_grid if ship != []]  # remove sunken ship
                if not self._player_one_grid:  # empty list = no more ships
                    self._status = 'SECOND_WON'  # second player wins
                    return True
                else:
                    self._which_turn = "first"  # updating turn
                    return True

    def get_num_ships_remaining(self, player):
        """Returns how many ships the player has left"""
        # the length of the list should determine how many 'ships' there are left in play
        if player == 'first':
            remaining = len(self._player_one_grid)
            return remaining
        else:
            remaining = len(self._player_two_grid)
            return remaining


# game = ShipGame()
# print(game.place_ship('first', 10, 'A1', 'C'))
# print(game.place_ship('first', 2, 'I8', 'R'))
# print(game.place_ship('second', 3, 'H2', 'C'))
# print(game.place_ship('second', 2, 'A1', 'C'))
# print(game.place_ship('first', 8, 'H2', 'R'))
# print(game.get_current_state())