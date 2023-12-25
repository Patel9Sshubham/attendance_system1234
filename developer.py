from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from pip import main


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("face recogniton system")


        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",28,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1330,height=35)


        img_top=Image.open(r"C:\Users\HP\Desktop\minner 1\sss.jpeg")
        img_top=img_top.resize((1330,600),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1330,height=600)

# ====================frame========================-
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=850,y=0,width=400,height=500)

        img_top1=Image.open(r"C:\Users\HP\Desktop\minner 1\k.jpg")
        img_top1=img_top1.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=160,height=160)

        
        #developer info
        dev_label=Label(main_frame,text="Hello i am krishna",font=("times new roman",15,"bold"),fg="green", bg="white")
        dev_label.place(x=0,y=7)

        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",15,"bold"),fg="green", bg="white")
        dev_label.place(x=0,y=40)

        img3=Image.open(r"C:\Users\HP\Desktop\minner 1\b.jpeg")
        img3=img3.resize((400,350),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(main_frame,image=self.photoimg3)
        f_lbl.place(x=0,y=170,width=400,height=350)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop() 