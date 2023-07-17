from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
from main import Face_Recognition_System
import constants


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Login")
        self.root.wm_iconbitmap('icon.ico')

        img1 = Image.open(r"Photos\f3.jpg")
        img1 = img1.resize((550,150),Image.ANTIALIAS)
        img1=img1.transpose(Image.FLIP_LEFT_RIGHT)
        #to display img as label, use photoimage()
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root,image=self.photoimg1)
        lb1.place(x=0, y=0, width=550, height=150)

        img2 = Image.open(r"Photos\facerecomain.jpg")
        img2 = img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lb1 = Label(self.root,image=self.photoimg2)
        lb1.place(x=550, y=0, width=550, height=150)


        img3 = Image.open(r"Photos\f3.jpg")
        img3 = img3.resize((550,150),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lb1 = Label(self.root,image=self.photoimg3)
        lb1.place(x=1100, y=0, width=550, height=150)

        
        #background image
        img4 = Image.open(r"Photos\b3.png")
        img4 = img4.resize((1550,692),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0, y=150, relwidth=1,relheight=1)

        title_bg = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SOFTWARE",font=("times new roman",33,"bold"),bg="black", fg="yellow")
        title_bg.place(x=-5, y=0, width=1550 , height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_bg,font=("times new roman",14,"bold"),bg="black", fg="white")
        lbl.place(x=50,y=0,width=110,height=30)
        time()

        frame=Frame(self.root,bg='black')
        frame.place(x=600,y=250,width=340,height=450)

        img5 = Image.open("Photos/login6.png")
        img5 = img5.resize((100,100),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lg_img = Label(frame,image=self.photoimg5,bg="black",borderwidth=0)
        lg_img.place(x=122, y=3, width=100,height=100)

        get_str=Label(frame,text="Get Started",font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=96,y=103)

    #label
        username_lb=Label(frame,text="Username",font=('times new roman',15,'bold'),fg='white',bg='black')
        username_lb.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.textuser.place(x=40,y=185,width=270)

        password_lb=Label(frame,text="Password",font=('times new roman',15,'bold'),fg='white',bg='black')
        password_lb.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtpass.config(show="*")
        self.txtpass.place(x=40,y=260,width=270)

    #icon image
        img6 = Image.open("Photos/login7.png")
        img6 = img6.resize((28,28),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lg_img = Label(frame,image=self.photoimg6,bg="black",borderwidth=0)
        lg_img.place(x=40, y=155, width=28,height=28)

        img7 = Image.open("Photos/login5.png")
        img7 = img7.resize((25,25),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        lg_img = Label(frame,image=self.photoimg7,bg="black",borderwidth=0)
        lg_img.place(x=40, y=231, width=25,height=25)
    #buttons
        #login
        loginbt=Button(frame,text='Login',font=('times new roman',15,'bold'),command=self.login,bd=3,relief=RIDGE,fg='white',bg='darkblue',activeforeground='white',activebackground='red')
        loginbt.place(x=110,y=300,width=120,height=35)

        
        #forgot password
        forgotbt=Button(frame,text='Forgot Password?',command=self.forgot_password,font=('times new roman',13,'bold'),borderwidth=0,relief=RIDGE,fg='red',bg='black',activeforeground='red',activebackground='black')
        forgotbt.place(x=94,y=338,width=160)

        #register
        registerbt=Button(frame,text='New User Register',command=self.register_window,font=('times new roman',13,'bold'),borderwidth=0,relief=RIDGE,fg='white',bg='blue',activeforeground='white',activebackground='blue')
        registerbt.place(x=90,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.textuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required !!")

        else:
            con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
            my_cursor=con.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                                                                                            self.textuser.get(),
                                                                                            self.txtpass.get()                    
                                                                                       ))

            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Username Or Password")
            else:
                open_main=messagebox.askyesno("Ask","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            con.commit()
            con.close()

    #==================reset password==========
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter Security Answer",parent=self.root2)
        elif self.txt_new_password=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
            my_cursor=con.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.textuser.get())
                my_cursor.execute(query,value)

                con.commit()
                con.close()
                messagebox.showinfo("Success","Your password has been reset",parent=self.root2)
                self.root2.destroy()

    #==========forgot password window=================
    def forgot_password(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
            my_cursor=con.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+490+210")

                
                frame=Frame(self.root2,bg='white',bd=8,relief=RIDGE)
                frame.place(x=5,y=0,width=330,height=440)

                lb=Label(frame,text="Forgot Password",font=("times new roman",20,'bold'),fg='red',bg='white')
                lb.place(x=0,y=0,relwidth=1)

                security_Q=Label(frame,text="Select Security Question",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_Q.place(x=30,y=80)
                self.combo_security_Q=ttk.Combobox(frame,font=('times new roman',15),state='readonly')
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=30,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(frame,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_A.place(x=30,y=150)
                self.txt_security_A=ttk.Entry(frame,font=('times new roman',15))
                self.txt_security_A.place(x=30,y=180,width=250)

                new_password=Label(frame,text="New Password",font=('times new roman',15,'bold'),bg='white',fg='black')
                new_password.place(x=30,y=220)
                self.txt_new_password=ttk.Entry(frame,font=('times new roman',15))
                self.txt_new_password.config(show="*")
                self.txt_new_password.place(x=30,y=250,width=250)

                btn=Button(frame,text='Reset',command=self.reset_password,font=('new times roman',17,'bold'),bd=3,relief=RIDGE,fg='white',bg='green',activebackground='green',activeforeground='white')
                btn.place(x=110,y=290)



class Register:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+-10+0")
        self.root.title("Register")

        #===================variables===============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confirm_pass=StringVar()

        #============images======================

        img1 = Image.open(r"Photos\f3.jpg")
        img1 = img1.resize((550,150),Image.ANTIALIAS)
        img1=img1.transpose(Image.FLIP_LEFT_RIGHT)
        #to display img as label, use photoimage()
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lb1 = Label(self.root,image=self.photoimg1)
        lb1.place(x=0, y=0, width=550, height=150)

        img2 = Image.open(r"Photos\facerecomain.jpg")
        img2 = img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lb1 = Label(self.root,image=self.photoimg2)
        lb1.place(x=550, y=0, width=550, height=150)


        img3 = Image.open(r"Photos\f3.jpg")
        img3 = img3.resize((550,150),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lb1 = Label(self.root,image=self.photoimg3)
        lb1.place(x=1100, y=0, width=550, height=150)

        #background image
        img4 = Image.open(r"Photos\b3.png")
        img4 = img4.resize((1550,692),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0, y=150, relwidth=1,relheight=1)

        title_bg = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SOFTWARE",font=("times new roman",33,"bold"),bg="black", fg="yellow")
        title_bg.place(x=-5, y=0, width=1550 , height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_bg,font=("times new roman",14,"bold"),bg="black", fg="white")
        lbl.place(x=50,y=0,width=110,height=30)
        time()

        img_left = Image.open(r"Photos\register2.jpg")
        img_left = img_left.resize((470,480),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        left_img = Label(bg_img,image=self.photoimg_left)
        left_img.place(x=129, y=80, width=470,height=480)

    #main frame
        s_frame=Frame(bg_img,bg='white',bd=8,relief=RIDGE)
        s_frame.place(x=600,y=80,width=700,height=90)

        frame=Frame(bg_img,bg='white',bd=8,relief=RIDGE)
        frame.place(x=600,y=170,width=700,height=388)

        register_lb=Label(s_frame,text="REGISTER HERE",font=('times new roman',40,'bold'),bg='white',fg='green')
        register_lb.place(x=100,y=10)

        #==============labels and entry=================
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),bg='white',fg='black')
        fname.place(x=50,y=10)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        self.fname_entry.place(x=50,y=40,width=250)

        lname=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg='white',fg='black')
        lname.place(x=370,y=10)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15,'bold'))
        self.txt_lname.place(x=370,y=40,width=250)

        contact=Label(frame,text="Contact No.",font=('times new roman',15,'bold'),bg='white',fg='black')
        contact.place(x=50,y=80)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',15))
        self.txt_contact.place(x=50,y=110,width=250)

        email=Label(frame,text="Email",font=('times new roman',15,'bold'),bg='white',fg='black')
        email.place(x=370,y=80)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',15))
        self.txt_lname.place(x=370,y=110,width=250)

        security_Q=Label(frame,text="Select Security Question",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_Q.place(x=50,y=150)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman',15),state='readonly')
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=180,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_A.place(x=370,y=150)
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=('times new roman',15))
        self.txt_security_A.place(x=370,y=180,width=250)

        password=Label(frame,text="Password",font=('times new roman',15,'bold'),bg='white',fg='black')
        password.place(x=50,y=220)
        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=('times new roman',15))
        self.txt_password.config(show="*")
        self.txt_password.place(x=50,y=250,width=250)

        confirm_password=Label(frame,text="Confirm Password",font=('times new roman',15,'bold'),bg='white',fg='black')
        confirm_password.place(x=370,y=220)
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_pass,font=('times new roman',15))
        self.txt_confirm_password.config(show="*")
        self.txt_confirm_password.place(x=370,y=250,width=250)

        #================check button===========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=('times new roman',12,"bold"),bg='white',onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=290)

        img5 = Image.open(r"Photos\register.jpg")
        img5 = img5.resize((250,55),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(frame,image=self.photoimg5,command=self.register_data,borderwidth=0,cursor='hand2',font=('times new roman',12,"bold"),bg='white')
        b1.place(x=35,y=315,width=250)

        img6 = Image.open(r"Photos\loginnow.jpg")
        img6 = img6.resize((225,40),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1=Button(frame,image=self.photoimg6,command=self.return_login,borderwidth=0,cursor='hand2',font=('times new roman',12,"bold"),bg='white')
        b1.place(x=370,y=317,width=225)

    #==========function=============

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_pass.get()=="" or self.var_confirm_pass.get()=="" or self.var_securityA.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_securityQ=="Select":
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)

        elif self.var_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)

        elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)

        else:
            con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
            my_cursor=con.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row!=None:
                messagebox.showerror("Error","User already exist , try another email")
            
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),                                                                                  
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                      ))

                con.commit()
                con.close()
                messagebox.showinfo("Success","Successfully Registered",parent=self.root)


    def return_login(self):
        self.root.destroy()



#calling main
if __name__=="__main__":
    main()





