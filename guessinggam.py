import tkinter as tk
import random

window1 = tk.Tk()

window1.title("Number guessing game")

rn = random.randint(1, 20)

def game():
    guess = e.get()
    rn2 = random.randint(1, 5)
    letpass = True
    global rn
    while True:
        try:
            guess = int(guess)
            letpass = True
            break
        except ValueError:
            output['text'] = "Please only enter numbers"
            letpass = False
            break
    if letpass == True:
        if rn == guess:
            output['text'] = "You got it, good job! Press guess to play again"
            rn = random.randint(1, 20)
        elif guess != rn and rn2 == 1:
            if rn <= 10:
                output['text'] = "It is less than or equal to 10"
            else:
                output['text'] = "It is more than 10"
        elif guess != rn and rn2 ==2:
            if rn % 2 == 0:
                output['text'] = "It is an even number."
            elif rn % 2 != 0:
                output['text'] = "It is an odd number."
        elif guess != rn and rn2 == 3:
            if rn % 3 ==0:
                output['text'] = "It is divisible by 3"
            else:
                output['text'] = "It is not divisible by 3"
        elif guess != rn and rn2 == 4:
            if rn < 5:
                output['text'] = "It is less than 5"
            else:
                output['text'] = "It is more than 4"
        elif guess != rn and rn2 == 5:
            if rn % 4 == 0:
                output['text'] = "It is divisible by 4"
            else:
                output['text'] = "It isn't divisible by 4"
    else:
        pass
    
instruc = tk.Label(window1, text="Type in your guess (1-20) and press Guess!")
instruc.grid(column=0, row=0)

instru2 = tk.Label(window1, text="If you guess wrong I will give you a hint!")
instru2.grid(column=0, row=1)

output = tk.Label(window1, text="")
output.grid(column=0, row=2)

e = tk.Entry(window1)
e.grid(column=0, row=3)

b = tk.Button(window1, text="Guess!", command=game)
b.grid(column=1, row=3)

window1.mainloop()
