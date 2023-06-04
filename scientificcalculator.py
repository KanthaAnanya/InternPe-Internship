from tkinter import *
import math

def click(val):
    enteredval=entryField.get()     #123 enteredval[0:len(enteredval)-1]
    ans=''
    try:
        if val=="C":
            enteredval=enteredval[0:len(enteredval)-1]  #12
            entryField.delete(0,END)
            entryField.insert(0,enteredval)
            return
        elif val=="CE":
            entryField.delete(0,END)
        elif val=="√":
            ans=math.sqrt(eval(enteredval))
        elif val=="π":
            ans=math.pi
        elif val=="cosθ":
            ans=math.cos(math.radians(eval(enteredval)))
        elif val=="tanθ":
            ans=math.tan(math.radians(eval(enteredval)))
        elif val=="sinθ":
            ans=math.sin(math.radians(eval(enteredval)))
        elif val=="2π":
            ans=2*math.pi
        elif val=="cosh":
            ans=math.cosh(eval(enteredval))
        elif val=="sinh":
            ans=math.sinh(eval(enteredval))
        elif val=="tanh":
            ans=math.tan(eval(enteredval))
        elif val==chr(8731):
            ans=eval(enteredval)**(1/3)
        elif val=="x\u02b8":  #4**2
            entryField.insert(END,'**')
            return
        elif val=="x\u00B3":
            ans=eval(enteredval)**3
        elif val=="x\u00B2":
            ans=eval(enteredval)**2
        elif val=="ln":
            ans=math.log2(eval(enteredval))
        elif val=="deg":
            ans=math.degrees(eval(enteredval))

        elif val=="rad":
            ans=math.radians(eval(enteredval))
            
        elif val=="log₁₀":
            ans=math.log10(eval(enteredval))
        elif val=="e":
            ans=math.e
        elif val=="x!":
            ans=math.factorial(eval(enteredval))
        elif val==chr(247):  #4/2=2
            entryField.insert(END,"/")
            return 
        elif val=="=":  
            ans=eval(enteredval)
        else:
            entryField.insert(END,val)
            return

        entryField.delete(0,END)
        entryField.insert(0,ans)
    except SyntaxError:
        pass
            
root=Tk()
root.title('Scientific Calculator')
root.config(bg='black')
root.geometry('680x500+100+100')

entryField=Entry(root,font=('arial',20,'bold'),bg='black',fg='white',bd=10,relief=SUNKEN,width=30)
entryField.grid(row=0,column=0,columnspan=8)

button_text_list=["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue=1
columnvalue=0
for i in button_text_list:
    

    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='black',fg='white',font=('arial',18,'bold'),activebackground='black',
                  command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue += 1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0
    

root.mainloop()
