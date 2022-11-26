from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import os
import numpy as np

class Developer:
    #constructor call
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogintion System")
        
        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open(r"Images_GUI\dev.jpg")
        img_top=img_top.resize((1530,790),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=790)
           
          
        main_frame=Frame(f_lb1,bd=2)
        main_frame.place(x=1050,y=0,width=500,height=100)
        
        img_top1=Image.open(r"Images_GUI\gaurav.jpeg")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lb1=Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=300,y=0,width=200,height=200)
        
        #devloper info   
        dep_label=Label(main_frame,text="Hello My name is Gaurav Sengar",font=("times new roman",12,"bold"),bg="white",fg="green")
        dep_label.place(x=0,y=5)
        dep_label=Label(main_frame,text="I am a Software Developer",font=("times new roman",12,"bold"),bg="white",fg="green")
        dep_label.place(x=0,y=40)
        
        
      
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        