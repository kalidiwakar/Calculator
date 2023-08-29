from tkinter import *
win = Tk()
win.title("Calculator")
win.geometry("600x600+300+50")
win.resizable(False,False)
win.configure(bg="#18191a")

equation =""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
def clear():
    global equation
    equation =""
    label_result.config(text=equation)
def calc():
    global equation
    result =""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result ="error"
            equation =""
    label_result.config(text=result)

label_result = Label(win, width=25, height=2, text="",bg="#dfe5eb", font=("arial", 30), anchor='e')
label_result.pack()




Button(win,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="red",bg="#8fa6bd",command = lambda: clear()).place(x=10,y=100)
Button(win,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("/")).place(x=150,y=100)
Button(win,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("%")).place(x=290,y=100)
Button(win,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("*")).place(x=430,y=100)

Button(win,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("7")).place(x=10,y=200)
Button(win,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("8")).place(x=150,y=200)
Button(win,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("9")).place(x=290,y=200)
Button(win,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("-")).place(x=430,y=200)

Button(win,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("4")).place(x=10,y=300)
Button(win,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("5")).place(x=150,y=300)
Button(win,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("6")).place(x=290,y=300)
Button(win,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("+")).place(x=430,y=300)

Button(win,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("1")).place(x=10,y=400)
Button(win,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("2")).place(x=150,y=400)
Button(win,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("3")).place(x=290,y=400)
Button(win,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show("0")).place(x=10,y=500)

Button(win,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="black",bg="#8fa6bd",command = lambda: show(".")).place(x=290,y=500)
Button(win,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="red",bg="#8fa6bd",command = lambda: calc()).place(x=430,y=400)
win.mainloop()