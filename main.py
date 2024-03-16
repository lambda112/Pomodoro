import tkinter

# CONSTANTS
PINK = "#e2929c"
RED = "#e7305b"
GREEN = "9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# UI SETUP
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

label_title = tkinter.Label(text = "Timer", font = (FONT_NAME, 40), fg = "red", bg = YELLOW)
label_title.grid(column=1, row=0)

check = "✓"
label_check = tkinter.Label(text=check, font = (FONT_NAME, 15), bg = YELLOW, fg = RED)
label_check.grid(column=1, row = 3)

start_button = tkinter.Button(text = "Start", font = (FONT_NAME, 10, "bold"))
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text = "Reset", font = (FONT_NAME, 10, "bold"))
reset_button.grid(column=2, row=2)

# Canvas
canvas = tkinter.Canvas(width=256, height=256, bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
tomato = canvas.create_image(128, 118, image = tomato_img)
timer = canvas.create_text(128, 148, text = "00:00", fill = "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)











window.mainloop()