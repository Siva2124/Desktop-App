import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox
from time import strftime

root = tk.Tk()
root.title("AU Math Calculator")
root.geometry('750x750+120+120')
#root.attributes('-alpha',0.5)
root.iconbitmap('./res/calculator.ico')

n11 = StringVar()
n12 = StringVar()
n21 = StringVar()
n22 = StringVar()
n31 = StringVar()
n32 = StringVar()
n41 = StringVar()
n42 = StringVar()
n51 = StringVar()
n52 = StringVar()
n61 = StringVar()
n62 = StringVar()
n71 = StringVar()
n72 = StringVar()
n81 = StringVar()
n82 = StringVar()
n91 = StringVar()
n92 = StringVar()
ans1 =StringVar()

def reset():
     n11.set("")
     n12.set("")
     n21.set("")
     n22.set("")
     n31.set("")
     n32.set("")
     n41.set("")
     n42.set("")
     n51.set("")
     n52.set("")
     n61.set("")
     n62.set("")
     n71.set("")
     n72.set("")
     n81.set("")
     n82.set("")
     n91.set("")
     n92.set("")
     ans1.set("")

def gpa():
    n1,n2,n3,n4,n5,n6 = (n11.get()),(n12.get()),(n21.get()),(n22.get()),(n31.get()),(n32.get())
    m1,m2,m3,m4,m5,m6 = (n41.get()),(n42.get()),(n51.get()),(n52.get()),(n61.get()),(n62.get())
    k1,k2,k3,k4,k5,k6 = (n71.get()),(n72.get()),(n81.get()),(n82.get()),(n91.get()),(n92.get())

    if (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit() and m1.isdigit() and m2.isdigit() and m3.isdigit() and m4.isdigit() and m5.isdigit() and m6.isdigit() and k1.isdigit() and k2.isdigit() and k3.isdigit() and k4.isdigit() and k5.isdigit() and k6.isdigit()):

        n1=int(float(n1))
        n2=int(float(n2))
        n3=int(float(n3))
        n4=int(float(n4))
        n5=int(float(n5))
        n6=int(float(n6))
        m1=int(float(m1))
        m2=int(float(m2))
        m3=int(float(m3))
        m4=int(float(m4))
        m5=int(float(m5))
        m6=int(float(m6))
        k1=int(float(k1))
        k2=int(float(k2))
        k3=int(float(k3))
        k4=int(float(k4))
        k5=int(float(k5))
        k6=int(float(k6))

        ans3 =((n1*n2)+(n3*n4)+(n5*n6)+(m1*m2)+(m3*m4)+(m5*m6)+(k1*k2)+(k3*k4)+(k5*k6))
        
        ans2 = float(ans3/(n1+n3+n5+m1+m3+m5+k1+k3+k5))
        
        ans1.set(ans2)
        tk.messagebox.showinfo("Correct Data","Well Done! Good")
        return True
    else :
        tk.messagebox.showwarning("Incorrect Data","Invalid Data ,Number only allowed")
        n11.set("")
        n12.set("")
        n21.set("")
        n22.set("")
        n31.set("")
        n32.set("")
        n41.set("")
        n42.set("")
        n51.set("")
        n52.set("")
        n61.set("")
        n62.set("")
        n71.set("")
        n72.set("")
        n81.set("")
        n82.set("")
        n91.set("")
        n92.set("")
        ans1.set("")
        return False
    return



def cgpa():
    n1,n2,n3,n4,n5,n6 = (n11.get()),(n12.get()),(n21.get()),(n22.get()),(n31.get()),(n32.get())
    m1,m2,m3,m4,m5,m6 = (n41.get()),(n42.get()),(n51.get()),(n52.get()),(n61.get()),(n62.get())
    k1,k2,k3,k4 = (n71.get()),(n72.get()),(n81.get()),(n82.get())

    if (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit() and m1.isdigit() and m2.isdigit() and m3.isdigit() and m4.isdigit() and m5.isdigit() and m6.isdigit() and k1.isdigit() and k2.isdigit() and k3.isdigit() and k4.isdigit()):

        n1=int(float(n1))
        n2=int(float(n2))
        n3=int(float(n3))
        n4=int(float(n4))
        n5=int(float(n5))
        n6=int(float(n6))
        m1=int(float(m1))
        m2=int(float(m2))
        m3=int(float(m3))
        m4=int(float(m4))
        m5=int(float(m5))
        m6=int(float(m6))
        k1=int(float(k1))
        k2=int(float(k2))
        k3=int(float(k3))
        k4=int(float(k4))
