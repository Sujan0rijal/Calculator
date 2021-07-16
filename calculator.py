from _ast import Lambda
from tkinter import *

root = Tk()

#title of project
root.title("calculator")

e = Entry(root, width= 35,borderwidth=5, fg="Black", bg="yellow")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def press_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def press_clear():
    e.delete(0, END)

def press_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_number)
    e.delete(0, END)

def press_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = float(first_number)
    e.delete(0, END)


def press_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def press_division():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

def press_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + float(second_number))

    if math == "sub":
        e.insert(0, f_num - float(second_number))

    if math == "multiply":
        e.insert(0, f_num * float(second_number))

    if math == "divide":
        e.insert(0, f_num / float(second_number))


button1 = Button(root,text="1" ,padx=40, pady=20, fg="Black", bg="blue", command=lambda :press_click(1))
button1.grid(row=1, column = 0)
button2 = Button(root, text="2",padx= 40, pady= 20, fg="Black", bg="blue", command= lambda :press_click(2))
button2.grid(row=1, column=1)
button3 = Button(root, text="3", padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(3))
button3.grid(row=1, column=2)
button4 = Button(root, text="4", padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(4))
button4.grid(row=2, column=0)
button5 = Button(root, text="5" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(5))
button5.grid(row=2, column=1)
button6 = Button(root, text="6" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(6))
button6.grid(row=2, column=2)
button7 = Button(root, text="7" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(7))
button7.grid(row=3, column=0)
button8 = Button(root, text="8" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(8))
button8.grid(row=3, column=1)
button9 = Button(root, text="9" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(9))
button9.grid(row=3, column=2)
button0 = Button(root, text="0" ,padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click(0))
button0.grid(row=4, column=2)
add = Button(root,text="+", padx=40, pady=20,fg="Black", bg="blue", command= press_add)
add.grid(row=4, column=0)
sub = Button(root, text="--", padx=40, pady=20,fg="Black", bg="blue", command= press_sub)
sub.grid(row=4,column=1)
equal = Button(root, text="=", padx=40, pady=20,fg="Black", bg="blue", command=press_equal)
equal.grid(row=5, column=1)
clear = Button(root, text="CLEAR", padx=79, pady=20,fg="Black", bg="blue", command=press_clear)
clear.grid(row=5, column=2, columnspan=2)
decimal= Button(root, text=".", padx=40, pady=20,fg="Black", bg="blue", command=lambda :press_click("."))
decimal.grid(row=3, column=3)
multiply = Button(root, text="X", padx=40, pady=20, fg="Black", bg="blue", command=press_multiply)
multiply.grid(row=1, column= 3)
divide = Button(root, text="/", padx=40, pady=20,fg="Black", bg="blue", command=press_division)
divide.grid(row=2, column=3)
root.mainloop()