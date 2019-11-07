from tkinter import *
screen=Tk()
screen.geometry("354x460")
screen.title("CALCULATOR")
screen.config(background='Dark gray')
textin=StringVar()
value_to_calc= ""
operetor_list1=["/","*","+","-"]

def clickbut(character):
     global value_to_calc
     try:
        if not (value_to_calc[-2] in operetor_list1 and value_to_calc[-1] in operetor_list1 and character in operetor_list1) and not (value_to_calc[-1] in ["/","*","+","-","."] and character==".") and not (value_to_calc[-1] in operetor_list1 and character in ["/","*"]) and not(value_to_calc[-1]=="." and character in operetor_list1):
            value_to_calc= value_to_calc + str(character)
            textin.set(value_to_calc)
     except:
        try:
            if not (value_to_calc[-1] in operetor_list1 and character in operetor_list1) and not (value_to_calc[-1] in ["/","*","+","-","."] and character==".") and not (value_to_calc[-1] in operetor_list1  and character in ["/","*"] and not(value_to_calc[-1]=="." and character in operetor_list1)):
                value_to_calc= value_to_calc + str(character)
                textin.set(value_to_calc)
        except:
            if character not in ["/","*","."]:
                value_to_calc= value_to_calc + str(character)
                textin.set(value_to_calc)

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
    try:
        if value_to_calc[-1] not in ["/","*","+","-","."]:
            num_list=[]
            operetor_list=[]
            num=""
            for i in value_to_calc:
                if num!="" and i in operetor_list1:
                    operetor_list.append(i)
                    num_list.append(num)
                    num=""
                else:num+=i
            num_list.append(num)
            print(num_list,operetor_list)
            
            for ind,oper in enumerate(operetor_list):
                if oper=="*":
                    num_list[ind:ind+2]=str(int(num_list[ind])*int(num_list[ind+1]))
                    num_list[ind:ind+2] = [''.join(num_list[ind:ind+2])]
                    operetor_list.remove(oper)
                elif oper=="/":
                    num_list[ind:ind + 2] = str(int(num_list[ind]) / int(num_list[ind + 1]))
                    num_list[ind:ind+2] = [''.join(num_list[ind:ind+2])]
                    operetor_list.remove(oper)
            print(operetor_list,num_list)
            
            value_to_calc = int(num_list[0])

            for ind,operater in enumerate(operetor_list):
                if operater=="+":
                    value_to_calc+=int(num_list[ind+1])
                elif operater=="-":
                    value_to_calc-=int(num_list[ind+1])
            
            value_to_calc=str(value_to_calc)
            textin.set(value_to_calc)
    except:
        pass

metext=Entry(screen, font=("Courier New", 30, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()
design_dict={"0":(10,310),"1":(10,100),"2":(10,170),"3":(10,240),"4":(75,100),"5":(75,170),"6":(75,240)
            ,"7":(140,100),"8":(140,170),"9":(140,240),"+":(205,100),"-":(205,170),"/":(205,310),"*":(205,240)}

for num in design_dict:
    but=Button(screen, padx=14, pady=14, bd=4, bg='white',command=lambda:clickbut(num),text=num, font=("Courier New", 16, 'bold'))
    but.place(x=design_dict[num][0],y=design_dict[num][1])
    print(design_dict[num])

butdot=Button(screen, padx=47, pady=14, bd=4, bg='white',command=lambda:clickbut("."), text=".", font=("Courier New", 16, 'bold'))
butdot.place(x=75,y=310)
butclear=Button(screen, padx=14, pady=49, bd=4, bg='white', text="CE",command=lambda:Clear(), font=("Courier New", 16, 'bold'))
butclear.place(x=270,y=100)
butDel=Button(screen, padx=14, pady=49, bd=4, bg='white', text="DEL",command=lambda:Del(), font=("Courier New", 16, 'bold'))
butDel.place(x=265,y=240)
butequal=Button(screen, padx=151, pady=14, bd=4, bg='white', text="=",command=lambda:Result(),font=("Courier New", 16, 'bold'))
butequal.place(x=10,y=380)
screen.mainloop()