#        k5=int(float(k5))
#        k6=int(float(k6))

        ans3 =(n1+n3+n5+m1+m3+m5+k1+k3)
        
        ans2 = float(ans3/(n2+n4+n6+m2+m4+m6+k2+k4))
        
        ans1.set(ans2)
        tk.messagebox.showinfo("Correct Data","Well Done! Good")
        return True

    else :
        tk.messagebox.showwarning("Incorrect Data","Invalid Data ,Number only allowed")
        n11.set("")
        n12.set("")
        n21.set("")
        n22.set("")
        n31.set("")
        n32.set("")
        n41.set("")
        n42.set("")
        n51.set("")
        n52.set("")
        n61.set("")
        n62.set("")
        n71.set("")
        n72.set("")
        n81.set("")
        n82.set("")
#        n91.set("")
#        n92.set("")
        ans1.set("")
        return False
    return

def time():
     string = strftime('%H:%M:%S %p')
     lab.config(text=string)
     lab.after(1000,time)
    
def startone():
    global lab
    btn10.destroy()
    btn11.destroy()
    
    label0= Label(canvas,text=r"AU STUDENT'S CALCULATION SYSTEM",
              bg="#54E45E",fg="Dark green")
    label0.configure(font =("Times", 25))
    label0.place(x=300,y=10)

    lab = Label(canvas,font=("ds-digital",40),background = "black", foreground = "cyan")
    lab.place(x=1000,y=50)
    time()

