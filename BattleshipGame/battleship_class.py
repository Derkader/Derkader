"""
Created on July 20, 2022

@author: derek nash

Battleship Sea and Battleship Boat Classes
"""
import random


class BattleshipSea:
    """BattleshipSea class"""

    def __init__(self, guesses):
        self.initial_guesses = guesses
        self.guesses = guesses
        self.grid_the_sea = [[0 for i in range(10)] for j in range(10)]
        self.boats = [BattleshipBoat(5, 'Carrier'), BattleshipBoat(4, 'Battleship'), BattleshipBoat(3, 'Destroyer'),
                      BattleshipBoat(3, 'Sub'), BattleshipBoat(2, 'Patrol')]

    def new_game(self):
        self.grid_the_sea = [[0 for i in range(10)] for j in range(10)]
        self.guesses = self.initial_guesses
        for boat in self.boats:
            boat.new_game()
        self.set_boats()

    # for each boat...
    # place boat head and get random direction
    # check if position and random direction (horizontal or vertical) will work
    # if not, try next direction (direction+1%2)
    # try both directions, and if one works then break/continue
    # else get new random coords for nose of boat
    # FINALLY, after finding arrangement that fits = True, set boat coords, update sea, then next boat
    def set_boats(self):
        for boat in self.boats:
            random_row = random.randint(0, 9)
            random_col = random.randint(0, 9)
            directions = ['vertical', 'horizontal']
            direction = random.randint(0, 1)
            random_dir = directions[direction]
            current_boat_placement_bool = self.does_this_boat_fit(boat.size, random_row, random_col, random_dir)
            while not current_boat_placement_bool:
                # print('we will try different position')
                for j in range(0, 2):
                    direction = (direction + 1) % 2
                    random_dir = directions[direction]
                    current_boat_placement_bool = self.does_this_boat_fit(boat.size, random_row, random_col, random_dir)
                    if current_boat_placement_bool:
                        continue
                random_row = random.randint(0, 9)
                random_col = random.randint(0, 9)
                current_boat_placement_bool = self.does_this_boat_fit(boat.size, random_row, random_col, random_dir)
                # print('needed new coordinates')
            self.set_boat_coords(boat, random_row, random_col, random_dir)

    # set this boat's coordinates, given the nose coordinates and direction
    # also update the sea grid with these coordinates
    def set_boat_coords(self, boat, nose_row, nose_col, direction):
        boat_size = boat.get_size()
        if direction == 'vertical':
            tail_row = nose_row + boat_size - 1
            tail_col = nose_col
        else:
            tail_row = nose_row
            tail_col = nose_col + boat_size - 1

        all_coords_for_this_boat = [(nose_row, nose_col)]
        if nose_row == tail_row:
            for i in range(nose_col + 1, tail_col + 1):
                all_coords_for_this_boat.append((nose_row, i))
        else:
            for i in range(nose_row + 1, tail_row + 1):
                all_coords_for_this_boat.append((i, nose_col))
        for row, col in all_coords_for_this_boat:
            self.grid_the_sea[row][col] = 1
        boat.set_coords(all_coords_for_this_boat)

    # True/False
    # does this boat fit on the sea grid with these nose coordinates and direction?
    # and does it overlap any other boats?
    def does_this_boat_fit(self, boat_size, nose_row, nose_col, direction):
        if nose_row > 9 or nose_col > 9 or self.grid_the_sea[nose_row][nose_col] == 1:
            return False

        if direction == 'vertical':
            tail_row = nose_row + boat_size - 1
            tail_col = nose_col
        else:
            tail_row = nose_row
            tail_col = nose_col + boat_size - 1

        if (0 <= tail_row <= 9) and (0 <= tail_col <= 9):
            # first collect all the coordinates for the boat
            all_coords_for_this_boat = [(nose_row, nose_col)]
            if nose_row == tail_row:
                for i in range(nose_col + 1, tail_col + 1):
                    all_coords_for_this_boat.append((nose_row, i))
            else:
                for i in range(nose_row + 1, tail_row + 1):
                    all_coords_for_this_boat.append((i, nose_col))
            # now check the boat's coordinates for boat overlap (grid == 1)
            for row, col in all_coords_for_this_boat:
                if self.grid_the_sea[row][col] != 0:
                    return False
            return True
        else:
            return False

    # basically it's 1 extra step added to the update_boats_and_grid function.
    # That tells you if you just lost the game (if guesses == 0 and boats still floating)
    def evaluate_guess(self, coord_row, coord_col):
        output_of_2_thru_6 = self.update_boats_and_grid(coord_row, coord_col)
        self.guesses -= 1
        if self.guesses == 0 and output_of_2_thru_6 != 6:
            return 7  # meaning, Game Over, you ran out of guesses
        else:
            return output_of_2_thru_6

    # returns a number based on what you hit
    # also, if you hit a boat, it updates the boat, checks if it's sunk, and updates the grid

    def update_boats_and_grid(self, coord_row, coord_col):  # takes the hit coordinates and updates the boat and grid
        previous_sea_status = self.grid_the_sea[coord_row][coord_col]
        if previous_sea_status == 0:  # if you hit empty water
            self.grid_the_sea[coord_row][coord_col] = 2
            return 2  # put a '2' on the grid
        elif previous_sea_status == 1:  # if you hit a boat
            boat_hit_index = 0
            for i in range(0, len(self.boats)):
                boat = self.boats[i]
                temp_coords = boat.return_coords()

                if (coord_row, coord_col) in temp_coords:
                    boat_hit_index = i
            self.boats[boat_hit_index].hit(coord_row, coord_col)
            if self.boats[boat_hit_index].is_it_sunk():
                sea_coords_to_update = self.boats[boat_hit_index].return_coords()
                for row, col in sea_coords_to_update:
                    self.grid_the_sea[row][col] = 4
                # with boat sunk and grid updated, now check if game over
                if self.check_if_all_boats_sunk_yet():
                    return 6  # meaning, Game Over You Win!!! You sunk the last boat
                else:
                    return 4  # meaning hit boat and sunk it
            else:  # boat hit but not sunk
                self.grid_the_sea[coord_row][coord_col] = 3
                return 3  # meaning hit boat
        elif (previous_sea_status == 2) or (previous_sea_status == 3) or (previous_sea_status == 4):
            return 5  # meaning, "You already hit that one." It will still cost a guess.

    # ask each boat if still floating
    def check_if_all_boats_sunk_yet(self):
        for boat in self.boats:
            if not boat.is_it_sunk():
                return False
        return True

    def return_the_sea_grid(self):
        return self.grid_the_sea
        # 0 if nothing
        # 1 if boat
        # 2 if nothing and was hit
        # 3 if boat and hit
        # 4 if boat and sunk
        # not on sea grid, but 5='you already hit that' and 6='You won, game over' and 7='out of guesses, you lose'

    def return_guesses_left(self):
        return self.guesses

    def print_the_sea_grid(self):
        row_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        col_label = '1  2  3  4  5  6  7  8  9  10'
        print('   ' + str(col_label))
        for i in range(0, 10):
            print(row_label[i] + ' ' + str(self.grid_the_sea[i]))

    def __str__(self):
        return 'a battleship sea with boats'

    def display(self):
        return 'a battleship sea with boats'


class BattleshipBoat:
    """BattleshipBoat class"""

    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.coords = []
        self.coords_hit = []
        self.is_sunk = False

    def get_size(self):
        return self.size

    def set_coords(self, coords):
        self.coords = coords

    def new_game(self):
        self.coords = []
        self.coords_hit = []
        self.is_sunk = False

    def return_coords(self):
        return self.coords

    def hit(self, row, col):
        if (row, col) in self.coords and (row, col) not in self.coords_hit:
            self.coords_hit.append((row, col))

        if len(self.coords_hit) == self.size:
            self.is_sunk = True

    def is_it_sunk(self):
        return self.is_sunk

    def __str__(self):
        return 'a battleship boat'
