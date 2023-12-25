# from itertools import _Predicate
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import rectangle
import mysql.connector
import cv2
import os
import numpy as np
# from itertools import _Predicate
# from itertools import izip_longest
# from itertools import zip_longest


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("face recogniton system")



        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",28,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1330,height=35)


        img_top=Image.open(r"C:\Users\HP\Desktop\minner 1\face.jpeg")
        img_top=img_top.resize((600,600),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=600,height=600)


        img_bottom=Image.open(r"C:\Users\HP\Desktop\minner 1\bbb.jpeg")
        img_bottom=img_bottom.resize((700,610),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=610,y=50,width=700,height=610)

        #button

        b1_1=Button(self.root,text="FACE RECOGNATION",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=800,y=600,width=300,height=40)

    #====================== face recognition =====================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
            feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for(x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,Predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-Predict/300)))

                c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                my_cursor=c.cursor()

                my_cursor.execute("select name from employee where employeeid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Shift from employee where employeeid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from employee where employeeid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                

                if confidence>77:
                    cv2.putText(img,f"employeeName:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"employeeid:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)        
            return img

        faceCscade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFfaceRecognizer_create()
        clf.read("trainningData.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCscade)
            cv2.imshow("welcome To face recognition",img)

            if cv2.waitKey():
                break
        video_cap.release()
        cv2.destroyAllWindows()
                        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 