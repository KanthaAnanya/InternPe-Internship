#import required modules
from tkinter import *
from tkinter.ttk import *

#importing strftime function to retrieve system's time
from time import strftime
root=Tk()
root.title=(' Digital Clock')

#function to dispaly time,day and date on the label
def clock():
    time_string =strftime('%H:%M:%S %p')  
    time_label.config(text=time_string)
    root.after(1000,clock)

    day_string=strftime('%A')           
    day_label.config(text=day_string)

    date_string=strftime('%B %d,%Y')       
    date_label.config(text=date_string)

time_label=Label(root,font=(' arial italic',50,'bold'),background='black',foreground='white')
day_label=Label(root,font=('arial italic',25,'bold'),background='white',foreground='black')
date_label=Label(root,font=('arial italic',25,'bold'),background='white',foreground='black')

#to place clock at the center of the window
time_label.pack(anchor='center')
clock()

day_label.pack(anchor='center')
clock()

date_label.pack(anchor='center')
clock()

root.mainloop()
