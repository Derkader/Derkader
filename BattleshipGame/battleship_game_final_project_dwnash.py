"""
Created on July 20, 2022

@author: derek nash

Battleship Game Final Project, main script
"""

import tkinter
from tkinter import *
from battleship_class import BattleshipSea


# does some input validation on the GUI's 1 textbox
# sends the coordinates to the BattleshipSea object to evaluate
# gets an integer answer and uses it to update labels on the GUI
def guess_button():
    button_new_game.config(state='active')
    global labels
    global e1
    coordinates_raw = e1.get().strip()
    e1.delete(0, END)
    temp_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    if coordinates_raw == '':
        message_label.config(text='You did not type anything')
    else:
        try:
            coordinates_raw = coordinates_raw[0:3].upper()
            coord_row = temp_dict[coordinates_raw[0]]
            coord_col = int(coordinates_raw[1:]) - 1
            output_of_2_thru_7 = my_BattleshipSea.evaluate_guess(coord_row, coord_col)
            message_half_string = ''
            if output_of_2_thru_7 == 2:
                labels[coord_row * 10 + coord_col].config(text='O')
                message_half_string = 'hit only water'
            elif output_of_2_thru_7 == 3:
                labels[coord_row * 10 + coord_col].config(text='X')
                message_half_string = 'hit a boat!'
            elif output_of_2_thru_7 == 4:
                labels[coord_row * 10 + coord_col].config(text='X')
                message_half_string = 'hit & sunk boat!'
            elif output_of_2_thru_7 == 5:
                message_half_string = 'was a wasted guess'
            elif output_of_2_thru_7 == 6:
                labels[coord_row * 10 + coord_col].config(text='X')
                message_half_string = 'was the winning shot! Game over, you win!!!'
                fire_button.config(state='disabled')
            elif output_of_2_thru_7 == 7:
                message_half_string = 'was your last guess and now you lose.'
                fire_button.config(state='disabled')
            else:
                message_half_string = 'error message that I should never see'
            message_label.config(text=coordinates_raw + ' ' + message_half_string)
            guesses_label.config(text='Guesses left: ' + str(my_BattleshipSea.return_guesses_left()))
        except:
            message_label.config(text='user typed something weird')
    # 0 if nothing
    # 1 if boat
    # 2 if nothing and was hit
    # 3 if boat and hit
    # 4 if boat and sunk
    # not on sea grid, but 5='you already hit that' and 6='You won, game over' and 7='out of guesses, you lose'


# resets the labels on the GUI and the Guesses
# clears the Battleship Sea grid and sets new boats
# prints a cheat sheet of the grid
def new_game():
    button_new_game.config(state='disabled')
    fire_button.config(state='active')
    global my_BattleshipSea
    my_BattleshipSea.new_game()
    print('Cheat sheet for this particular game, to help with grading')
    print()
    my_BattleshipSea.print_the_sea_grid()

    global labels
    for label1 in labels:
        label1.config(text=' ')


if __name__ == "__main__":

    guesses = 50
    my_BattleshipSea = BattleshipSea(guesses)
    m = tkinter.Tk()
    m.title('Battleship! Play until you win!')

    button_new_game = tkinter.Button(m, text='Start new game', width=30, state='active', command=new_game)
    button_new_game.grid(row=1, columnspan=15, sticky='ew')
    message_label = tkinter.Label(m, text='message board for new messages')
    message_label.grid(row=2, columnspan=12, sticky='ew')

    num_string = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for num in range(4, 14):
        Label(m, text=num_string[num - 4]).grid(row=num, column=1)
    for num2 in range(1, 11):
        Label(m, text=str(num2)).grid(row=3, column=num2 + 1)

    labels = []
    for row in range(4, 14):
        for col in range(2, 12):
            label = Label(m, text=' ')
            label.grid(row=row, column=col)
            labels.append(label)

    guesses_label = Label(m, text="Guesses left: " + str(my_BattleshipSea.return_guesses_left()))
    guesses_label.grid(row=8, column=12)
    Label(m, text="Enter coordinates here").grid(row=10, column=12)
    e1 = Entry(m)
    e1.grid(row=11, column=12)
    fire_button = tkinter.Button(m, text='fire', width=16, state='disabled', command=guess_button)
    fire_button.grid(row=12, column=12, sticky='ew')
    exit_button = tkinter.Button(m, text='exit', width=15, command=m.destroy)
    exit_button.grid(row=16, columnspan=15, sticky='ew')
    m.mainloop()