#==============================Labels=====&====== Entries============================================================
    label_1= Label(canvas,text ="Credit Scores",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label_1.place(x=400,y=70)
    label_1= Label(canvas,text ="Grade points",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label_1.place(x=700,y=70)


    label1= Label(canvas,text ="sub_1",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label1.place(x=50,y=120)
    entry1= Entry(canvas,width=20,bd=10,textvariable= n11)
    entry1.place(x=400,y=120)
    entry1= Entry(canvas,width=20,bd=10,textvariable= n12)
    entry1.place(x=700,y=120)

    label2= Label(canvas,text ="sub_2",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label2.place(x=50,y=170)
    entry2= Entry(canvas,bd=10,textvariable= n21)
    entry2.place(x=400,y=170)
    entry2= Entry(canvas,bd=10,textvariable= n22)
    entry2.place(x=700,y=170)

    label3= Label(canvas,text ="sub_3",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label3.place(x=50,y=220)
    entry3= Entry(canvas,bd=10,textvariable= n31)
    entry3.place(x=400,y=220)
    entry3= Entry(canvas,bd=10,textvariable= n32)
    entry3.place(x=700,y=220)

    label4= Label(canvas,text ="sub_4",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label4.place(x=50,y=270)
    entry4= Entry(canvas,bd=10,textvariable= n41)
    entry4.place(x=400,y=270)
    entry4= Entry(canvas,bd=10,textvariable= n42)
    entry4.place(x=700,y=270)

    label5= Label(canvas,text ="sub_5",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label5.place(x=50,y=320)
    entry5= Entry(canvas,bd=10,textvariable= n51)
    entry5.place(x=400,y=320)
    entry5= Entry(canvas,bd=10,textvariable= n52)
    entry5.place(x=700,y=320)

    label6= Label(canvas,text ="sub_6",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label6.place(x=50,y=370)
    entry6= Entry(canvas,bd=10,textvariable= n61)
    entry6.place(x=400,y=370)
    entry6= Entry(canvas,bd=10,textvariable= n62)
    entry6.place(x=700,y=370)

    label7= Label(canvas,text ="prac_sub1",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label7.place(x=50,y=420)
    entry7= Entry(canvas,bd=10,textvariable= n71)
    entry7.place(x=400,y=420)
    entry7= Entry(canvas,bd=10,textvariable= n72)
    entry7.place(x=700,y=420)

    label8= Label(canvas,text ="prac_sub2",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label8.place(x=50,y=470)
    entry8= Entry(canvas,bd=10,textvariable= n81)
    entry8.place(x=400,y=470)
    entry8= Entry(canvas,bd=10,textvariable= n82)
    entry8.place(x=700,y=470)

    label9= Label(canvas,text ="prac_sub3",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label9.place(x=50,y=520)
    entry9= Entry(canvas,bd=10,textvariable= n91)
    entry9.place(x=400,y=520)
    entry9= Entry(canvas,bd=10,textvariable= n92)
    entry9.place(x=700,y=520)


    label10= Label(canvas,text =" GPA ",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
    label10.place(x=900,y=370)
    entry10= Entry(canvas,bd=10,textvariable=ans1)
    entry10.place(x=950,y=470)

    btn1 = Button(canvas,text = " Reset" , anchor = 'center',
                  width = 20,bg="#77FFFF",fg="blue",
                  activebackground = "#54E45E",font = "Times 15",command = reset)
    reset_button = canvas.create_window(500,600,anchor='center',window=btn1)

    btn2 = Button(canvas,text = " Calculate " , anchor = 'center',
                  width = 20,bg="#77FFFF",fg="blue",
                  activebackground = "#54E45E",font = "Times 15",command = gpa)
    calc_button = canvas.create_window(800,600,anchor='center',window=btn2)
    print("Sucessfully Executed!!!")


def starttwo():
     global lab
     btn10.destroy()
     btn11.destroy()
     label0= Label(canvas,text="AU STUDENTS CALCULATION SYSTEM",
              bg="#54E45E",fg="Dark green")
     label0.configure(font =("Times", 25))
     label0.place(x=300,y=10)

     lab = Label(canvas,font=("ds-digital",40),background = "black", foreground = "cyan")
     lab.place(x=1000,y=50)
     time()
    
     label_1= Label(canvas,text ="Total Scores",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label_1.place(x=400,y=70)
     label_1= Label(canvas,text ="Total Grade points",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label_1.place(x=700,y=70)


     label1= Label(canvas,text ="sem_1",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label1.place(x=50,y=120)
     entry1= Entry(canvas,width=20,bd=10,textvariable= n11)
     entry1.place(x=400,y=120)
     entry1= Entry(canvas,width=20,bd=10,textvariable= n12)
     entry1.place(x=700,y=120)

     label2= Label(canvas,text ="sem_2",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label2.place(x=50,y=170)
     entry2= Entry(canvas,bd=10,textvariable= n21)
     entry2.place(x=400,y=170)
     entry2= Entry(canvas,bd=10,textvariable= n22)
     entry2.place(x=700,y=170)

     label3= Label(canvas,text ="sem_3",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label3.place(x=50,y=220)
     entry3= Entry(canvas,bd=10,textvariable= n31)
     entry3.place(x=400,y=220)
     entry3= Entry(canvas,bd=10,textvariable= n32)
     entry3.place(x=700,y=220)

     label4= Label(canvas,text ="sem_4",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label4.place(x=50,y=270)
     entry4= Entry(canvas,bd=10,textvariable= n41)
     entry4.place(x=400,y=270)
     entry4= Entry(canvas,bd=10,textvariable= n42)
     entry4.place(x=700,y=270)

     label5= Label(canvas,text ="sem_5",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label5.place(x=50,y=320)
     entry5= Entry(canvas,bd=10,textvariable= n51)
     entry5.place(x=400,y=320)
     entry5= Entry(canvas,bd=10,textvariable= n52)
     entry5.place(x=700,y=320)

     label6= Label(canvas,text ="sem_6",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label6.place(x=50,y=370)
     entry6= Entry(canvas,bd=10,textvariable= n61)
     entry6.place(x=400,y=370)
     entry6= Entry(canvas,bd=10,textvariable= n62)
     entry6.place(x=700,y=370)

     label7= Label(canvas,text ="sem_7",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label7.place(x=50,y=420)
     entry7= Entry(canvas,bd=10,textvariable= n71)
     entry7.place(x=400,y=420)
     entry7= Entry(canvas,bd=10,textvariable= n72)
     entry7.place(x=700,y=420)

     label8= Label(canvas,text ="sem_8",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label8.place(x=50,y=470)
     entry8= Entry(canvas,bd=10,textvariable= n81)
     entry8.place(x=400,y=470)
     entry8= Entry(canvas,bd=10,textvariable= n82)
     entry8.place(x=700,y=470)

     label10= Label(canvas,text =" CGPA ",width=20,bg="#54E40A",fg="Dark blue",bd=10,font=("bold",15))
     label10.place(x=900,y=370)
     entry10= Entry(canvas,bd=10,textvariable=ans1)
     entry10.place(x=950,y=470)    

#     bbtn = Button(canvas,text = "<<" , anchor = 'center',
#                 width = 15,bg="#54E40A",fg="Dark blue",
#                  activebackground = "#54E45E",font = "Times 15",command = back)
#     back_button = canvas.create_window(100,600,anchor='center',window=bbtn)
     btn1 = Button(canvas,text = " Reset" , anchor = 'center',
              width = 20,bg="#77FFFF",fg="blue",
              activebackground = "#54E45E",font = "Times 15",command = reset)
     reset_button = canvas.create_window(500,600,anchor='center',window=btn1)

     btn2 = Button(canvas,text = " Calculate " , anchor = 'center',
                   width = 20,bg="#77FFFF",fg="blue",
                   activebackground = "#54E45E",font = "Times 15",command = cgpa)
     calc_button = canvas.create_window(800,600,anchor='center',window=btn2)
     print("Sucessfully Executed!!!")

#def back():
#     k=starttwo()
#     k.destroy()
     

def startapp():
     global btn10
     global btn11
     btn10 = Button(canvas,text = " GPA " , anchor = 'center',
                  width = 15,bg="#54E40A",fg="Dark blue",height =3,border =0,
                  activebackground = "#54E45E",font = "Times 30",command = startone)
     start1_button = canvas.create_window(300,300,anchor='center',window=btn10)

     btn11 = Button(canvas,text = " CGPA " , anchor = 'center',
                  width = 15,bg="#54E40A",fg="Dark blue",height =3,border = 0,
                  activebackground = "#54E45E",font = "Times 30",command = starttwo)
     start1_button = canvas.create_window(900,300,anchor='center',window=btn11)

def start():
    label1.destroy()
    label2.destroy()
    btn.destroy()
    startapp()




canvas=Canvas(root,width=1240, height=800)
img=ImageTk.PhotoImage(Image.open("./res/Fresh.png"))
canvas.create_image(0,0,anchor=NW, image=img)

label1= Label(canvas,
              text =" AU Students Calculation System",
              width=45,
              bg="yellow",
              fg="red",
              justify = "center",
              
              bd=10,
              font=("Times",30,"bold"))
label1.place(x=50,y=50)

label2= Label(canvas,
              text ="You are welcome !\n To our system\n That's a great one.",
              width=50,
              bg="#33ff33",
              fg="Dark blue",
              justify = "center",
              
              bd=10,
              font=("Old English Text MT",25,"bold"))
label2.place(x=50,y=270)

btn = Button(
    canvas,
    text = "START >",
    font = ("Matura MT Script Capitals",20,"bold"),
    bg = "#77FFFF",
    fg = "blue",
    activebackground ="yellow",
    command = start
)
startbutton = canvas.create_window(620,600,anchor='center',window=btn)


canvas.pack()
root.mainloop()
