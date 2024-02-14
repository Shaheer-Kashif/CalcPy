from tkinter import *
from math import *

num = 0
num2 = 0
sign = None
count = 0
pas = True
hist = ""
result = 0
oneoff = 0

root = Tk()
root.title("Calculator by Shaheer Kashif")
root.iconbitmap("ico/calc.ico")

def ignore_keyboard_input(event):
    return "break"

def buttonclick(inp):
    global count,pas,sign
    if count >= 2 and pas == 0:
        e.delete(0,END)
        pas = 1
    if sign == "=" or sign == "!" or sign == "square" or sign == "root" or sign == "reciprocal":
        history_label.delete(0,END)
        e.delete(0,END)
        sign = ""
    additional = e.get()
    e.delete(0,END)
    e.insert(0,additional+inp)
    
def buttonoperator(op):
    if e.get() == "":
        pass
    else:
        global num,num2,sign,count,pas,hist,result,oneoff
        if ("=" in hist or "!" in history_label.get() or "²" in history_label.get() or "√" in history_label.get() or "ᛑ/"in history_label.get()) and count == 0:
            if "=" in hist:
                hist = hist.replace("",hist[0:hist.index("=")])
            elif "!" in history_label.get() or "²" in history_label.get() or "√" in history_label.get() or "ᛑ/"in history_label.get():
                if "!" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("!")])
                elif "²" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("²")])
                elif "√" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("√")+1])
                elif "ᛑ/"in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("ᛑ/")])
                    
            history_label.delete(0,END)
        if oneoff == 0:
            hist = e.get() + op
        else: 
            hist = op
            oneoff = 0
        history_label.insert(END,hist)
        history_label.grid(row = 0,column=0,columnspan=5)
        if op == "+" or op == "-" or op == "x" or op == "÷" or op == "^":
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
                elif sign == "^":
                    result = pow(float(num),float(num2))
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
            elif sign == "^":
                result = pow(float(num),float(num2))
            sign = op
            e.delete(0,END)
            if result == int(result):
                result = int(result)
            else:
                result = round(result,8)
            e.insert(0,result)

def buttondecimal():
    if "." in e.get():
        pass
    else:
        e.insert(END,".")
        num = e.get()
    
def buttonclear():
    global hist,num,num2,sign,count,pas,result
    hist = ""
    num = 0
    num2 = 0
    sign = None
    count = 0
    pas = True
    result = 0
    history_label.delete(0,END)
    e.delete(0,END)
    
def backspace():
    if e.get() == "":
        pass
    else:
        temp = e.get()
        e.delete(0,END)
        temp = temp.replace(temp[len(temp)-1],"",1)
        e.insert(0,temp)
        
def oneoffs(operation):
    global sign
    if e.get() == "":
        pass
    else:
        if sign != "":
            global num2,count,oneoff
            if operation == '!':
                num2 = e.get()
                history_label.insert(END,str(num2)+"!")
                lis = list(range(2,int(num2)+1))
                num2 = 1
                for res in lis:
                    num2 *= res
            elif operation == 'square' or operation == 'root' or operation == 'reciprocal':
                num2 = e.get()
                if operation == 'root':
                    history_label.insert(END,"√"+str(num2))
                    num2 = sqrt(float(num2))
                elif operation == 'square':
                    history_label.insert(END,str(num2)+"²")
                    num2 = int(num2)*int(num2)
                else:
                    history_label.insert(END,"(ᛑ/"+str(num2)+")")
                    num2 = 1/float(num2)
                    
            e.delete(0,END)
            e.insert(0,num2)
            oneoff = 1
            count += 1
                       
        else:
            if operation == '!':
                num = e.get()
                history_label.delete(0,END)
                history_label.insert(0,str(num)+"!")
                result = 1
                lis = list(range(2,int(num)+1))
                for num in lis:
                    result *= num
                e.delete(0,END)
                e.insert(0,result)
                
            elif operation == 'square' or operation == 'root' or operation == 'reciprocal':
                num = e.get()
                history_label.delete(0,END)
                if operation == 'root':
                    history_label.insert(0,"√"+str(num))
                    result = sqrt(float(num))
                elif operation == 'square':
                    history_label.insert(0,str(num)+"²")
                    result = int(num)*int(num)
                else:
                    history_label.insert(0,"ᛑ/"+str(num))
                    result = 1/float(num)
                
                e.delete(0,END)
                e.insert(0,result)
                
            sign = operation
            
