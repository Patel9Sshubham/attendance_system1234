from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("face recogniton system")


        # **************variables***********
        self.var_dep=StringVar()
        self.var_Position=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
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

        #current Position
        current_Position_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="current Work information",font=("times new roman ",12,"bold"))
        current_Position_frame.place(x=20,y=120,width=580,height=110)

        #department
        dep_label=Label(current_Position_frame,text="department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        
        dep_combo=ttk.Combobox(current_Position_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"),state="read only",width=17)
        dep_combo["values"]=("select Department","computer","it","civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        

        # Position
        Position_label=Label(current_Position_frame,text="Position",font=("times new roman",12,"bold"),bg="white")
        Position_label.grid(row=0,column=2,padx=10,sticky=W)

        
        Position_combo=ttk.Combobox(current_Position_frame,font=("times new roman",12,"bold"),state="read only",width=17)
        Position_combo["values"]=("select Department","workers","employee","manager","accountant")
        Position_combo.current(0)
        Position_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

                                
        # year
        year_label=Label(current_Position_frame,textvariable=self.var_Position, text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        
        year_combo=ttk.Combobox(current_Position_frame,textvariable=self.var_year, font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)                    
        
         #semester
        semester_label=Label(current_Position_frame,text="semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        
        semester_combo=ttk.Combobox(current_Position_frame,textvariable=self.var_semester, font=("times new roman",12,"bold"),state="read only",width=17)
        semester_combo["values"]=("select sem","1st","2nd","3rd","4th","5th","6th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)   
        

        #company employee information

        company_employee_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="employee information",font=("times new roman ",12,"bold"))
        company_employee_frame.place(x=20,y=240,width=580,height=210)

        #employee ID
        employeeId_label=Label(company_employee_frame,text="employeeId:",font=("times new roman",12,"bold"),bg="white")
        employeeId_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)


        employeeId_entry=ttk.Entry(company_employee_frame,textvariable=self.var_id, width=16,font=("times new roman",12,"bold"))
        employeeId_entry.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        
        #employee Name
        employeeName_label=Label(company_employee_frame, text="employeeName:",font=("times new roman",12,"bold"),bg="white")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        employeeName_entry=ttk.Entry(company_employee_frame,textvariable=self.var_name, width=16,font=("times new roman",12,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=5,pady=2,sticky=W)


        #employee Gender
        employeeGender_label=Label(company_employee_frame,text="employeeGender:",font=("times new roman",12,"bold"),bg="white")
        employeeGender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        employeeGender_entry=ttk.Entry(company_employee_frame,textvariable=self.var_gender ,width=16,font=("times new roman",12,"bold"))
        employeeGender_entry.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        

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
        Radiobtn1=ttk.Radiobutton(company_employee_frame,variable=self.var_radio1 , text="take photo sample",value="yes")
        Radiobtn1.grid(row=6,column=0)

        Radiobtn2=ttk.Radiobutton(company_employee_frame,variable=self.var_radio1, text="No photo sample",value="No")
        Radiobtn2.grid(row=6,column=1)

        #bbuttons frame

        btn_frame=Frame(company_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=135,width=575,height=50)

        
        save_btn=Button(btn_frame,text="save", command=self.add_data, width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take photo sample",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="update photo sample",width=19,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

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
        search_combo["values"]=("select","1st","emp_id","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        search_btn=Button(search_frame,text="show All",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=4)
  
        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=180,width=575,height=240)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","gender","age","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("Position",text="Positions")
        self.employee_table.heading("year",text="year of joining")
        self.employee_table.heading("sem",text="semester")
        self.employee_table.heading("id",text="id")
        self.employee_table.heading("gender",text="gender")
        self.employee_table.heading("age",text="age")
        self.employee_table.heading("email",text="email")
        self.employee_table.heading("phone",text="Phone no")
        self.employee_table.heading("address",text="address")
        self.employee_table.heading("photo",text="photo")
        self.employee_table["show"]="headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("Position",width=100)
        self.employee_table.column("year",width=100)
        self.employee_table.column("sem",width=100)
        self.employee_table.column("id",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("age",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("photo",width=150)

        self.employee_table.pack(fill=BOTH,expand=1)



    #**************function decrelation**********
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_id.get():
            messagebox.showerror("Error ", "All the fields are required",parent=self.root)
        else:
            try:
                #pass
                #messagebox.showeinfo("success","Welcome sir/madam")
                conn=mysql.connector.connect(host="localhost",username="root@localhost",Password="SHpatel@9893",  database="minner")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_Position.get(),
                                                                                                self.var_year.get(),      
                                                                                                self.var_semester.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_age.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_radio1.get(),
                                                                                                self.var_radio2.get()
                                                                                        ))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("success","employee details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due To :{str(es)}",parent=self.root)    

 

if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()