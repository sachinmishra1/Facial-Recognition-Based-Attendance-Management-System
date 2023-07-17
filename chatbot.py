from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.wm_iconbitmap('icon.ico')
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img = Image.open(r"Photos\chatbot.jpg")
        img = img.resize((200,70),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        lb = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        lb.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        #self.scroll_y.config(command=self.yview)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="clear Data",command=self.clear_func,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)



    #=====================function declaration===============\

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def clear_func(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\n\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')

        if(self.entry.get()=='Hello' or self.entry.get()=='Hi' ):
            self.text.insert(END,'\n\n'+'Bot: Hello Sir')

        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine and You ?')
  
        elif(self.entry.get()=='Good' or self.entry.get()=='Fine' or self.entry.get()=='Fantastic' ):
            self.text.insert(END,'\n\n'+'Bot: Nice to Hear Sir !!')
        
        elif(self.entry.get()=='Creator?' or self.entry.get()=='Who created you?' or self.entry.get()=='owner?' ):
            self.text.insert(END,'\n\n'+'Bot: Mr.Ritik Jain created me using pyhton')

        elif(self.entry.get()=='Your name?' or self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr. Rockxxy')

        elif(self.entry.get()=='Nice to meet you'):
            self.text.insert(END,'\n\n'+'Bot: Nice to meet you too Sir')

        elif(self.entry.get()=='Any contact of your creator?' or self.entry.get()=='How to contact your creator?'):
            self.text.insert(END,'\n\n'+'Bot: His email ID : ritikjain10159@gmail.com , sachinmishra@gmail.com')
            self.text.insert(END,'\n\n'+'Bot: His contact no : 9811102497')
        
        elif(self.entry.get()=='Tell me something about this project' or self.entry.get()=='Tell something about this project'):
            self.text.insert(END,'\n\n'+'Bot: This is a Facial Recognition Smart Attendance Software using machine learning')

        elif(self.entry.get()=='bye' or self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Thanks for chatting Sir')

        elif(self.entry.get()=='What is machine learning?'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning (ML) is the study of computer\nalgorithms that can improve automatically through \nexperience and by the use of data. It is seen\nas a part of artificial intelligence. Machine learning \nalgorithms build a model based on sample data,\nknown as "training data", in order to make predictions\nor decisions without being explicitly programmed to do so.')

        elif(self.entry.get()=='How does face recognition works?' or self.entry.get()=='What is face recognition?'):
            self.text.insert(END,'\n\n'+'Bot: Facial Recognition is a way of\nrecognizing a human face through\ntechnology.A facial recognition\nsytem uses biometrics to map\nfacial features from a photograph\nor video. It compares the information\nwith a database of known faces to find\na match.')

        elif(self.entry.get()=='How many languages you can speak?' or self.entry.get()=='Can you speak English?'):
            self.text.insert(END,'\n\n'+'Bot: I can only speak English')
        
        elif(self.entry.get()=='What is chatbot?'):
            self.text.insert(END,'\n\n'+'Bot: A chatbot is a software application\nused to conduct an on-line chat conversation\nvia text or text-to-speech, in lieu of\nproviding direct contact with a live human agent.')

        elif(self.entry.get()=='How many countries uses facial recognition?'):
            self.text.insert(END,'\n\n'+'Bot: There are 109 countries today\nthat are either using or have approved\nthe use of facial recognition technology\nfor surveillance purposes.')




        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry I did not get it')
        


            
        
        
        


if __name__=="__main__":
    root=Tk()
    obj = ChatBot(root)
    root.mainloop()     