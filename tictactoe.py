from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]: #if the current player is "X"
            buttons[row][column]['text'] = "X" #set the text of the button to "X"
            if check_winner() is False: #check if there is a winner after the move
                player = players[1] #switch to the other player
                Label.config(text=players[1] + " turn") #update the label to show the current player's turn
            elif check_winner() is True: #if there is a winner
                Label.config(text=players[0] + " wins!") #update the label to show that "X" wins
            elif empty_spaces() is False: #if there are no empty spaces left and no winner, it's a tie
                Label.config(text="It's a tie!") #update the label to show that it's a tie
        else: #if the current player is "O"
            buttons[row][column]['text'] = "O" #set the text of the button to "O"
            if check_winner() is False: #check if there is a winner after the move
                player = players[0] #switch to the other player
                Label.config(text=players[0] + " turn") #update the label to show the current player's turn
            elif check_winner() is True: #if there is a winner
                Label.config(text=players[1] + " wins!") #update the label to show that "O" wins
            elif empty_spaces() is False: #if there are no empty spaces left and no winner, it's a tie
                Label.config(text="It's a tie!") #update the label to show that it's a tie
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