from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np
import mediapipe as mp
import constants

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1570x790+-10+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('icon.ico')

        title_lb = Label(self.root, text="FACE RECOGNITION",font=("times new roman",33,"bold"),bg="blue", fg="white")
        title_lb.place(x=-20, y=1, width=1570 , height=45)

        img_left = Image.open(r"Photos\f3.jpg")
        img_left = img_left.resize((735,750),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lb_left = Label(self.root,image=self.photoimg_left)
        lb_left.place(x=5, y=50, width=735, height=730)

        img_right = Image.open(r"Photos\facerecomain.jpg")
        img_right = img_right.resize((810,730),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        lb_right = Label(self.root,image=self.photoimg_right)
        lb_right.place(x=725, y=50, width=810, height=730)


        b1_1=Button(lb_right,text="Face Recognition",command=self.face_recogn,cursor="hand2",font=("times new roman",18,"bold"),bg="green", fg="white")
        b1_1.place(x=270,y=633,width=290,height=50)

    #===============Attendance==========================
    def mark_attendance(self,i,r,n,d):
        with open("attendance_report/temp.csv",'r+',newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #=================Face recognition===================

    def face_recogn(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=mysql.connector.connect(host=constants.host,username=constants.username,password=constants.password,database="face_recognition")
                my_cursor=con.cursor()

                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)                

                my_cursor.execute("select roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)                


                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                #my_cursor.execute("select student_id from student where student_id="+str(id))
                #i=my_cursor.fetchone()
                i=str(id)                
                


                if confidence>80:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),1)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)            

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        # INITIALIZING OBJECTS
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_face_mesh = mp.solutions.face_mesh

        drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        cap=cv2.VideoCapture(0)

    # DETECT THE FACE LANDMARKS
        with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
            while True:
                success,img=cap.read()
                img=recognize(img,clf,faceCascade)

                # Flip the img horizontally and convert the color space from BGR to RGB
                img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

                # To improve performance
                img.flags.writeable = False
                
                # Detect the face landmarks
                results = face_mesh.process(img)

                # To improve performance
                img.flags.writeable = True

                # Convert back to the BGR color space
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                # Draw the face mesh annotations on the img.
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        mp_drawing.draw_landmarks(
                            image=img,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())

                img = cv2.flip(img, 1)
                # Display the img
                cv2.imshow('MediaPipe FaceMesh', img)
                
                # Terminate the process
                if cv2.waitKey(5) & 0xFF == 13:
                    break

        cap.release()

                







if __name__=="__main__":
    root=Tk()
    obj = Face_recognition(root)
    root.mainloop()     