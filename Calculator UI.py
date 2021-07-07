from tkinter import*

calcu = Tk()


calcu.title("Calculator") 
calcu.resizable(0,0)

backg=Frame(calcu, bg="white") 
backg.pack() 

equation=  StringVar()
widg=Entry(backg,textvariable=equation,justify=RIGHT,font=("arial",20,"bold"),bg="black",fg="white")
widg.pack()


widg.grid(row=0,column=0,ipadx=10,columnspan = 4,ipady=20,pady=15,)

calcu.mainloop()
