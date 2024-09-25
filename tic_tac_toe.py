from tkinter import *
import random
import sys

window = Tk()
window.geometry("400x600")
window.title("Tic Tac Toe")

HEIGHT = 2
WIDTH = 5

player = ''
winner = ''
possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn_counter = 1
leaving_loop = False
multi_state = False

player1_score = player2_score = 0



def computer_play():
    global turn_counter, leaving_loop, possible_choices
    if (turn_counter % 2) != 0:
        choice = random.choice(possible_choices)
        possible_choices.remove(choice)
        if choice == 1:
            button1['text'] = 'O'
            button1['state'] = DISABLED
        elif choice == 2:
            button2['text'] = 'O'
            button2['state'] = DISABLED
        elif choice == 2:
            button2['text'] = 'O'
            button2['state'] = DISABLED
        elif choice == 3:
            button3['text'] = 'O'
            button3['state'] = DISABLED
        elif choice == 4:
            button4['text'] = 'O'
            button4['state'] = DISABLED
        elif choice == 5:
            button5['text'] = 'O'
            button5['state'] = DISABLED
        elif choice == 6:
            button6['text'] = 'O'
            button6['state'] = DISABLED
        elif choice == 7:
            button7['text'] = 'O'
            button7['state'] = DISABLED
        elif choice == 8:
            button8['text'] = 'O'
            button8['state'] = DISABLED
        elif choice == 9:
            button9['text'] = 'O'
            button9['state'] = DISABLED

    turn_counter += 1
        

def btn_status(status):
    button1.configure(state=status)
    button2.configure(state=status)
    button3.configure(state=status)
    button4.configure(state=status)
    button5.configure(state=status)
    button6.configure(state=status)
    button7.configure(state=status)
    button8.configure(state=status)
    button9.configure(state=status)


def btn_click(button):
    global player, turn_counter, possible_choices
    if (turn_counter % 2) != 0:
        player = 'O'
    else:
        player = 'X'

    
    if player == 'O':
        button.configure(text='O')
    else:
        button.configure(text='X')

    if button == button1:
        possible_choices.remove(1)
    elif button == button2:
        possible_choices.remove(2)
    elif button == button3:
        possible_choices.remove(3)
    elif button == button4:
        possible_choices.remove(4)
    elif button == button5:
        possible_choices.remove(5)
    elif button == button6:
        possible_choices.remove(6)
    elif button == button7:
        possible_choices.remove(7)
    elif button == button8:
        possible_choices.remove(8)
    elif button == button9:
        possible_choices.remove(9)

    button.configure(state=DISABLED)

    turn_counter += 1

    if multi_state == True:
        multi_player()
        check_winner()
    else:
        computer_play()
        check_winner()


def multi_player():
    global multi_state
    multi_state = True
    if (turn_counter % 2) != 0:
        player = 'O'
    else:
        player = 'X'


def game_mode(mode):
    global multi_state
    btn_status(ACTIVE)
    if mode == 'single':
        multi_state = False
        computer_play()
    else:
        multi_state = True
        multi_player()

    single_btn.configure(state=DISABLED)
    multi_btn.configure(state=DISABLED)


def end_game():
    global possible_choices
    btn_status(DISABLED)
    possible_choices = []


def update_score(player):
    global  player1_score, player2_score
    if player == 'Player1':
        player1_score += 1
    elif player == 'Player2':
        player2_score += 1

    score_label.configure(text = f"O: {player1_score} :: {player2_score} :X")


def check_winner():
    global winner
    winner = ''
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        winner = 'Player2'
        button1['bg'] = 'red'
        button2['bg'] = 'red'
        button3['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
        winner = 'Player2'
        button4['bg'] = 'red'
        button5['bg'] = 'red'
        button6['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
        winner = 'Player2'
        button7['bg'] = 'red'
        button8['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
        winner = 'Player2'
        button1['bg'] = 'red'
        button4['bg'] = 'red'
        button7['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
        winner = 'Player2'
        button2['bg'] = 'red'
        button5['bg'] = 'red'
        button8['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
        winner = 'Player2'
        button3['bg'] = 'red'
        button6['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
        winner = 'Player2'
        button1['bg'] = 'red'
        button5['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        winner = 'Player2'
        button3['bg'] = 'red'
        button5['bg'] = 'red'
        button7['bg'] = 'red'
        update_score(winner)
        end_game()
    
    # Second Player
    elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
        winner = 'Player1'
        button1['bg'] = 'red'
        button2['bg'] = 'red'
        button3['bg'] = 'red'
        update_score(winner)
        end_game()
       
    elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
        winner = 'Player1'
        button4['bg'] = 'red'
        button5['bg'] = 'red'
        button6['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':
        winner = 'Player1'
        button7['bg'] = 'red'
        button8['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
        winner = 'Player1'
        button1['bg'] = 'red'
        button4['bg'] = 'red'
        button7['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
        winner = 'Player1'
        button2['bg'] = 'red'
        button5['bg'] = 'red'
        button8['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
        winner = 'Player1'
        button3['bg'] = 'red'
        button6['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
        winner = 'Player1'
        button1['bg'] = 'red'
        button5['bg'] = 'red'
        button9['bg'] = 'red'
        update_score(winner)
        end_game()
    elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
        winner = 'Player1'
        button3['bg'] = 'red'
        button5['bg'] = 'red'
        button7['bg'] = 'red'
        update_score(winner)
        end_game()
    

def restart_game():
    global possible_choices, winner
    possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    winner = ''
    turn_counter = 1
    single_btn['state'] = ACTIVE
    multi_btn['state'] = ACTIVE
    button1['text'] = ''
    button2['text'] = ''
    button3['text'] = ''
    button4['text'] = ''
    button5['text'] = ''
    button6['text'] = ''
    button7['text'] = ''
    button8['text'] = ''
    button9['text'] = ''
    button1['bg'] = 'white'
    button2['bg'] = 'white'
    button3['bg'] = 'white'
    button4['bg'] = 'white'
    button5['bg'] = 'white'
    button6['bg'] = 'white'
    button7['bg'] = 'white'
    button8['bg'] = 'white'
    button9['bg'] = 'white'



label = Label(window, text="Tic Tac Toe", font="Times 40 bold", fg="green")

label.pack()

top_frame = Frame(window, width=100)
top_frame.pack(side=TOP, pady=10)

single_btn = Button(top_frame, text="Single Player", width=10, command=lambda: game_mode('single'))
single_btn.pack(side=LEFT, padx=10)

multi_btn = Button(top_frame, text="Multi Player", width=10, command=lambda: game_mode('multi'))
multi_btn.pack(side=LEFT, padx=10)

frame = Frame(window, height=100, width=100)
frame.pack()

button1 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button1))
button2 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button2))
button3 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button3))
button4 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button4))
button5 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button5))
button6 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button6))
button7 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button7))
button8 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button8))
button9 = Button(frame, text='', font="Times 25 bold", width=WIDTH, height=HEIGHT, command=lambda: btn_click(button9))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

lower_frame = Frame(window, width=10)
lower_frame.pack(pady=10)

restart_btn = Button(lower_frame, text="Restart", width=10, command=restart_game)
restart_btn.pack(side=LEFT, padx=10)

end_btn = Button(lower_frame, text="End", width=10, command=sys.exit)
end_btn.pack(side=RIGHT, padx=10)

score_frame = Frame(window, width=10)
score_frame.pack(pady=10)

score_label = Label(score_frame, text="X : 0 :: 0: O", font="Times 20 bold")
score_label.pack()

btn_status(DISABLED)

window.mainloop()