def plusminus():
    if e.get() == "":
        pass
    else:
        tempnum = e.get()
        tempnum = -1*(float(tempnum))
        e.delete(0,END)
        e.insert(0,tempnum)

def percent():
    if e.get() == "":
        pass
    else:
        tempnum = e.get()
        tempnum = (float(tempnum)) / 100
        e.delete(0,END)
        e.insert(0,tempnum)
        
def trigno_funcs(*args):
    trig_option = trig_val.get()
    trig_val.set("Trignometric Functions")
    trigfunc = OptionMenu(root, trig_val, *trig_options)
    trigfunc.grid(row=2,column=0,columnspan=2)
    if trig_option == "Trignometric Functions" or e.get() == "":
        pass
    else:
        tempnum = e.get()
        if trig_option == "sin":
            tempnum = sin(float(tempnum))
        elif trig_option == "cos":
            tempnum = cos(float(tempnum))
        elif trig_option == "tan":
            tempnum = tan(float(tempnum))
        e.delete(0,END)
        e.insert(0,tempnum)

def trigno_funcs_inverse(*args):
    trig_option2 = trig_val2.get()
    trig_val2.set("Trignometric Functions Inverse")
    trigfunc2 = OptionMenu(root, trig_val, *trig_options2)
    trigfunc2.grid(row=2,column=2,columnspan=3,ipadx=17)
    if trig_option2 == "Trignometric Functions Inverse" or e.get() == "":
        pass
    else:
        tempnum = e.get()
        if trig_option2 == "sin⁻¹":
            tempnum = degrees(asin(float(tempnum)))
        elif trig_option2 == "cos⁻¹":
            tempnum = degrees(acos(float(tempnum)))
        elif trig_option2 == "tan⁻¹":
            tempnum = degrees(atan(float(tempnum)))
        e.delete(0,END)
        e.insert(0,tempnum)
        
history_label = Entry(root,width=63,justify="right",borderwidth=0,fg="#3A3A3A")
history_label.grid(row = 0,column=0,columnspan=5)
e = Entry(root, width=25,state="normal",font=("Helvetica",20),justify="right",borderwidth=0)
e.grid(row=1,column=0,columnspan=5)

