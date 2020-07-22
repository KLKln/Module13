import tkinter
from random import randint
import tkinter as tk


class NumberGuesser:
    guessed_List = []

    def __init__(self, guessed_list=[]):
        self.guessed_list = guessed_list

    def add_guess(num):
        guessed_list.append(num)

    def list_guesses(self):
        for n in NumberGuesser.guessed_List:
            return n



m = tkinter.Tk()
m.title('Guessing Game')
label_instruction = tk.Label(m, text="Guess a number between 1 and 10")
label_line1 = tk.Label(m, text="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
label_num_guesses = tk.Label(m, text="Number of guesses: 0")
label_max_guesses = tk.Label(m, text="Max guesses: 3")
label_line2 = tk.Label(m, text="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
label_guesses = tk.Label(m, text="Game feedback")
label_line3 = tk.Label(m, text="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

buttons = []
for index in range(1,  11):
    button = tk.Button(m, text=index, command=lambda index=index: process(index), state=tk.DISABLED)
    buttons.append(button)

button_start_game_list = []
for index in range(0, 1):
    button_start_game = tk.Button(m, text="start", command=lambda: start(index))
    button_start_game_list.append(button_start_game)


label_instruction.grid(row=0, column=0, columnspan=5)
label_line1.grid(row=1, column=0, columnspan=5)
label_num_guesses.grid(row=2, column=0, columnspan=3)
label_max_guesses.grid(row=2, column=3, columnspan=2)
label_line2.grid(row=3, column=0, columnspan=5)
label_guesses.grid(row=4, column=0, columnspan=5)

label_line3.grid(row=9, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col
        buttons[i].grid(row=row+10, column=col)

button_start_game_list[0].grid(row=13, column=0, columnspan=5)

exit_button = tkinter.Button(m, text='Exit', command=m.destroy)
exit_button.grid(row=14, column=0, columnspan=5)

guess = 0
number_of_guesses = 0
random_number = randint(1, 10)
print(random_number)
label_num_guesses = 4
label_guesses = []


def init():
    global buttons, guess, number_of_guesses, random_number, label_num_guesses, label_guesses, guessed_list
    guess = 0
    number_of_guesses = 0
    random_number = randint(1, 10)
    guessed_list = []
    label_num_guesses["text"] = "Number of Guesses: 0"
    label_guesses = "Numbers guessed: " + NumberGuesser.list_guesses()

    for label_guess in label_guesses:
        label_guess.grid_forget()
        label_guesses = []


def process(i):
    global number_of_guesses, buttons, label_guesses, guess
    guess = i
    number_of_guesses += 1
    NumberGuesser.add_guess(num=guess)
    label_num_guesses["text"] = 'Number of guesses: ' + str(number_of_guesses)
    label_guesses = 'Numbers you have guessed: ' + str(guess)

    if guess == random_number:
        lbl = tk.Label(m, text="You Win! You Guessed the number!", fg="green")
        lbl.grid(row=label_num_guesses, column=0, comlumnspan=5)
        label_num_guesses.append(lbl)
        label_num_guesses += 1

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        if guess > random_number:
            lbl = tk.Label(m, text="Number I'm thinking of is lower than your current number")
            lbl.grid(row=label_guesses, column=0, columnspan=5)
            label_num_guesses.append(lbl)
            label_guesses += 1
        else:
            lbl = tk.Label(m, text="Number I'm thinking of is higher than your current number")
            lbl.grid(row=label_guesses, column=0, columnspan=5)
            label_num_guesses.append(lbl)
            label_guesses += 1

    if number_of_guesses == 5:
        if guess != random_number:
            lbl = tk.Label(m, text="You have lost the game!", fg="red")
            lbl.grid(row=label_guesses, column=0, columnspan=5)
            label_num_guesses.append(lbl)
            label_guesses += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def start(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        button_start_game_list[i]["text"] = "Restart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


m.mainloop()
