import string
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import title
from PIL import Image,ImageTk
from employee2 import Employee
from chatbot import ChatBot 
import os
#from os import startfile
from time import strftime
from datetime import datetime
from train1 import Train
#from face_recognization import Face_Recognition
from developer import Developer
from datetime import datetime
from attendance import Attendance
from face_recognizer2 import Face_Recognition
import tkinter.messagebox
from tkinter import messagebox



class Face_Recognition_System:

   def __init__(self,root):
    self.root=root
    self.root.geometry("1400x660+0+0")
    self.root.title("face Recognition System")
    #first image
    img1=Image.open(r"sss.jpeg")
    img1=img1.resize((500,130),Image.Resampling.LANCZOS)
    self.photoimg1=ImageTk.PhotoImage(img1)

    f_lbl=Label(self.root,image=self.photoimg1)
    f_lbl.place(x=0,y=0,width=400,height=130)
    #2 image
    img2=Image.open(r"ss.jpeg")
    img2=img2.resize((500,130),Image.Resampling.LANCZOS)
    self.photoimg2=ImageTk.PhotoImage(img2)

    f_lbl=Label(self.root,image=self.photoimg2)
    f_lbl.place(x=400,y=0,width=420,height=130)
#3 image
    img3=Image.open(r"ssss.jpeg")
    img3=img3.resize((450,130),Image.Resampling.LANCZOS)
    self.photoimg3=ImageTk.PhotoImage(img3)

    f_lbl=Label(self.root,image=self.photoimg3)
    f_lbl.place(x=820,y=0,width=450,height=130)
#bg image
    img4=Image.open(r"bg.jpeg")
    img4=img4.resize((1400,710),Image.Resampling.LANCZOS)
    self.photoimg4=ImageTk.PhotoImage(img4)

    bg_img=Label(self.root,image=self.photoimg4)
    bg_img.place(x=0,y=130,width=1400,height=710)
    
    title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",20,"bold"),bg="yellow",fg="red")
    title_lbl.place(x=0,y=0,width=1300,height=40)


    #==============time==================
    def time():
        now=datetime.now()
        string = now.strftime("%H:%M:%S")

        # string=datetime.datetime.strptime('2-1-2020 3:14:5', '%m-%d-%Y %H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000,time)
    
    lbl=Label(title_lbl,font = ('times new roman',14,'bold'),background='white',foreground='blue')
    lbl.place(x=0,y=0,width=110,height=50)
    time()


#employee button
    img5=Image.open(r"b.jpeg")
    img5=img5.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg5=ImageTk.PhotoImage(img5)

    b1=Button(bg_img,image=self.photoimg5,command=self.employee2,cursor="hand2")
    b1.place(x=200,y=100,width=180,height=180)

    b1_1=Button(bg_img,text="Employee Details",command=self.employee2 ,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=200,y=280,width=180,height=25)
#detect face button
    img7=Image.open(r"face.jpeg")
    img7=img7.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg7=ImageTk.PhotoImage(img7)

  #  b1=Button(bg_img,image=self.photoimg7,cursor="hand2" )
    b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.face_data )
    b1.place(x=420,y=100,width=180,height=180)
    
    #b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data ,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=420,y=280,width=180,height=25)
#Attendance button
    img6=Image.open(r"bbb.jpeg")
    img6=img6.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg6=ImageTk.PhotoImage(img6)

    b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
    b1.place(x=640,y=100,width=180,height=180)

    b1_1=Button(bg_img,text="Attendance",cursor="hand2", command=self.attendance_data ,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=640,y=280,width=180,height=25)
#help
    img8=Image.open(r"b44.jpeg")
    img8=img8.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg8=ImageTk.PhotoImage(img8)

    b1=Button(bg_img,image=self.photoimg8,command=self.chatbot,cursor="hand2")
    b1.place(x=860,y=100,width=180,height=180)

    b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=860,y=280,width=180,height=25)
#train data button
    img9=Image.open(r"b55.jpeg")
    img9=img9.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg9=ImageTk.PhotoImage(img9)

    b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
    b1.place(x=200,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=200,y=480,width=180,height=25)
#photos button
    img10=Image.open(r"b66.jpeg")
    img10=img10.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg10=ImageTk.PhotoImage(img10)

    b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
    #b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
    b1.place(x=420,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    #b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=420,y=480,width=180,height=25)
#Developer button
    img11=Image.open(r"b77.jpeg")
    img11=img11.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg11=ImageTk.PhotoImage(img11)

    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
    b1.place(x=640,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=640,y=480,width=180,height=25)
#exit button
    img12=Image.open(r"b88.png")
    img12=img12.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg12=ImageTk.PhotoImage(img12)

    b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit )
    #b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
    b1.place(x=860,y=320,width=180,height=180)
    
    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    #b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=860,y=480,width=180,height=25)



   def open_img(self):
        os.startfile("data")
        #self.new_window=Toplevel(self.root)
        #self.app=Employee(self.new_window)

        
   def iExit(self):
        self.iExit=tkinter.Messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return

      #********* function button***********
   def employee2(self):
     self.new_window=Toplevel(self.root)
     self.app=Employee(self.new_window) 


      #********* train button***********
   def train_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Train(self.new_window) 


     #********* face_recognation button***********
   def face_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Face_Recognition(self.new_window) 


    #*************** Attendence system********************

   def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)


        #********* developer button***********
   def developer_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Developer(self.new_window) 

       #********* help button***********
   def chatbot(self):
     self.new_window=Toplevel(self.root)
     self.app=ChatBot(self.new_window) 


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()