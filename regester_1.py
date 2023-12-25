
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("regester")
        self.root.geometry("1300x800+0+0")


        #**************bg img*****************
        self.bg=ImageTk.PhotoImage(file=r"ee.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        # *************left image****************
        self.bg1=ImageTk.PhotoImage(file=r"C:/Users/HP/Desktop/minner 1/regester1.jpeg")
        
        left_bg1=Label(self.root,image=self.bg1)
        left_bg1.place(x=50,y=100, width=400,height=450)

       #****************main frame***************
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=100,width=750,height=450)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)


        #******************lables and entry********************
        #*****************row1************************

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)

        self.fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=100,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=100,width=250)

        #************row2****************
        contact=Label(frame,text="contact no",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=140)

        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=170,width=250)


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=140)

        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=170,width=250)
        

        #************row3****************
        security_Q=Label(frame,text="select security quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=210)

        self.txt_combosecurity_Q=ttk.Combobox(frame,font=("times new roman",15),state="ReadOnly")
        self.txt_combosecurity_Q["values"]=("select","your Birth place","your country")
        self.txt_combosecurity_Q.place(x=50,y=240,width=250)
        self.txt_combosecurity_Q.current(0)


        security_A=Label(frame,text="security_Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=210)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=240,width=250)

        #************row4****************
        pswd=Label(frame,text="password ",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=280)

        self.txt_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=310,width=250)


        confirm_pswd=Label(frame,text="confirm password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=280)

        self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=310,width=250)

        #******************chechbutton********************

        Checkbtn=Checkbutton(frame,text="I agree the term and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=350)

        #**************buttons**************
        img4=Image.open("C:/Users/HP/Desktop/minner 1/button regester.jpeg")
        img4=img4.resize((100,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=100,y=390,width=100)
    
        
        img5=Image.open("C:/Users/HP/Desktop/minner 1/b88.png")
        img5=img5.resize((100,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img5)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=420,y=390,width=100)

        
        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
