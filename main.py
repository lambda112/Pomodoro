import tkinter
import math

# CONSTANTS
PINK = "#e2929c"
RED = "#e7305b"
GREEN = "9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# FUNCTIONS
def start_timer():
    global reps
    reps += 1
    print(reps)
    mark = "✓" * (reps // 2)

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        label_check.config(text = mark)
        label_title.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_check.config(text = mark)
        label_title.config(text = "Break", fg=PINK)
    else:
        count_down(WORK_MIN* 60)
        label_title.config(text = "Work", fg="green")

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00") 
    label_title.config(text = "Timer", fg="red")
    label_check["text"] = ""
    global reps
    reps = 0
    
# UI SETUP
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

label_title = tkinter.Label(text = "Timer", font = (FONT_NAME, 40), fg = "red", bg = YELLOW)
label_title.grid(column=1, row=0)

label_check = tkinter.Label(font = (FONT_NAME, 15), bg = YELLOW, fg = RED)
label_check.grid(column=1, row = 3)

start_button = tkinter.Button(text = "Start", font = (FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text = "Reset", font = (FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

# Canvas
canvas = tkinter.Canvas(width=256, height=256, bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
tomato = canvas.create_image(128, 118, image = tomato_img)
timer_text = canvas.create_text(128, 148, text = "00:00", fill = "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

# Countdown 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()







window.mainloop()