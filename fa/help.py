from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import os
import numpy as np

class Help:
    #constructor call
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogintion System")
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img_top=Image.open(r"Images_GUI\hlp.jpg")
        img_top=img_top.resize((1530,790),Image.Resampling.LANCZOS) #converst high level image to low level
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1530,height=790)
        
        dep_label=Label(f_lb1,text="Email:gsengar263@gmail.com",font=("times new roman",50,"bold"),bg="white",fg="green")
        dep_label.place(x=400,y=260)
        
        
   
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()   