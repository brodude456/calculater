from tkinter import *
screen=Tk()
screen.geometry("354x460")
screen.title("CALCULATOR")
screen.config(background='Dark gray')
textin=StringVar()
value_to_calc= ""

def clickbut(character):
     global value_to_calc
     try:

            value_to_calc= value_to_calc + str(character)
            textin.set(value_to_calc)

     except:

        try:


        except:

def Clear():
    global value_to_calc
    value_to_calc= ""
    textin.set(value_to_calc)

def Del():
    global value_to_calc
    try:value_to_calc= value_to_calc[:-1]
    except:pass
    textin.set(value_to_calc)

def Result():
    global value_to_calc

metext=Entry(screen, font=("Courier New", 30, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()
but1=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(1), text="1", font=("Courier New", 16, 'bold'))
but1.place(x=10,y=100)
but2=Button(screen, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(2), text="2", font=("Courier New", 16, 'bold'))
but2.place(x=10,y=170)
but3=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(3), text="3", font=("Courier New", 16, 'bold'))
but3.place(x=10,y=240)
but4=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(4), text="4", font=("Courier New", 16, 'bold'))
but4.place(x=75,y=100)
but5=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(5), text="5", font=("Courier New", 16, 'bold'))
but5.place(x=75,y=170)
but6=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(6), text="6", font=("Courier New", 16, 'bold'))
but6.place(x=75,y=240)
but7=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(7), text="7", font=("Courier New", 16, 'bold'))
but7.place(x=140,y=100)
but8=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(8), text="8", font=("Courier New", 16, 'bold'))
but8.place(x=140,y=170)
but9=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(9), text="9", font=("Courier New", 16, 'bold'))
but9.place(x=140,y=240)
but0=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(0), text="0", font=("Courier New", 16, 'bold'))
but0.place(x=10,y=310)
butdot=Button(screen, padx=47, pady=14, bd=4, bg='white',command=lambda:clickbut("."), text=".", font=("Courier New", 16, 'bold'))
butdot.place(x=75,y=310)
butpl=Button(screen, padx=14, pady=14, bd=4, bg='white', text="+",command=lambda:clickbut("+"), font=("Courier New", 16, 'bold'))
butpl.place(x=205,y=100)
butsub=Button(screen, padx=14, pady=14, bd=4, bg='white', text="-",command=lambda:clickbut("-"), font=("Courier New", 16, 'bold'))
butsub.place(x=205,y=170)
butml=Button(screen, padx=14, pady=14, bd=4, bg='white', text="*",command=lambda:clickbut("*"), font=("Courier New", 16, 'bold'))
butml.place(x=205,y=240)
butdiv=Button(screen, padx=14, pady=14, bd=4, bg='white', text="/",command=lambda:clickbut("/"), font=("Courier New", 16, 'bold'))
butdiv.place(x=205,y=310)
butclear=Button(screen, padx=14, pady=49, bd=4, bg='white', text="CE",command=lambda:Clear(), font=("Courier New", 16, 'bold'))
butclear.place(x=270,y=100)
butDel=Button(screen, padx=14, pady=49, bd=4, bg='white', text="DEL",command=lambda:Del(), font=("Courier New", 16, 'bold'))
butDel.place(x=265,y=240)
butequal=Button(screen, padx=151, pady=14, bd=4, bg='white', text="=",command=lambda:Result(),font=("Courier New", 16, 'bold'))
butequal.place(x=10,y=380)
screen.mainloop()
