from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x768+0+0")
        self.root.title("Employee Pannel")

     

         #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_Shift=StringVar()
        self.var_Name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        self.var_location=StringVar()



        img=Image.open(r"C:\Users\HP\Desktop\minner project\ff.jpg")
        img=img.resize((430,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=430,height=150)

        
        img22=Image.open(r"C:\Users\HP\Desktop\minner project\ppo.png")
        img22=img22.resize((430,150),Image.ANTIALIAS)
        self.photoimg22=ImageTk.PhotoImage(img22)

        f_lb2 = Label(self.root,image=self.photoimg22)
        f_lb2.place(x=430,y=0,width=430,height=150)

        img1=Image.open(r"C:\Users\HP\Desktop\minner project\sss.jpeg")
        img1=img1.resize((430,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=860,y=0,width=430,height=150)


        bg1=Image.open(r"C:\Users\HP\Desktop\minner project\bg.jpeg")
        bg1=bg1.resize((1530,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=150,width=1530,height=710)

        #  #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",20,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # #========================Section Creating==================================

        # # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=20,y=55,width=1210,height=410)

        # # Left Label Frame 
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        Left_frame.place(x=10,y=10,width=580,height=380)

        img_left=Image.open(r"C:\Users\HP\Desktop\minner project\sss.jpeg")
        img_left=img_left.resize((1366,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1 = Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=560,height=140)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white") 
        left_inside_frame.place(x=0,y=140,width=560,height=180)
        
        #labels and entry
         #Employeeid
        EmployeeId_label = Label(left_inside_frame,text="EMP-ID:",font=("verdana",10,"bold"),fg="black",bg="white")
        EmployeeId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        EmployeeId_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        EmployeeId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #emp Shift
        Employee_Shift_label = Label(left_inside_frame,text="EMP-Shift:",font=("verdana",10,"bold"),fg="black",bg="white")
        Employee_Shift_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        Employee_Shift_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",10,"bold"))
        Employee_Shift_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

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

        #  # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=140,width=635,height=40)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",10,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("verdana",10,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("verdana",10,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("verdana",10,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        

        #  # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=600,y=10,width=600,height=380)
        
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=20,width=580,height=315)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Shift.No","Department","Name","Time","Date","Attend","Location"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="EMP-ID")
        self.attendanceReport.heading("Shift.No",text="Shift.No")
        self.attendanceReport.heading("Name",text="EMP-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport.heading("Location",text="Location")
        self.attendanceReport["show"]="headings"
        
        
        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Shift.No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        self.attendanceReport.column("Location",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
    
    #==============================fetch data====================================
        
    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
#======================import csv============
    def importCsv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
       with open(fln) as myfile:
         csvread=csv.reader(myfile,delimiter=",")
         for i in csvread:
            mydata.append(i)
         self.fetchData(mydata)
            
# ==========export csv=============================

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
             for i in mydata:
              exp_write.writerow(i)
            messagebox.showinfo("Successfuly","Export Data Successfully!"+os.path.basename(fln)+"sucessfully")
        except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  



 #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_row=self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_row)
        rows=content["values"]

        self.var_id.set(rows[0]),
        self.var_Shift.set(rows[1]),
        self.var_Name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_dep.set(rows[4])
        self.var_time.set(rows[5]),
        self.var_date.set(rows[6]),
        self.var_attend.set(rows[7])  

         #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_Shift.set("")
        self.var_Name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")
           #============================Reset Data======================
    def update_data(self):
        self.var_id.set("")
        self.var_Shift.set("")
        self.var_Name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()