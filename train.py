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
        self.root.geometry("1570x790+-10+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('icon.ico')

        title_lb = Label(self.root, text="TRAIN  DATA  SET",font=("times new roman",33,"bold"),bg="cyan", fg="darkblue")
        title_lb.place(x=-10, y=1, width=1570 , height=60)

        img_top = Image.open(r"Photos\train.jpg")
        img_top = img_top.resize((1570,260),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        lb_top = Label(self.root,image=self.photoimg_top)
        lb_top.place(x=-10, y=60, width=1570, height=260)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red", fg="white")
        b1_1.place(x=-10,y=300,width=1570,height=60)

        img_bot = Image.open(r"Photos\faces3.jpg")
        img_bot = img_bot.resize((1570,450),Image.ANTIALIAS)
        self.photoimg_bot = ImageTk.PhotoImage(img_bot)
        lb_bot = Label(self.root,image=self.photoimg_bot)
        lb_bot.place(x=-10, y=360, width=1570, height=450)


    def train_classifier(self):
        data_dir=("data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')    #grayscale image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #===============train Classifier===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed !!!",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()     