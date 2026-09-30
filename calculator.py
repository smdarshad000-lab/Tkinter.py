# !/usr/bin/env python      
import tkinter as tk

# def eval():
#     return text

app = tk.Tk()

app.geometry("420x420")
# app.title("calculator")
# app.config(bg="black")


label = tk.Label(app, text="Calculator",
                 font = ('Arial,40,bold'), 
                 fg="green", bg ="black",
                 relief=tk.SUNKEN,
                 bd=10,
                 padx=20,
                 pady=10)  # parentheses work as a constructor
label.pack()


# def click():
#     print("i clicked the button!")

# button = tk.Button(app,
#                    text="Click",
#                    command=click,)

# button.pack()


# entry = tk.Entry(app,
#                  font=("Arial",50),
#                  show="*")

# # entry.insert(0,"spongebob")
# entry.pack()


# def submit():
#     username = entry.get()
#     print("hello" + username)
#     # entry.config(state="disabled")

# def delete():
#     entry.delete(0, tk.END)


# def backspace():
#     entry.delete(len(entry.get())-1,tk.END)



# submit_button = tk.Button(app,
#                           text="submit",
#                           command=submit)
# submit_button.pack()

# delete_button = tk.Button(app,
#                           text="delete",
#                           command=delete)
# delete_button.pack()

# backspace_button = tk.Button(app,
#                           text="backspace",
#                           command=backspace)
# backspace_button.pack()

# def display():
#     if(x.get() == 1):
#         print("you")
#     else:
#         print("no")

# x = tk.IntVar()

# check_button = tk.Checkbutton(app,
#                            text="heeelllllooo",
#                            variable = x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display)
# check_button.pack()


expression = tk.Entry(app)
expression.pack()

status = tk.Label(app, text="")
status.pack()

equation = tk.Label(app)
equation.pack()

def show(value):
    expression.insert(tk.End,value)
    expression.focus_set()

def clear():
    expression.delete(0,tk.END)

def backspace():
    text = expression.get()
    expression.delete(len(text) -1,tk.End)

def calculate():
    text = expression.get()
    if text == "" or text =="=":
        return
    try:
        result = eval(text)
        expression.delete(0,tk.END)
        expression.insert(0,str(result))
        status.config(text="")
    except Exception:
        expression.delete(0, tk.END)
        status.config(text="Error")
        status.config(text="")

app.bind("<Return>", lambda event: calculate())
app.bind("<KP_Enter>", lambda event: calculate())
expression.bind("<Return>", lambda event: calculate())
expression.bind("<KP_Enter>", lambda event:calculate())

buttons = [["7", "8", "9", "/",],
           ["4", "5", "6", "*",],
           ["1", "2", "3", "-",],
           ["0", ".", "C", "+",],
           ["<", "=", "=", "=",],
           ]

box = tk.Frame(app)
box.pack()

for row in range(5):
    for column in range(4):
        number = buttons[row][column]

        if number == "=":
            button = tk.Button(box,
                               text = "=",
                               command = calculate)
            button.grid(row = row, column = column)
        elif number == "C":
            button = tk.Button(box,
                               text = number,
                               command = clear)
        elif number == "<":
            button = tk.Button(box,
                               text = number,
                               command = backspace)
        else:
            button = tk.Button(box,
                               text = number,
                               command = lambda n = number: show(n))

            button.grid(row = row, column = column)

        box.rowconfigure(row)
        box.columnconfigure(column)
        

app.mainloop()           