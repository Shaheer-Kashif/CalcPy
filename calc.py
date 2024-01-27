from tkinter import *

root = Tk()
root.title("Calculator by Shaheer Kashif")

def buttonclick(inp):
    pass

e = Entry(root, width=40, borderwidth=10)
e.grid(row=0,column=0,columnspan=4)

# defining buttons
button_1 = Button(root,text = "1",command = lambda: buttonclick(),padx = 28,pady = 14)
button_2 = Button(root,text = "2",command = lambda: buttonclick(),padx = 28,pady = 14)
button_3 = Button(root,text = "3",command = lambda: buttonclick(),padx = 28,pady = 14)

button_4 = Button(root,text = "4",command = lambda: buttonclick(),padx = 28,pady = 14)
button_5 = Button(root,text = "5",command = lambda: buttonclick(),padx = 28,pady = 14)
button_6 = Button(root,text = "6",command = lambda: buttonclick(),padx = 28,pady = 14)

button_7 = Button(root,text = "7",command = lambda: buttonclick(),padx = 28,pady = 14)
button_8 = Button(root,text = "8",command = lambda: buttonclick(),padx = 28,pady = 14)
button_9 = Button(root,text = "9",command = lambda: buttonclick(),padx = 28,pady = 14)

button_0 = Button(root,text = "0",command = lambda: buttonclick(),padx = 28,pady = 14)
button_clear = Button(root,text = "C",command = lambda: buttonclick(),padx = 28,pady = 14)

button_add = Button(root,text = "+",command = lambda: buttonclick(),padx = 28,pady = 14)
button_subtract = Button(root,text = "-",command = lambda: buttonclick(),padx = 28,pady = 14)
button_multiply = Button(root,text = "x",command = lambda: buttonclick(),padx = 28,pady = 14)
button_divide = Button(root,text = "÷",command = lambda: buttonclick(),padx = 28,pady = 14)
button_equal = Button(root,text = "=",command = lambda: buttonclick(),padx = 28,pady = 14)

# placing buttons
button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)

button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)

button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)

button_0.grid(row = 4,column = 0)
button_clear.grid(row = 4,column = 1)
button_equal.grid(row = 4,column = 2)

button_add.grid(row = 1,column = 3)
button_subtract.grid(row = 2,column = 3)
button_multiply.grid(row = 3,column = 3)
button_divide.grid(row = 4,column = 3)


root.mainloop()