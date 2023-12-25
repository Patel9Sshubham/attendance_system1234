# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
# from sqlite3 import *
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        
        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",28,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1330,height=35)

        img_top=Image.open(r"C:\Users\HP\Desktop\minner project\face.jpeg")
        img_top=img_top.resize((600,580),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=600,height=580)


        img_bottom=Image.open(r"C:\Users\HP\Desktop\minner project\bbb.jpeg")
        img_bottom=img_bottom.resize((650,580),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=610,y=55,width=650,height=580)

        #button

        b1_1=Button(f_lbl,text="FACE RECOGNATION",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=150,y=510,width=300,height=40)

    #====================== face recognition =====================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,Predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-Predict/300)))

                c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                my_cursor=c.cursor()

                my_cursor.execute("select name from employee where employeeId="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select City from employee where employeeId="+str(id))
                R=my_cursor.fetchone()
                R="+".join(R)
                print("hello1")

                if confidence>77:
                    cv2.putText(img,f"employeeName:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"employeeId:{R}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    
                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)        
            return img
        
        faceCscade=cv2.CascadeClassifier("C:\\Program Files\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFfaceRecognizer_create()
        clf.read("C:\\Users\HP\\Desktop\\git project\\Python-FYP-Face-Recognition-Attendence-System-1\\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCscade)
            cv2.imshow("welcome To face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    root.mainloop()