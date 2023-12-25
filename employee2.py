from tkinter import*
from tkinter import ttk
from tkinter.tix import TEXT
from turtle import left, st, update 
from PIL import Image,ImageTk
from tkinter import messagebox
from colorama import Cursor
import mysql.connector
import cv2


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("face recogniton system")

        # **************variables***********
        self.var_dep=StringVar()
        self.var_City=StringVar()
        self.var_year=StringVar()
        self.var_Shift=StringVar()
        self.var_employeeid=StringVar()
        self.var_name=StringVar()
        #self.var_gender=StringVar()
        self.var_age=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

        #first image
        img1=Image.open(r"C:\Users\HP\Desktop\minner 1\sss.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=120)
        #2 image
        img2=Image.open(r"C:\Users\HP\Desktop\minner 1\ss.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=120)
        #3 image
        img3=Image.open(r"C:\Users\HP\Desktop\minner 1\ssss.jpeg")
        img3=img3.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=450,height=120)

        #bg image
        img4=Image.open(r"C:\Users\HP\Desktop\minner 1\b77.jpeg")
        img4=img4.resize((1400,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=120,width=1400,height=710)
        title_lbl=Label(bg_img,text="EMPLOYEE ATTENDANCE MANAGMENT SYSTEM ",font=("times new roman",28,"bold"),bg="white",fg="dark red")
        title_lbl.place(x=0,y=0,width=1430,height=35)

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=10,y=45,width=1250,height=470)
        

        #left lable frame

        left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="employee Details",font=("times new roman ",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=450)

        img_left=Image.open(r"C:\Users\HP\Desktop\minner 1\b66.jpeg")
        img_left=img_left.resize((600,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=33,y=200,width=587,height=90)

        #current courses
        current_position_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="current Work information",font=("times new roman ",12,"bold"))
        current_position_frame.place(x=20,y=120,width=580,height=110)

        #department
        dep_label=Label(current_position_frame,text="department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        
        dep_combo=ttk.Combobox(current_position_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"),state="read only",width=17)
        dep_combo["values"]=("select Department","computer","it","civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        

        # City
        City_label=Label(current_position_frame,text="City",font=("times new roman",12,"bold"),bg="white")
        City_label.grid(row=0,column=2,padx=10,sticky=W)

        
        City_combo=ttk.Combobox(current_position_frame,textvariable=self.var_City ,font=("times new roman",12,"bold"),state="read only",width=17)
        City_combo["values"]=("select City","Dewas","Indore","Ujjain","Delhi","Bhopal")
        City_combo.current(0)
        City_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

                                
        # year
        year_label=Label(current_position_frame,text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        
        year_combo=ttk.Combobox(current_position_frame,textvariable=self.var_year ,font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)                    
        
         #semester
        Shift_label=Label(current_position_frame,text="Shift",font=("times new roman",12,"bold"),bg="white")
        Shift_label.grid(row=1,column=2,padx=10,sticky=W)

        
        Shift_combo=ttk.Combobox(current_position_frame,textvariable=self.var_Shift, font=("times new roman",12,"bold"),state="read only",width=17)
        Shift_combo["values"]=("select Shift","1st","2nd")
        Shift_combo.current(0)
        Shift_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)   
        

        #company employee information

        company_employee_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="employee information",font=("times new roman ",12,"bold"))
        company_employee_frame.place(x=20,y=240,width=580,height=210)

        #employee ID
        employeeId_label=Label(company_employee_frame,text="employeeId:",font=("times new roman",12,"bold"),bg="white")
        employeeId_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        employeeId_entry=ttk.Entry(company_employee_frame,textvariable=self.var_employeeid ,width=16,font=("times new roman",12,"bold"))
        employeeId_entry.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        
        #employee Name
        employeeName_label=Label(company_employee_frame,text="employeeName:",font=("times new roman",12,"bold"),bg="white")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        employeeName_entry=ttk.Entry(company_employee_frame,textvariable=self.var_name ,width=16,font=("times new roman",12,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=5,pady=2,sticky=W)

        # #employee Gender
        # employeeGender_label=Label(company_employee_frame,text="employeeGender:",font=("times new roman",12,"bold"),bg="white")
        # employeeGender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # employeeGender_entry=ttk.Entry(company_employee_frame, textvariable=self.var_gender ,width=16,font=("times new roman",12,"bold"))
        # employeeGender_entry.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        

        #employee age
        employeeage_label=Label(company_employee_frame,text="employeeage:",font=("times new roman",12,"bold"),bg="white")
        employeeage_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        employeeage_entry=ttk.Entry(company_employee_frame,textvariable=self.var_age ,width=16,font=("times new roman",12,"bold"))
        employeeage_entry.grid(row=1,column=3,padx=5,pady=2,sticky=W)

        #employee address
        employeeaddress_label=Label(company_employee_frame,text="employeeaddress:",font=("times new roman",12,"bold"),bg="white")
        employeeaddress_label.grid(row=1,column=0,padx=10,pady=7,sticky=W)

        employeeaddress_entry=ttk.Entry(company_employee_frame,textvariable=self.var_address ,width=16,font=("times new roman",12,"bold"))
        employeeaddress_entry.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #employee Email
        employeeEmail_label=Label(company_employee_frame,text="employeeEmail:",font=("times new roman",12,"bold"),bg="white")
        employeeEmail_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        employeeEmail_entry=ttk.Entry(company_employee_frame,textvariable=self.var_email ,width=16,font=("times new roman",12,"bold"))
        employeeEmail_entry.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        
        #employee PhNo
        employeePhNo_label=Label(company_employee_frame,text="employeePhNo:",font=("times new roman",12,"bold"),bg="white")
        employeePhNo_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        employeePhNo_entry=ttk.Entry(company_employee_frame,textvariable=self.var_phone ,width=16,font=("times new roman",12,"bold"))
        employeePhNo_entry.grid(row=2,column=3,padx=5,pady=2,sticky=W)
        
        #radio Button

        self.var_radio1=StringVar()
        Radiobtn1=ttk.Radiobutton(company_employee_frame,variable=self.var_radio1, text="take photo sample",value="yes")
        Radiobtn1.grid(row=6,column=0)

        
        Radiobtn2=ttk.Radiobutton(company_employee_frame,variable=self.var_radio1,text="No photo sample",value="No")
        Radiobtn2.grid(row=6,column=1)

        #bbuttons frame

        btn_frame=Frame(company_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=135,width=575,height=45)

        
        save_btn=Button(btn_frame,text="save",command=self.add_data ,width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update_data,text="update",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data, width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data, width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(company_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=157,width=575,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset, text="Take photo sample",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="update photo sample",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #Right lable frame

        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="employee Details",font=("times new roman ",12,"bold"))
        Right_frame.place(x=650,y=10,width=590,height=450)

        img_right=Image.open(r"C:\Users\HP\Desktop\minner 1\b.jpeg")
        img_right=img_right.resize((600,100),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=670,y=200,width=580,height=90)

        #**********search system*************

        search_frame=LabelFrame(Right_frame,bd=2, bg="white",relief=RIDGE,text="search system",font=("times new roman ",12,"bold"))
        search_frame.place(x=5,y=100,width=575,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=10)
        search_combo["values"]=("select","City","employee_id","name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.fetch_data,text="search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        search_btn=Button(search_frame,command=self.fetch_data,text="show All",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=4)
  
        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=180,width=575,height=240)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","City","year","Shift","employeeId","employeeName","address","age","email","phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("City",text="City")
        self.employee_table.heading("year",text="year")
        self.employee_table.heading("Shift",text="Shift")
        self.employee_table.heading("employeeId",text="employeeId")
        self.employee_table.heading("employeeName",text="employeeName")
        self.employee_table.heading("address",text="employeeaddress")
        self.employee_table.heading("age",text="employeeage")
        self.employee_table.heading("email",text="employeeEmail")
        self.employee_table.heading("phone",text="employeePhNo")
        #self.employee_table.heading("photo",text="photo")
        self.employee_table["show"]="headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("City",width=100)
        self.employee_table.column("year",width=100)
        self.employee_table.column("Shift",width=100)
        self.employee_table.column("employeeId",width=100)
        self.employee_table.column("employeeName",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("age",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        #self.employee_table.column("photo",width=150)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
#====================== function declearation=================

    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_employeeid.get()=="":
            messagebox.showerror("Error ", "All the fields are required",parent=self.root)
        else:
            try:
                messagebox.showinfo("success","welcome")
                c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                my_cursor=c.cursor()
                messagebox.showinfo("success","welcome2")
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[    self.var_dep.get(),
                                                                                                    self.var_City.get(),
                                                                                                    self.var_year.get(),      
                                                                                                    self.var_Shift.get(),
                                                                                                    self.var_employeeid.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_age.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get()
                                                                                                                          ])
            #                                                                                        # self.var_radio1.get()
            #   
            
                messagebox.showinfo("success","welcome2")                              
                c.commit()
                self.fetch_data()
                c.close()
                print("successfull")
                #messagebox.showinfo("success","employee details has been added successfully",parent=self.root)
            except Exception as es:
                # messagebox.showerror("Error",f"due To :{str(es)}",parent=self.root)
                print(es)

    #**********fetch data ***************
    def fetch_data(self):
          
          conn=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from employee")
          data=my_cursor.fetchall()
          

          if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
          conn.close()

    #=============get curser===============
    def get_cursor(self,event=""):
        Cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(Cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_City.set(data[1]),
        self.var_year.set(data[2]),
        self.var_Shift.set(data[3]),
        self.var_employeeid.set(data[4]),
        self.var_name.set(data[5]),
        self.var_address.set(data[6]),
        self.var_age.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9])

    # #========update function======
    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_employeeid.get()=="":
            messagebox.showerror("Error ", "All the fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","do you want to update this employee details",parent=self.root)
                if update>0:
                    c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                    my_cursor=c.cursor()
                    my_cursor.execute("update employee set Department=%s,City=%s,year=%s,Shift=%s,employeename=%s,employeeaddres=%s,employeeage=%s,email=%s,phone=%s where ,employeeId=%s",[
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_City.get(),
                                                                                                                                                                self.var_year.get(),      
                                                                                                                                                                self.var_Shift.get(),
                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_employeeid.get()
                                                                                                                                                            ])

                else:
                    if not update:
                        return 
                messagebox.showinfo("success","employee details successfully updated completely",parent=self.root)
                c.commit()
                self.fetch_data()
                c.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_employeeid.get()=="":
            messagebox.showerror("error","enployee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee delete page","do you you want to delete this employee",parent=self.root)
                if delete>0:
                     c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                     my_cursor=c.cursor()           
                     sql="delete from employee where employeeId=%s"
                     val=(self.var_employeeid.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                c.commit()
                #self.fetch_data()
                c.close()
                messagebox.showinfo("delete","succesfully delete details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    



    #reset
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_City.set("select City")
        self.var_year.set("select year")
        self.var_Shift.set("select Shift")
        self.var_employeeid.set("")
        self.var_name.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_email.set("")
        self.var_phone.set("")



    #============= Generate data set or take photo samples =================
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_employeeid.get()=="":
            messagebox.showerror("Error ", "All the fields are required",parent=self.root)
        else:
            try:
                c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
                my_cursor=c.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                
                id=0
                for x in myresult:
                    id+=1
                    #print(id)
                    #print(self.var_employeeid.get())
                
                my_cursor.execute("update employee set Department=%s,City=%s,year=%s,Shift=%s,employeename=%s,employeeaddress=%s,employeeage=%s,employeeEmail=%s,employeePhNo=%s where employeeId=%s",[
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_City.get(),
                                                                                                        self.var_year.get(),      
                                                                                                        self.var_Shift.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_age.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_employeeid.get()
                                                                                                    ])    
                print(self.var_employeeid.get())
                c.commit()
                self.fetch_data()
                self.reset_data()
                c.close()


                #============== Load predifined data on face frontals from opencv ===================

                face_classifier=cv2.CascadeClassifier("C:\\Program Files\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # minimum Neighbor=5
                
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
            
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+"k.jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50) ,cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

