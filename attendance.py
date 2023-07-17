from os import pardir
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1570x790+-10+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('icon.ico')
        
        #======variables====================
        self.var_dep= StringVar()
        self.var_stu_id= StringVar()
        self.var_stu_name= StringVar()
        self.var_roll= StringVar()
        self.var_date= StringVar()
        self.var_time= StringVar()
        self.var_dep= StringVar()
        self.var_attend= StringVar()

        img1 = Image.open(r"Photos\a16.jpg")
        img1 = img1.resize((550,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root,image=self.photoimg1)
        lb1.place(x=0, y=0, width=550, height=150)


        img2 = Image.open(r"Photos\a17.jpg")
        img2 = img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lb1 = Label(self.root,image=self.photoimg2)
        lb1.place(x=550, y=0, width=550, height=150)


        img3 = Image.open(r"Photos\a13.jpg")
        img3 = img3.resize((550,150),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lb1 = Label(self.root,image=self.photoimg3)
        lb1.place(x=1100, y=0, width=550, height=150)



       
    #background
        img4 = Image.open(r"Photos\background.jpg")
        img4 = img4.resize((1570,700),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=-10, y=150, width=1570, height=700)

        title_bg = Label(bg_img, text="Attendance Management System",font=("times new roman",33,"bold"),bg="red", fg="white")
        title_bg.place(x=-10, y=1, width=1570 , height=45)

        #main frame
        frame = Frame(bg_img,bd=2,bg='white')
        frame.place(x=20,y=50,width=1515,height=600)

#left label frame
        Left_frame=LabelFrame(frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("new time romans",12,"bold"))
        Left_frame.place(x=5, y=-3, width=730, height=580)

        img_left = Image.open(r"Photos\attendance2.jpg")
        img_left = img_left.resize((720,220),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lb_left = Label(Left_frame,image=self.photoimg_left)
        lb_left.place(x=2, y=-2, width=720, height=220)

        left_in_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg='white')
        left_in_frame.place(x=3,y=220,width=720,height=330)

    #label and entry
    #attendanceId
        attendanceID_label=Label(left_in_frame,text="Student ID :",font=("new time romans",13,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_stu_id,font=("new time romans",13))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

    #student roll
        roll_label=Label(left_in_frame,text="Roll :",font=("new time romans",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        atten_roll=ttk.Entry(left_in_frame,width=20,textvariable=self.var_roll,font=("new time romans",13))
        atten_roll.grid(row=0,column=3,padx=10,pady=10,sticky=W)

    #name
        name_label=Label(left_in_frame,text="Student Name :",font=("new time romans",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        atten_name=ttk.Entry(left_in_frame,width=20,textvariable=self.var_stu_name,font=("new time romans",13))
        atten_name.grid(row=1,column=1,padx=10,pady=10,sticky=W)

    #department
        dep_label=Label(left_in_frame,text="Department :",font=("new time romans",13,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        atten_dep=ttk.Entry(left_in_frame,width=20,textvariable=self.var_dep,font=("new time romans",13))
        atten_dep.grid(row=1,column=3,padx=10,pady=10,sticky=W)

    #time
        time_label=Label(left_in_frame,text="Time :",font=("new time romans",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        atten_time=ttk.Entry(left_in_frame,width=20,textvariable=self.var_time,font=("new time romans",13))
        atten_time.grid(row=2,column=1,padx=10,pady=10,sticky=W)

    #date
        date_label=Label(left_in_frame,text="Date :",font=("new time romans",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        atten_date=ttk.Entry(left_in_frame,width=20,textvariable=self.var_date,font=("new time romans",12))
        atten_date.grid(row=2,column=3,padx=10,pady=10,sticky=W)

    #attendance
        atten_label=Label(left_in_frame,text="Attendance Status :",font=("new time romans",13,"bold"),bg="white")
        atten_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(left_in_frame,font=("new time romans",12),width=16,textvariable=self.var_attend,state='readonly')
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)

    #button Frame
        btn_frame=Frame(left_in_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=3,y=190,width=710,height=130)

        Import_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=55,font=("new time romans",16,"bold"),bg="blue",fg='white',cursor="hand2")
        Import_btn.grid(row=0,column=0)

        Export_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=55,font=("new time romans",16,"bold"),bg="blue",fg='white',cursor="hand2")
        Export_btn.grid(row=1,column=0)

        #Update_btn=Button(btn_frame,text="Update",width=16,font=("new time romans",12,"bold"),bg="blue",fg='white')
        #Update_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",width=55,command=self.reset_data,font=("new time romans",16,"bold"),bg="blue",fg='white',cursor="hand2")
        Reset_btn.grid(row=2,column=0)








#right label frame
        Right_frame=LabelFrame(frame,bd=2,bg="white", relief=RIDGE, text="Attendance Details", font=("new time romans",12,"bold"))
        Right_frame.place(x=740, y=-3, width=770, height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=760,height=560)


        #==============scroll bar =====================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #===============fetch data=============================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    
    #import csv
    def importCSV(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA","No DATA found to export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fin)+"successfully",parent=self.root)

            f = open("attendance_report/temp.csv", "w")
            f.truncate()
            f.close()

        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']

        self.var_stu_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_stu_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attend.set(rows[6])


    def reset_data(self):
        self.var_stu_id.set("")
        self.var_roll.set("")
        self.var_stu_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("")


if __name__=="__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()