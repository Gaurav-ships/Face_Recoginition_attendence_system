from cProfile import label
from tkinter import *
import os
import tkinter
from tkinter import ttk
from time import strftime
from datetime import datetime

from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
from help import Help

class Face_Recoginition_System:
    #constructor call
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogintion System")
        
        #first image
        img=Image.open(r"Images_GUI\gra3.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg=ImageTk.PhotoImage(img)
        
        f1=Label(self.root,image=self.photoimg)
        f1.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\Dell\Desktop\fa\images\1.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f1=Label(self.root,image=self.photoimg1)
        f1.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"Images_GUI\gra2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f1=Label(self.root,image=self.photoimg2)
        f1.place(x=1000,y=0,width=550,height=130)
        
        
         #background image
        img3=Image.open(r"Images_GUI\gra1.jpg")
        img3=img3.resize((1530,790),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="FACE RECOGINITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000,time)
            
        lb1=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="green")
        lb1.place(x=0,y=0,width=110,height=50)
        time()
        
        #student button
        img4=Image.open(r"Images_GUI\std1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg4=ImageTk. PhotoImage(img4 )
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2") 
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #Detect button
        img5=Image.open(r"Images_GUI\f_det.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data) 
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
         #Attendence button
        img6=Image.open(r"Images_GUI\banner1.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data) 
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        #Help desk button
        img7=Image.open(r"Images_GUI\hlp.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help_data) 
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        #Train Face button
        img8=Image.open(r"Images_GUI\f_bg.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data) 
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
         #photo Face button
        img9=Image.open(r"Images_GUI\banner.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img) 
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
         #Devloper button
        img10=Image.open(r"Images_GUI\dev.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Developer_data) 
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Devloper",cursor="hand2",command=self.Developer_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
         #Exit button
        img11=Image.open(r"Images_GUI\exi.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exit) 
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
     
    def open_img(self):
        os.startfile("data_img")   
        #Function buttons
    
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
    
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    
    def Developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)
  
        
           
        
    def Help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)
  
        
    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Recoginition","Are you sure to exit",parent=self.root)
        if self.Exit>0:
            self.root.destroy()
        else:
            return  
   
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recoginition_System(root)
    root.mainloop()        