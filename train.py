from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x790+0+0")
        self.root.title("face recogniton system")


        title_lbl=Label(self.root,text="TRAIN DATA SET ",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=35)


    #     img_top=Image.open(r"C:\Users\HP\Desktop\minner project\face.jpeg")
    #     img_top=img_top.resize((1300,300),Image.ANTIALIAS)
    #     self.photoimg_top=ImageTk.PhotoImage(img_top)
        
    #     f_lbl=Label(self.root,image=self.photoimg_top)
    #     f_lbl.place(x=0,y=55,width=1300,height=300)
        
    #     #button

    #     b1_1=Button(self.root,text="TRAIN DATA",command=self.getImagesWithID,cursor="hand2",font=("times new roman",27,"bold"),bg="yellow",fg="red")
    #     b1_1.place(x=0,y=350,width=1300,height=40)

    #     img_bottom=Image.open(r"C:\Users\HP\Desktop\minner project\b66.jpeg")
    #     img_bottom=img_bottom.resize((1300,300),Image.ANTIALIAS)
    #     self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
    #     f_lbl=Label(self.root,image=self.photoimg_bottom)
    #     f_lbl.place(x=0,y=390,width=1300,height=300)

    
    # def train_classifier(self):
    #     data_dir=("data")
    #     path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    #     #print(path)
    #     faces=[]
    #     ids=[]

    #     for image in path:
    #         img=Image.open(image).convert('L') #gray scale image
    #         imageNp=np.array(img,'uint8')
    #         id=int(os.path.split(image)[1].split('.')[1])

    #         faces.append(imageNp)
    #         ids.append(id)
    #         cv2.imshow("Training",imageNp)
    #         cv2.waitKey(1)==13
    #         print("waitkey")
    #     return np.array(ids),faces

    #     messagebox.showinfo("result","Training datasets completed!!!")

    #     #******************* Train the classifier And save***********************
    #     Ids,faces=train_classifier(self)
    #     clf=cv2.face.LBPHFaceRecognizer_create()
    #    # print(id)
    #     clf.train(faces,ids)
    #     #clf.save('/trainningData.yml')
    #     clf.write("/classifier.xmL")
    #     print("Th nd")
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("result","Training datasets completed!!!") 

        import cv2
        import os
        import numpy as np
        from PIL import Image

            # Path for face image database
        path = 'data'
        recognizer = cv2.face.LBPHFaceRecognizer()
        def getImagesWithID(path):
            
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            Ids=[]
            for imagePath in imagePaths:
                faceImg=Image.open(imagePath).convert('L')
                faceNp=np.array(faceImg,'uint8')
                ID=int(os.path.split(imagePath)[-1].split('.')[1])
                faces.append(faceNp)
                Ids.append(ID)
                cv2.imshow("training",faceNp)
                cv2.waitKey(10)
            return np.array(Ids), faces

        Ids,faces=getImagesWithID(path)
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,Ids)
        recognizer.write('trainningData.xml')
        cv2.destroyAllWindows()   


            


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        