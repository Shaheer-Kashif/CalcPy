from tkinter import *
from math import *

#Main Variables
num = 0
num2 = 0
sign = None
count = 0
pas = True
hist = ""
result = 0
oneoff = 0
status = "enabled"

#Main Window
root = Tk()
root.title("Calculator by Shaheer Kashif")
root.iconbitmap("ico/calc.ico")
root.resizable(False, False)

def ignore_keyboard_input(event):
    return "break"

# Input Number
def buttonclick(inp):
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    global count,pas,sign
    if count >= 2 and pas == 0:
        e.delete(0,END)
        pas = 1
    if sign == "=" or sign == "!" or sign == "square" or sign == "root" or sign == "reciprocal" or sign == "trig" or sign == "trig_inv":
        history_label.delete(0,END)
        e.delete(0,END)
        sign = ""
    additional = e.get()
    e.delete(0,END)
    e.insert(0,additional+inp)
    
# Main Operator Function
def buttonoperator(op):
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if e.get() == "":
        pass
    else:
        global num,num2,sign,count,pas,hist,result,oneoff,trig_option,trig_option2,hl
        if ("=" in hist or "!" in history_label.get() or "²" in history_label.get() or "√" in history_label.get() or "ᛑ/"in history_label.get() or (sign == "trig" or sign == "trig_inv")) and count == 0:
            if "=" in hist:
                hist = hist.replace("",hist[0:hist.index("=")])
            elif "!" in history_label.get() or "²" in history_label.get() or "√" in history_label.get() or "ᛑ/"in history_label.get() or sign == "trig" or sign == "trig_inv":
                if "!" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("!")])
                elif "²" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("²")])
                elif "√" in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("√")+1])
                elif "ᛑ/"in history_label.get():
                    hist = history_label.get().replace("",history_label.get()[0:history_label.get().index("ᛑ/")])
                elif sign == "trig" or sign == "trig_inv":
                    if sign == "trig":
                        hist = history_label.get().replace("",history_label.get()[0:history_label.get().index(trig_option+"("+hl+")")])
                    elif sign == "trig_inv":
                        hist = history_label.get().replace("",history_label.get()[0:history_label.get().index(trig_option2+"("+hl+")")])
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

# Decimal Function
def buttondecimal():
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if "." in e.get():
        pass
    else:
        e.insert(END,".")
        num = e.get()
    
# Reset Function
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
    
# Backspace Function
def backspace():
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if e.get() == "":
        pass
    else:
        temp = e.get()
        e.delete(0,END)
        temp = temp.replace(temp[len(temp)-1],"",1)
        e.insert(0,temp)
        
# OneOffs Operation(Square,Factorial,Root)
def oneoffs(operation):
    global sign
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if e.get() == "":
        pass
    else:
        if sign != None:
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
      
# Plus Minus Button Function      
def plusminus():
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if e.get() == "":
        pass
    else:
        tempnum = e.get()
        tempnum = -1*(float(tempnum))
        e.delete(0,END)
        e.insert(0,tempnum)

# Percent Button Function
def percent():
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    if e.get() == "":
        pass
    else:
        tempnum = e.get()
        tempnum = (float(tempnum)) / 100
        e.delete(0,END)
        e.insert(0,tempnum)
        
#Trigonometric Function Button
def trigno_funcs(*args):
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    global sign,count,oneoff,trig_option,hl
    trig_option = trig_val.get()
    trig_val.set("Trignometric Functions")
    trigfunc = OptionMenu(root, trig_val, *trig_options)
    trigfunc.grid(row=2,column=0,columnspan=2)
    if trig_option == "Trignometric Functions" or e.get() == "":
        pass
    else:
        tempnum = e.get()
        hl = tempnum
        try:
            if trig_option == "sin":
                history_label.insert(END,"sin("+str(tempnum)+")")
                tempnum = sin(radians(float(tempnum)))
            elif trig_option == "cos":
                history_label.insert(END,"cos("+str(tempnum)+")")
                tempnum = cos(radians(float(tempnum)))
            elif trig_option == "tan":
                history_label.insert(END,"tan("+str(tempnum)+")")
                tempnum = tan(radians(float(tempnum)))
        except ValueError:
            tempnum = "Invalid Input"
            status = "disabled"
        e.delete(0,END)
        e.insert(0,tempnum)
        if sign != None:
            oneoff = 1
            count += 1
        else:
            sign = "trig"
            
trig_val = StringVar()
trig_val.set("Trignometric Functions")
trig_options = ["sin","cos","tan"]
trigfunc = OptionMenu(root, trig_val, *trig_options)
trig_val.trace("w",trigno_funcs)
trigfunc.grid(row=2,column=0,columnspan=2)

