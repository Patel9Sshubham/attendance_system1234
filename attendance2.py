from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
#import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Employee Pannel")



        img=Image.open(r"C:\Users\HP\Desktop\minner project\b66.jpeg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=450,height=130)

        
        img22=Image.open(r"C:\Users\HP\Desktop\minner project\bbb.jpeg")
        img22=img22.resize((450,130),Image.ANTIALIAS)
        self.photoimg22=ImageTk.PhotoImage(img22)

        f_lb2 = Label(self.root,image=self.photoimg22)
        f_lb2.place(x=450,y=0,width=450,height=130)

        img1=Image.open(r"C:\Users\HP\Desktop\minner project\b88.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=900,y=0,width=450,height=130)


        bg1=Image.open(r"C:\Users\HP\Desktop\minner project\b77.jpeg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

         #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        img_left=Image.open(r"C:\Users\HP\Desktop\minner project\b44.jpeg")
        img_left=img_left.resize((1366,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1 = Label(left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=645,height=140)

        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white") #bd mean border 
        left_inside_frame.place(x=0,y=140,width=645,height=320)
        
        #labels and entry
         #Employeeid
        EmployeeId_label = Label(left_inside_frame,text="EMP-ID:",font=("verdana",10,"bold"),fg="black",bg="white")
        EmployeeId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        EmployeeId_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        EmployeeId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #emp Roll
        Employee_roll_label = Label(left_inside_frame,text="Roll.No:",font=("verdana",10,"bold"),fg="black",bg="white")
        Employee_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        Employee_roll_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        Employee_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #emp Name
        Employee_name_label = Label(left_inside_frame,text="EMP-Name:",font=("verdana",10,"bold"),fg="black",bg="white")
        Employee_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        Employee_name_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        Employee_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
         #Department
        dep_label = Label(left_inside_frame,text="Department:",font=("verdana",10,"bold"),fg="black",bg="white")
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

         #time
        time_label = Label(left_inside_frame,text="Time:",font=("verdana",10,"bold"),fg="black",bg="white")
        time_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        time_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("verdana",10,"bold"),fg="black",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_inside_frame,text="Attend-status:",font=("verdana",10,"bold"),fg="black",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_inside_frame,width=13,font=("verdana",10,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

         # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=250,width=635,height=50)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        

         # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)
        
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=40,width=620,height=400)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No","department","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("department",text="department")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"
        
        
        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("department",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        # self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
    
        



if __name__ == "_main_":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()