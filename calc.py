from tkinter import *

num = 0
num2 = 0
sign = None
count = 0
pas = True
hist = ""

root = Tk()
root.title("Calculator by Shaheer Kashif")
root.iconbitmap("ico/calc.ico")

def ignore_keyboard_input(event):
    return "break"

def buttonclick(inp):
    global count,pas,sign,hist
    hist += inp
    if count >= 2 and pas == 0:
        e.delete(0,END)
        pas = 1
    if sign == "=":
        history_label.delete(0,END)
        e.delete(0,END)
    additional = e.get()
    e.delete(0,END)
    e.insert(0,additional+inp)
    
def buttonoperator(op):
    global hist
    hist += op
    history_label = Entry(root,width=50,justify="right")
    history_label.insert(0,hist)
    history_label.grid(row = 0,column=0,columnspan=5)
    if e.get() == "":
        pass
    else:
        global num,num2,sign,count,pas
        if op == "+" or op == "-" or op == "x" or op == "÷":
            count += 1
            if count >= 2:
                num2 = e.get()
                if sign == "+":
                    result = float(num) + float(num2)
                elif sign == "-":
                    result = float(num) - float(num2)
                elif sign == "x":
                    result = float(num) * float(num2)
                elif sign == "÷":
                    result = float(num) / float(num2)
                num = result
                pas = 0
                sign = op
                e.delete(0,END)
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result,8)
                e.insert(0,result)
            else:
                num = e.get()
                sign = op
                e.delete(0,END)
        elif op == "=":
            count = 0
            num2 = e.get()
            if sign == "+":
                result = float(num) + float(num2)
            elif sign == "-":
                result = float(num) - float(num2)
            elif sign == "x":
                result = float(num) * float(num2)
            elif sign == "÷":
                result = float(num) / float(num2)
            sign = op
            e.delete(0,END)
            if result == int(result):
                result = int(result)
            else:
                result = round(result,8)
            e.insert(0,result)

def buttonclear():
    e.delete(0,END)
    
def backspace():
    temp = e.get()
    e.delete(0,END)
    temp = temp.replace(temp[len(temp)-1],"",1)
    e.insert(0,temp)

history_label = Entry(root,width=50,justify="right")
history_label.grid(row = 0,column=0,columnspan=5)
e = Entry(root, width=25,state="normal",font=("Helvetica",20),justify="right")
e.grid(row=1,column=0,columnspan=5)

# defining buttons
button_1 = Button(root,text = "1",command = lambda: buttonclick('1'),padx = 26,pady = 14,font= "helvetica",bg="white")
button_2 = Button(root,text = "2",command = lambda: buttonclick('2'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_3 = Button(root,text = "3",command = lambda: buttonclick('3'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_4 = Button(root,text = "4",command = lambda: buttonclick('4'),padx = 26,pady = 14,font= "helvetica",bg="white")
button_5 = Button(root,text = "5",command = lambda: buttonclick('5'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_6 = Button(root,text = "6",command = lambda: buttonclick('6'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_7 = Button(root,text = "7",command = lambda: buttonclick('7'),padx = 26,pady = 14,font= "helvetica",bg="white")
button_8 = Button(root,text = "8",command = lambda: buttonclick('8'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_9 = Button(root,text = "9",command = lambda: buttonclick('9'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_0 = Button(root,text = "0",command = lambda: buttonclick('0'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_decimal = Button(root,text = ".",command = lambda: buttonclick('.'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_clear = Button(root,text = "C",command = buttonclear,padx = 34,pady = 14,font= "helvetica")
button_backspace = Button(root, text = "⌫",command = backspace,padx = 30,pady = 14,font= "helvetica")

button_add = Button(root,text = "+",command = lambda: buttonoperator('+'),padx = 26,pady = 14,font= "helvetica")
button_subtract = Button(root,text = "-",command = lambda: buttonoperator('-'),padx = 28,pady = 14,font= "helvetica")
button_multiply = Button(root,text = "x",command = lambda: buttonoperator('x'),padx = 27,pady = 14,font= "helvetica")
button_divide = Button(root,text = "÷",command = lambda: buttonoperator('÷'),padx = 26,pady = 14,font= "helvetica")
button_equal = Button(root,text = "=",command = lambda: buttonoperator('='),padx = 28,pady = 14,font= "helvetica",bg="#176cb5",fg="white")

# placing buttons
button_1.grid(row = 4,column = 0)
button_2.grid(row = 4,column = 1)
button_3.grid(row = 4,column = 2)

button_4.grid(row = 3,column = 0)
button_5.grid(row = 3,column = 1)
button_6.grid(row = 3,column = 2)

button_7.grid(row = 2,column = 0)
button_8.grid(row = 2,column = 1)
button_9.grid(row = 2,column = 2)

button_0.grid(row = 5,column = 1)
button_decimal.grid(row = 5,column = 0)
button_clear.grid(row = 3,column = 4)

button_equal.grid(row = 5,column=2)
button_backspace.grid(row = 2,column=4)

button_add.grid(row = 2,column = 3)
button_subtract.grid(row = 3,column = 3)
button_multiply.grid(row = 4,column = 3)
button_divide.grid(row = 5,column = 3)

# Event binding to ignore keyboard input
e.bind("<Key>", ignore_keyboard_input)
history_label.bind("<Key>", ignore_keyboard_input)

root.mainloop()