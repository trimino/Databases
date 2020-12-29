from tkinter import *
w = Tk()
w.geometry('650x400')

state=StringVar()

c=Canvas(w,bg="gray94",height=750,width=650)
c.config(scrollregion=c.bbox("all"))
c.pack(expand=YES,fill=BOTH)

scr=Scrollbar(c)
scr.pack(side=RIGHT,fill=Y)

c.config(yscrollcommand=scr.set)
scr.config(command=c.yview)

l2 = ['KA', 'NY']

#widgets
button1 = Button(c, text="Back")
label1 = Label(c, text="Registration form", width=20, font=("bold", 20))
label2 = Label(c, text="State", width=20, font=("bold", 10))
dl2 = OptionMenu(w, state, *l2)
button2 = Button(c, text='Submit', width=20)

c.create_window(100, 200, window=button1)
c.create_window(160, 750, window=label1)
c.create_window(310, 390, window=dl2)
c.create_window(149, 390, window=label2)
c.create_window(240, 690, window=button2)

c.configure(scrollregio=c.bbox("all"))

w.mainloop()