#Trigonometric Inverse Function Button
def trigno_funcs_inverse(*args):
    global status
    if status == "disabled":
        buttonclear()
        status = "enabled"
    global sign,count,oneoff,trig_option2,hl
    trig_option2 = trig_val2.get()
    trig_val2.set("Trignometric Inverse Functions")
    trigfunc2 = OptionMenu(root, trig_val2, *trig_options2)
    trigfunc2.grid(row=2,column=2,columnspan=3,ipadx=17)
    if trig_option2 == "Trignometric Inverse Functions" or e.get() == "":
        pass
    else:
        tempnum = e.get()
        hl = tempnum
        try:
            if trig_option2 == "sin⁻¹":
                history_label.insert(END,"sin⁻¹("+str(tempnum)+")")
                tempnum = degrees(asin(float(tempnum)))
            elif trig_option2 == "cos⁻¹":
                history_label.insert(END,"cos⁻¹("+str(tempnum)+")")
                tempnum = degrees(acos(float(tempnum)))
            elif trig_option2 == "tan⁻¹":
                history_label.insert(END,"tan⁻¹("+str(tempnum)+")")
                tempnum = degrees(atan(float(tempnum)))
        except ValueError:
            tempnum = "Invalid Input"
            status = "disabled"
        e.delete(0,END)
        e.insert(0,tempnum)
        if sign != None:
            oneoff = 1
            count += 1
        else:
            sign = "trig_inv"
            
trig_val2 = StringVar()
trig_val2.set("Trignometric Inverse Functions")
trig_options2 = ["sin⁻¹","cos⁻¹","tan⁻¹"]
trigfunc2 = OptionMenu(root, trig_val2, *trig_options2)
trig_val2.trace("w",trigno_funcs_inverse)
trigfunc2.grid(row=2,column=2,columnspan=3,ipadx=17)
        
#History and Calculation Label
history_label = Entry(root,width=68,justify="right",borderwidth=0,fg="#3A3A3A")
history_label.grid(row = 0,column=0,columnspan=5)
e = Entry(root, width=27,state="normal",font=("Helvetica",20),justify="right",borderwidth=0)
e.grid(row=1,column=0,columnspan=5)

# defining buttons 1-9
for i in range(0,10):
    if i == 1 or i == 4 or i == 7:
        locals()["button_"+str(i)] = Button(root,text = str(i) ,command = lambda x = i: buttonclick(str(x)),padx = 32,pady = 14,font= "helvetica",bg="white")
    else:
        locals()["button_"+str(i)] = Button(root,text = str(i),command = lambda x = i: buttonclick(str(x)),padx = 28,pady = 14,font= "helvetica",bg="white")
# placing buttons 1-9
key = 1
for rows in range(6,3,-1):
    for col in range(3):
        (locals()["button_"+str(key)]).grid(row = rows,column = col)
        key += 1

# Basic Arithmetic Operations and their Placing
arith_ope = ["+","-","×","÷","^"]
for index,k in enumerate(arith_ope):
    if k == "-" or k == "^" or k == "×":
        if k == "^":
            locals()["button_"+str(k)] = Button(root,text = "xʸ",command = lambda j = k: buttonoperator(str(j)),padx = 24,pady = 14,font= "helvetica")
        elif k == "×":
            locals()["button_"+str(k)] = Button(root,text = k,command = lambda j = "x": buttonoperator("x"),padx = 26,pady = 14,font= "helvetica")
        else:
            locals()["button_"+str(k)] = Button(root,text = str(k),command = lambda j = k: buttonoperator(str(j)),padx = 28,pady = 14,font= "helvetica")
    else:
        locals()["button_"+str(k)] = Button(root,text = str(k),command = lambda j = k: buttonoperator(str(j)),padx = 26,pady = 14,font= "helvetica")
    locals()["button_"+str(k)].grid(row = index+3,column=3)  
  
# Misc Buttons  
button_decimal = Button(root,text = ".",command = buttondecimal,padx = 31,pady = 14,font= "helvetica",bg="white")
button_plusminus = Button(root,text = "+/-",command = plusminus,padx = 27,pady = 14,font= "helvetica",bg="white")
button_clear = Button(root,text = "C",command = buttonclear,padx = 29,pady = 14,font= "helvetica")
button_backspace = Button(root, text = "⌫",command = backspace,padx = 24,pady = 14,font= "helvetica")

button_equal = Button(root,text = "=",command = lambda: buttonoperator('='),padx = 30,pady = 14,font= "helvetica",bg="#176cb5",fg="white")

button_factorial = Button(root,text = "x!",command = lambda: oneoffs('!'),padx = 28,pady = 14,font= "helvetica")
button_square = Button(root,text = "x²",command = lambda: oneoffs('square'),padx = 31,pady = 14,font= "helvetica")
button_squareroot = Button(root,text = "√x",command = lambda: oneoffs('root'),padx = 24,pady = 14,font= "helvetica")

button_percent = Button(root,text = "%",command = percent,padx = 28,pady = 14,font= "helvetica")
button_reciprocal = Button(root,text = "1/x",command = lambda: oneoffs('reciprocal'),padx = 23,pady = 14,font= "helvetica")
    
# Misc Buttons Placement
button_plusminus.grid(row=7,column=0)
button_0.grid(row=7,column=1)
button_decimal.grid(row=7,column=2)
button_equal.grid(row =7,column=4)

button_factorial.grid(row =6,column=4)

button_percent.grid(row=5,column=4)

button_clear.grid(row=4,column=4)

button_square.grid(row=3, column=0)
button_squareroot.grid(row=3,column=1)
button_reciprocal.grid(row=3,column=2)
button_backspace.grid(row=3,column=4)

# Event binding to ignore keyboard input
e.bind("<Key>", ignore_keyboard_input)
history_label.bind("<Key>", ignore_keyboard_input)

root.mainloop()