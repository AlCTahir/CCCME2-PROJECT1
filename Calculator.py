from tkinter import*
import math as math

calcu = Tk()
calcu.title("Calculator")

calcu.resizable(0,0)

backg=Frame(calcu,bg="white")
backg.pack()

equation=  StringVar()
widg=Entry(backg,textvariable=equation,justify=RIGHT,font=("arial",20,"bold"),bg="black",fg="white")
widg.pack()



def Click(display_n):
    num=widg.get()
    widg.delete(0,END)
    widg.insert(0, num+display_n)
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
 
def sc(scical):
    key=scical.widget
    text=key["text"]
    no=widg.get()
    result=""
    if text=="√":
        result=str(math.sqrt(float(no)))
    if text =="π":
        if no=="":
            result=str(math.pi)
        else:
            result=str(float(no) * math.pi)
    widg.delete(0, END)
    widg.insert(0,result)

  


calcu.mainloop()
