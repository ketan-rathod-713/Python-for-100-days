
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer  = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Long Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Short Break")
        count_down(short_break_sec)
    else:
        label.config(text="Work Time")
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    global timer
    print(count)
    # minutes = math.floor(count/60)
    minutes = count // 60
    seconds = count % 60
    if(minutes < 10):
        minutes = f"0{minutes}"
    if(seconds < 10):
        seconds = f"0{seconds}"
    finalString = f"{minutes}:{seconds}"
    # here i want "10:05" in minute and second , so let the count is the second then formate it
    canvas.itemconfig(canvas_text ,text=finalString)
    if(count==0):
        start_timer()
        mark = ""
        for i in range(reps//2):
            mark += "👍"
        check_marks.config(text=mark)
        return
    timer = window.after(1000,count_down, count - 1) # store it in timer as when user clicks reset we want to stop it , so call canncel_after
    # dont call countdown here but rather in window.after so that it can run after 1 ms

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)

label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME,40,"bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2,column=0)

# start_timer()

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=3)

check_marks = Label()
check_marks.grid(column=1, row=3)

# while True:
#     print("dont do this")

window.mainloop() # The main loop shows that it's a event driven in each milli second it sees if something happened or not , and if we put another loop inside our main program then it actually won't be able to reach the mainLoop so nothing will update

# canvas widget = draw something on it
# https://colorhunt.co/

# Python Dynamic Typing
# at first i can do like a = 12
# then i can do a = "string" No error
# We dynamicly change the data type of the variable