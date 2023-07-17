from os import pardir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import constants

class Student:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1570x790+-10+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('icon.ico')
        
        #================variable====================
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_sem= StringVar()
        self.var_stu_id= StringVar()
        self.var_stu_name= StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()
        self.var_btn1=StringVar()

        self.var_stu_id_seach= StringVar()


    #top
        img1 = Image.open(r"Photos\a9.jpg")
        img1 = img1.resize((550,120),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root,image=self.photoimg1)
        lb1.place(x=0, y=0, width=550, height=120)


        img2 = Image.open(r"Photos\a7.jpg")
        img2 = img2.resize((550,120),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lb1 = Label(self.root,image=self.photoimg2)
        lb1.place(x=550, y=0, width=550, height=120)


        img3 = Image.open(r"Photos\a8.jpg")
        img3 = img3.resize((550,120),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lb1 = Label(self.root,image=self.photoimg3)
        lb1.place(x=1100, y=0, width=550, height=120)


    #background
        img4 = Image.open(r"Photos\background.jpg")
        img4 = img4.resize((1570,750),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=-10, y=120, width=1570, height=750)

        title_bg = Label(bg_img, text="Student Management System",font=("times new roman",33,"bold"),bg="red", fg="white")
        title_bg.place(x=-10, y=1, width=1570 , height=45)

#main frame(no text)
        frame = Frame(bg_img,bd=2,bg='white')
        frame.place(x=30,y=50,width=1500,height=650)


#left label frame
        Left_frame=LabelFrame(frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("new time romans",12,"bold"))
        Left_frame.place(x=10, y=-3, width=710, height=606)

        img_left = Image.open(r"Photos\attendance2.jpg")
        img_left = img_left.resize((698,150),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lb_left = Label(Left_frame,image=self.photoimg_left)
        lb_left.place(x=2, y=-2, width=698, height=150)

    #current course
        cc_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current course information", font=("new time romans",12,"bold"))
        cc_frame.place(x=2, y=150, width=698, height=120)

        #department
        dep_label=Label(cc_frame,text="Department",font=("new time romans",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("new time romans",12,"bold"),width=20,state='readonly')
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=5,sticky=W)

        #course
        course_label=Label(cc_frame,text="Course",font=("new time romans",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("new time romans",12,"bold"),width=20,state='readonly')
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=5)


        #year
        year_label=Label(cc_frame,text="year",font=("new time romans",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("new time romans",12,"bold"),width=20,state='readonly')
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=5,sticky=W)


        #semester
        semester_label=Label(cc_frame,text="semester",font=("new time romans",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(cc_frame,textvariable=self.var_sem,font=("new time romans",12,"bold"),width=20,state='readonly')
        semester_combo["values"]=("Select semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=3,pady=5,sticky=W)


    #class student info
        Student_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Student Information", font=("new time romans",12,"bold"))
        Student_frame.place(x=2, y=270, width=698, height=310)

        #studentId
        StudentID_label=Label(Student_frame,text="StudentID :",font=("new time romans",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        StudentID_entry=ttk.Entry(Student_frame,textvariable=self.var_stu_id,width=18,font=("new time romans",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=7,sticky=W)


        #student name
        StudentName_label=Label(Student_frame,text="Student Name :",font=("new time romans",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=7,sticky=W)

        StudentName_entry=ttk.Entry(Student_frame,textvariable=self.var_stu_name,width=18,font=("new time romans",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=7,sticky=W)


        #class division
        Division_label=Label(Student_frame,text="Division :",font=("new time romans",12,"bold"),bg="white")
        Division_label.grid(row=1,column=0,padx=10,pady=7,sticky=W)

        Division_combo=ttk.Combobox(Student_frame,textvariable=self.var_div,font=("new time romans",12),width=16,state='readonly')
        Division_combo["values"]=("Select Division","A","B","C","D")
        Division_combo.current(0)
        Division_combo.grid(row=1,column=1,padx=10,pady=7,sticky=W)

        

        #Roll no
        Roll_no_label=Label(Student_frame,text="Roll No :",font=("new time romans",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=7,sticky=W)

        Roll_no_entry=ttk.Entry(Student_frame,width=18,textvariable=self.var_roll,font=("new time romans",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=7,sticky=W)


        #gender
        Gender_label=Label(Student_frame,text="Gender :",font=("new time romans",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=7,sticky=W)

        Gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=("new time romans",12),width=16,state='readonly')
        Gender_combo["values"]=("Select Gender","Male","Female","Others")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=7,sticky=W)



        #DOB
        Dob_label=Label(Student_frame,text="DOB :",font=("new time romans",12,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=10,pady=7,sticky=W)

        Dob_entry=ttk.Entry(Student_frame,textvariable=self.var_dob,width=18,font=("new time romans",12))
        Dob_entry.grid(row=2,column=3,padx=10,pady=7,sticky=W)


        #email
        Email_label=Label(Student_frame,text="Email :",font=("new time romans",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=7,sticky=W)

        Email_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=18,font=("new time romans",12))
        Email_entry.grid(row=3,column=1,padx=10,pady=7,sticky=W)


        #Phone No
        Phone_label=Label(Student_frame,text="Phone No:",font=("new time romans",12,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=7,sticky=W)

        Phone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=18,font=("new time romans",12))
        Phone_entry.grid(row=3,column=3,padx=10,pady=7,sticky=W)


        #Address
        Address_label=Label(Student_frame,text="Address :",font=("new time romans",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=7,sticky=W)

        Address_entry=ttk.Entry(Student_frame,textvariable=self.var_address,width=18,font=("new time romans",12))
        Address_entry.grid(row=4,column=1,padx=10,pady=7,sticky=W)


        #Teacher Name
        Teacher_label=Label(Student_frame,text="Teacher Name :",font=("new time romans",12,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=7,sticky=W)

        Teacher_entry=ttk.Entry(Student_frame,textvariable=self.var_teacher,width=18,font=("new time romans",12))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=7,sticky=W)


    #radio Buttons
        
        btn1 = ttk.Radiobutton(Student_frame,variable=self.var_btn1,text="Take a Photo Sample",value="yes")
        btn1.grid(row=5,column=0)
        btn2 = ttk.Radiobutton(Student_frame,variable=self.var_btn1,text="No Photo Sample",value="no")
        btn2.grid(row=5,column=1)

    #button Frame
        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=2,y=215,width=690,height=36)

        Save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Reset_btn.grid(row=0,column=3)


        btn_frame2=Frame(Student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame2.place(x=2,y=245,width=690,height=32)

        Take_Photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",width=34,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Take_Photo_btn.grid(row=0,column=0)
        Update_Photo_btn=Button(btn_frame2,text="Update Photo Sample",command=self.generate_dataset,width=34,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Update_Photo_btn.grid(row=0,column=1)






#right label frame
        Right_frame=LabelFrame(frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("new time romans",12,"bold"))
        Right_frame.place(x=730, y=-3, width=760, height=606)

        img_right = Image.open(r"Photos\a2.jpg")
        img_right = img_right.resize((750,150),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        lb_right = Label(Right_frame,image=self.photoimg_right)
        lb_right.place(x=2, y=-2, width=750, height=150)

        #=================search system+=============
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white", relief=RIDGE, text="Search System", font=("new time romans",12,"bold"))
        Search_frame.place(x=3, y=150, width=750, height=70)

        Search_label=Label(Search_frame,text="Search By:",font=("new time romans",12,"bold"),bg="red",fg='white')
        Search_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("new time romans",12,"bold"),width=12,state='readonly')
        Search_combo["values"]=("Select","Student ID")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=3,pady=7,sticky=W)

        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_stu_id_seach,width=14,font=("new time romans",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=5,pady=7,sticky=W)

        Search_btn=Button(Search_frame,text="Search",command=self.search_data,width=12,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Search_btn.grid(row=0,column=3,padx=4)

        Show_All_btn=Button(Search_frame,text="Show All",command=self.fetch_data,width=12,font=("new time romans",12,"bold"),bg="blue",fg='white')
        Show_All_btn.grid(row=0,column=4)


    #==========Table Frame===================

        Table_frame=Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
        Table_frame.place(x=3, y=220, width=750, height=360)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #====================function===========================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id=="" or self.var_roll=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
                my_cursor=con.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_stu_id.get(),
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_btn1.get()
                                                                                                            ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Student detail has been added Successfully",parent=self.root)        

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #=====================fetch====================================
    def fetch_data(self):
        con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
        my_cursor=con.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())        
            for i in data :
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()

    #=====================search====================================
    def search_data(self):
        con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
        my_cursor=con.cursor()
        # self.student_table.delete(*self.student_table.get_children())
        query=("select * from student where student_id=%s")
        value=(self.var_stu_id_seach.get(),)
        my_cursor.execute(query,value)
        data = my_cursor.fetchall()

        if data!=None:
            self.student_table.delete(*self.student_table.get_children())        
            for i in data :
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()
    #==================================get cursor======================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_btn1.set(data[14])
        
    #==========update func===============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stu_id=="" or self.var_roll=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update >0:
                    con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
                    my_cursor=con.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_stu_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_btn1.get(),
                                                                                                                                                                                                                    self.var_stu_id.get()
                                                                                                                                                                                                                ))

                else:
                    if not Update:
                        return  
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)                                                                                                                                                                                              
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #==========delete func=============
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
                    my_cursor=con.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return  
                messagebox.showinfo("Success","Student details successfully Deleted",parent=self.root)                                                                                                                                                                                              
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #===================reset===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_btn1.set("")


    #===============Take photo sample=======================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stu_id=="" or self.var_roll=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
                my_cursor=con.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=str(self.var_stu_id.get())
                #for x in myresult:
                #    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_stu_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_btn1.get(),
                                                                                                                                                                                                                    self.var_stu_id.get()==id
                                                                                                                                                                                                                ))
                con.commit()
                self.fetch_data()
                self.reset_data()
                con.close()

                #====================Load predifined data or face frontals from opencv============

                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    
                    #scaling factor =1.3
                    #min neighbour =5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 & 0xff or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            


if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()