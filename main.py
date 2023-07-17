from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from chatbot import ChatBot
from developer import Developer

class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+-10+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('icon.ico')

        img1 = Image.open(r"Photos\f3.jpg")
        img1 = img1.resize((550,100),Image.ANTIALIAS)
        img1=img1.transpose(Image.FLIP_LEFT_RIGHT)
        #to display img as label, use photoimage()
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root,image=self.photoimg1)
        lb1.place(x=0, y=0, width=550, height=100)


        img2 = Image.open(r"Photos\facerecomain.jpg")
        img2 = img2.resize((550,100),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lb1 = Label(self.root,image=self.photoimg2)
        lb1.place(x=550, y=0, width=500, height=100)


        img3 = Image.open(r"Photos\f3.jpg")
        img3 = img3.resize((550,100),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lb1 = Label(self.root,image=self.photoimg3)
        lb1.place(x=1000, y=0, width=550, height=100)

        
        #background image
        img4 = Image.open(r"Photos\b8.webp")
        img4 = img4.resize((1570,750),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=-20, y=100, width=1570, height=750)

        title_bg = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SOFTWARE",font=("times new roman",33,"bold"),bg="black", fg="yellow")
        title_bg.place(x=20, y=0, width=1570 , height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_bg,font=("times new roman",14,"bold"),bg="black", fg="white")
        lbl.place(x=50,y=0,width=110,height=30)
        time()

    #buttons
        #1 Student 
        img5 = Image.open(r"Photos\Students.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.studend_details,cursor="hand2")
        b1.place(x=150,y=70,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.studend_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=150,y=270,width=220,height=40)


        #2 face detector
        img6 = Image.open(r"Photos\face_detector.png")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b2.place(x=470,y=70,width=220,height=220)
        b2_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b2_1.place(x=470,y=270,width=220,height=40)

        
        #3 attendance 
        img7 = Image.open(r"Photos\attendance.jpeg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,command=self.attendance_data,cursor="hand2")
        b3.place(x=790,y=70,width=220,height=220)
        b3_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b3_1.place(x=790,y=270,width=220,height=40)


        #4 Help Desk
        img8 = Image.open(r"Photos\Help_desk2.png")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8,command=self.chatbot_work,cursor="hand2")
        b4.place(x=1110,y=70,width=220,height=220)
        b4_1=Button(bg_img,text="Help Desk",command=self.chatbot_work,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b4_1.place(x=1110,y=270,width=220,height=40)


        #5 Train Data
        img9 = Image.open(r"Photos\face_detector2.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b5.place(x=150,y=350,width=220,height=220)
        b5_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b5_1.place(x=150,y=550,width=220,height=40)


        #6 Photos
        img10 = Image.open(r"Photos\photos.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=470,y=350,width=220,height=220)
        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b6_1.place(x=470,y=550,width=220,height=40)


        #7 developers
        img11 = Image.open(r"Photos\developer.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,command=self.developer_work,cursor="hand2")
        b7.place(x=790,y=350,width=220,height=220)
        b7_1=Button(bg_img,text="Developers",command=self.developer_work,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b7_1.place(x=790,y=550,width=220,height=40)



        #8 Exit
        img12 = Image.open(r"Photos\exit.jpg")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8=Button(bg_img,image=self.photoimg12,command=self.iexit,cursor="hand2")
        b8.place(x=1110,y=350,width=220,height=220)
        b8_1=Button(bg_img,text="Exit",command=self.iexit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b8_1.place(x=1110,y=550,width=220,height=40)


    def open_img(self):
        os.startfile('data')

    def iexit(self):
        self.iexit=messagebox.askyesno("Face Recognition","Are you sure want to exit this program?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    #=====================Functtion Button=======================================

    def studend_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def chatbot_work(self):
        self.new_window = Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def developer_work(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)


#calling main
if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()