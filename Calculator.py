from tkinter import*

calcu = Tk()
calcu.title("Calculator")

calcu.resizable(0,0)

backg=Frame(calcu,bg="white")
backg.pack()

equation=  StringVar()
widg=Entry(backg,textvariable=equation,justify=RIGHT,font=("arial",20,"bold"),bg="black",fg="white")
widg.pack()



def Click(display_n):
    old=widg.get()
    widg.delete(0,END)
    widg.insert(0, old+display_n)
    return

def Clear():
    widg.delete(0,END)
    return
    
def delete():
    current=widg.get()
    length=len(current)-1
    widg.delete(length,END)

def equal():
    ans=widg.get()
    ans=eval(ans)
    widg.delete(0,END)
    widg.insert(0,ans) 
    pass
  
button1 = Button(backg,font= ("arial",15),text=' 1 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("1"), height=3, width=8)
button2 = Button(backg,font= ("arial",15),text=' 2 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("2"), height=3, width=8)
button3 = Button(backg,font= ("arial",15),text=' 3 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("3"), height=3, width=8)
button4 = Button(backg,font= ("arial",15),text=' 4 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("4"), height=3, width=8)
button5 = Button(backg,font= ("arial",15),text=' 5 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("5"), height=3, width=8)
button6 = Button(backg,font= ("arial",15),text=' 6 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("6"), height=3, width=8)
button7 = Button(backg,font= ("arial",15),text=' 7 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("7"), height=3, width=8)
button8 = Button(backg,font= ("arial",15),text=' 8 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("8"), height=3, width=8)
button9 = Button(backg,font= ("arial",15),text=' 9 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("9"), height=3, width=8)
button0 = Button(backg,font= ("arial",15),text=' 0 ',bd=1,relief="sunken",fg='black', bg='white',command=lambda: Click("0"), height=3, width=8)
calcu.mainloop()

