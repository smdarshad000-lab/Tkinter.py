# !/usr/bin/env python      
import tkinter as tk

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


entry = tk.Entry(app,
                 font=("Arial",50))
entry.pack()


def submit():
    username = entry.get()
    print("hello" + username)

def delete():
    entry.delete(0, tk.END)


def backspace():
    entry.delete(len(entry.get())-1,tk.END)



submit_button = tk.Button(app,
                          text="submit",
                          command=submit)
submit_button.pack()

delete_button = tk.Button(app,
                          text="delete",
                          command=delete)
delete_button.pack()

backspace_button = tk.Button(app,
                          text="backspace",
                          command=backspace)
backspace_button.pack()


app.mainloop()           