# defining buttons
button_1 = Button(root,text = "1",command = lambda: buttonclick('1'),padx = 32,pady = 14,font= "helvetica",bg="white")
button_2 = Button(root,text = "2",command = lambda: buttonclick('2'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_3 = Button(root,text = "3",command = lambda: buttonclick('3'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_4 = Button(root,text = "4",command = lambda: buttonclick('4'),padx = 32,pady = 14,font= "helvetica",bg="white")
button_5 = Button(root,text = "5",command = lambda: buttonclick('5'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_6 = Button(root,text = "6",command = lambda: buttonclick('6'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_7 = Button(root,text = "7",command = lambda: buttonclick('7'),padx = 32,pady = 14,font= "helvetica",bg="white")
button_8 = Button(root,text = "8",command = lambda: buttonclick('8'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_9 = Button(root,text = "9",command = lambda: buttonclick('9'),padx = 28,pady = 14,font= "helvetica",bg="white")

button_0 = Button(root,text = "0",command = lambda: buttonclick('0'),padx = 28,pady = 14,font= "helvetica",bg="white")
button_decimal = Button(root,text = ".",command = buttondecimal,padx = 31,pady = 14,font= "helvetica",bg="white")
button_plusminus = Button(root,text = "+/-",command = plusminus,padx = 27,pady = 14,font= "helvetica",bg="white")
button_clear = Button(root,text = "C",command = buttonclear,padx = 29,pady = 14,font= "helvetica")
button_backspace = Button(root, text = "⌫",command = backspace,padx = 24,pady = 14,font= "helvetica")

button_add = Button(root,text = "+",command = lambda: buttonoperator('+'),padx = 26,pady = 14,font= "helvetica")
button_subtract = Button(root,text = "-",command = lambda: buttonoperator('-'),padx = 28,pady = 14,font= "helvetica")
button_multiply = Button(root,text = "×",command = lambda: buttonoperator('x'),padx = 26,pady = 14,font= "helvetica")
button_divide = Button(root,text = "÷",command = lambda: buttonoperator('÷'),padx = 26,pady = 14,font= "helvetica")
button_equal = Button(root,text = "=",command = lambda: buttonoperator('='),padx = 26,pady = 14,font= "helvetica",bg="#176cb5",fg="white")
button_exponent = Button(root,text = "xʸ",command = lambda: buttonoperator('^'),padx = 28,pady = 14,font= "helvetica")
button_factorial = Button(root,text = "x!",command = lambda: oneoffs('!'),padx = 28,pady = 14,font= "helvetica")
button_square = Button(root,text = "x²",command = lambda: oneoffs('square'),padx = 31,pady = 14,font= "helvetica")
button_squareroot = Button(root,text = "√x",command = lambda: oneoffs('root'),padx = 24,pady = 14,font= "helvetica")

button_percent = Button(root,text = "%",command = percent,padx = 28,pady = 14,font= "helvetica")
button_reciprocal = Button(root,text = "1/x",command = lambda: oneoffs('reciprocal'),padx = 23,pady = 14,font= "helvetica")

trig_val = StringVar()
trig_val.set("Trignometric Functions")
trig_options = ["sin","cos","tan"]
trigfunc = OptionMenu(root, trig_val, *trig_options)
trig_val.trace("w",trigno_funcs)
trigfunc.grid(row=2,column=0,columnspan=2)

trig_val2 = StringVar()
trig_val2.set("Trignometric Functions Inverse")
trig_options2 = ["sin⁻¹","cos⁻¹","tan⁻¹"]
trigfunc2 = OptionMenu(root, trig_val2, *trig_options2)
trig_val2.trace("w",trigno_funcs_inverse)
trigfunc2.grid(row=2,column=2,columnspan=3,ipadx=17)

                        
# placing buttons
button_1.grid(row = 6,column = 0)
button_2.grid(row = 6,column = 1)
button_3.grid(row = 6,column = 2)

button_4.grid(row = 5,column = 0)
button_5.grid(row = 5,column = 1)
button_6.grid(row = 5,column = 2)

button_7.grid(row = 4,column = 0)
button_8.grid(row = 4,column = 1)
button_9.grid(row = 4,column = 2)

button_0.grid(row = 7,column = 1)
button_plusminus.grid(row=7,column=0)
button_decimal.grid(row = 7,column = 2)
button_clear.grid(row = 4,column = 4)

button_equal.grid(row = 7,column=3)
button_backspace.grid(row = 3,column=4)

button_add.grid(row = 3,column = 3)
button_square.grid(row = 3 , column= 0)
button_squareroot.grid(row = 3 , column= 1)
button_reciprocal.grid(row = 3, column = 2)

button_subtract.grid(row = 4,column = 3)
button_multiply.grid(row = 5,column = 3)
button_percent.grid(row=5, column=4)
button_divide.grid(row = 6,column = 3)
button_equal.grid(row = 7,column=3)
button_exponent.grid(row = 6,column=4)
button_factorial.grid(row = 7,column=4)


# Event binding to ignore keyboard input
e.bind("<Key>", ignore_keyboard_input)
history_label.bind("<Key>", ignore_keyboard_input)

root.mainloop()