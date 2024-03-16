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

# Canvas
canvas = tkinter.Canvas(width=256, height=256, bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(128, 118, image = tomato_img)
canvas.create_text(128, 148, text = "00:00", fill = "white", font=(FONT_NAME, 30, "bold"))
canvas.pack()



5










window.mainloop()