from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.entry_func)


        main_frame=Frame(self.root,bd=4,bg='sky blue',width=610)
        main_frame.pack()
        
        img_chat=Image.open('b.jpeg')
        img_chat=img_chat.resize((150,70),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,
        compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='dark blue',bg='sky blue')
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=10,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='dark blue',bg='sky blue')
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=ttk.Entry(btn_frame,width=40,font=('time new roman',12,'bold'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)
        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',14,'bold'),width=8,fg='dark blue',bg='sky blue')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        self.clare=Button(btn_frame,text="Clear Data>>",font=('arial',14,'bold'),width=10,fg='dark blue',bg='sky blue')
        self.clare.grid(row=1,column=0,padx=5,sticky=W)
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='dark blue',bg='sky blue')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
        
        
        ########function Declaration####################
        
        
    def entry_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END, '\n'+send) 
        
        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red',bg='white')
        
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red',bg='white')
        
        if(self.entry.get()=='hello'):
           self.text.insert(END, '\n\n'+'Bot:Hii')
        
        elif(self.entry.get()=='hii'):
          self.text.insert(END, '\n\n'+'Bot:hello') 
        
        elif(self.entry.get()=='How are you'):
          self.text.insert(END, '\n\n'+'Bot: fine and you') 
        
        elif(self.entry.get()=='how does face recognition work'):
          self.text.insert(END, '\n\n'+'Bot:Facial recognition works in three steps: \n\n1.detection,\n\n2.analysis,\n\n3.recognition.') 
        
        elif(self.entry.get()=='what is python'):
         self.text.insert(END, '\n\n'+'Bot: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics developed by Guido van Rossum. It was originally released in 1991. Designed to be easy as well as fun, the name "Python" is a nod to the British comedy group Monty Python.') 
       
        elif(self.entry.get()=='what is chatbot'):
         self.text.insert(END, '\n\n'+'Bot: A chatbot communicates similarly to instant messaging. A chatbot is software that simulates human conversations. ') 
       
        elif(self.entry.get()=='What is Machine learning'):
         self.text.insert(END, '\n\n'+'Bot:Machine learning is a subfield of artificial intelligence, which is broadly defined as the capability of a machine to imitate intelligent human behavior. Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.')
       
        elif(self.entry.get()=='thankyou'):
         self.text.insert(END, '\n\n'+'Bot:thankyou for chatting') 
       
        else:
         self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")





if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()