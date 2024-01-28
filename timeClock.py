from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("clock")

def time():
   string = strftime('%H:%M:%S %p')
   l.config(text=string)
   l.after(1000,time)

l = Label(root , foreground="black" , background="white" , font="Helvetica" )
l.pack(anchor='center')
time()
mainloop()