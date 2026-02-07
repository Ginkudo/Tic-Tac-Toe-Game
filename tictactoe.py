from tkinter import *
import random

def next_turn():
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

window = Tk() #window is the main application window
window.title("Tic Tac Toe") #title of the game
players = ["X", "O"] #players in the game
player = random.choice(players) #randomly select a player to start the game
buttons = [[0, 0, 0], #buttons is a 3x3 list that will hold the button objects for the tic tac toe grid
           [0, 0, 0],
           [0, 0, 0]]

Label = Label(text= player + " turn", font=('consolas', 40)) #Label is a label widget that will display the current player's turn
Label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game) #reset_button is a button widget that will call the new_game function when clicked to reset the game
reset_button.pack(side="top") #pack the reset button at the top of the window

Frame = Frame(window) #Frame is a frame widget that will hold the tic tac toe grid
Frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(Frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column)) #create a button for each cell in the tic tac toe grid and set its command to call the next_turn function with the row and column as arguments
        buttons[row][column].grid(row=row, column=column) #place the button in the grid using the grid geometry manager
window.mainloop()