from tkinter import *

num = 0
num2 = 0
sign = None
count = 0
pas = True

root = Tk()
root.title("Calculator by Shaheer Kashif")
root.iconbitmap("ico/calc.ico")

def buttonclick(inp):
    global count,pas
    if count >= 2 and pas == 0:
        e.delete(0,END)
        pas = 1
    additional = e.get()
    e.delete(0,END)
    e.insert(0,additional+inp)
    
def buttonoperator(op):
    global num,num2,sign,count,pas
    if op == "+" or op == "-" or op == "*" or op == "÷":
        count += 1
        if count >= 2:
            num2 = e.get()
            if sign == "+":
                result = int(num) + int(num2)
            elif sign == "-":
                result = int(num) - int(num2)
            elif sign == "*":
                result = int(num) * int(num2)
            elif sign == "÷":
                result = int(num) / int(num2)
            num = result
            pas = 0
            sign = op
            e.delete(0,END)
            e.insert(0,result)
        else:
            num = e.get()
            sign = op
            e.delete(0,END)
        
    elif op == "=":
        count = 0
        num2 = e.get()
        if sign == "+":
            result = int(num) + int(num2)
        elif sign == "-":
            result = int(num) - int(num2)
        elif sign == "*":
            result = int(num) * int(num2)
        elif sign == "÷":
            result = int(num) / int(num2)
        e.delete(0,END)
        e.insert(0,result)

def buttonclear():
    e.delete(0,END)

e = Entry(root, width=40, borderwidth=10)
e.grid(row=0,column=0,columnspan=4)

# defining buttons
button_1 = Button(root,text = "1",command = lambda: buttonclick('1'),padx = 28,pady = 14)
button_2 = Button(root,text = "2",command = lambda: buttonclick('2'),padx = 28,pady = 14)
button_3 = Button(root,text = "3",command = lambda: buttonclick('3'),padx = 28,pady = 14)

button_4 = Button(root,text = "4",command = lambda: buttonclick('4'),padx = 28,pady = 14)
button_5 = Button(root,text = "5",command = lambda: buttonclick('5'),padx = 28,pady = 14)
button_6 = Button(root,text = "6",command = lambda: buttonclick('6'),padx = 28,pady = 14)

button_7 = Button(root,text = "7",command = lambda: buttonclick('7'),padx = 28,pady = 14)
button_8 = Button(root,text = "8",command = lambda: buttonclick('8'),padx = 28,pady = 14)
button_9 = Button(root,text = "9",command = lambda: buttonclick('9'),padx = 28,pady = 14)

button_0 = Button(root,text = "0",command = lambda: buttonclick('0'),padx = 28,pady = 14)
button_clear = Button(root,text = "C",command = buttonclear,padx = 27,pady = 14)

button_add = Button(root,text = "+",command = lambda: buttonoperator('+'),padx = 27,pady = 14)
button_subtract = Button(root,text = "-",command = lambda: buttonoperator('-'),padx = 29,pady = 14)
button_multiply = Button(root,text = "x",command = lambda: buttonoperator('*'),padx = 28,pady = 14)
button_divide = Button(root,text = "÷",command = lambda: buttonoperator('÷'),padx = 27,pady = 14)
button_equal = Button(root,text = "=",command = lambda: buttonoperator('='),padx = 27,pady = 14)

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