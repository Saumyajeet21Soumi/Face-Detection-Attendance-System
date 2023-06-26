import tkinter
from tkinter import* 
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import student
from train import train
from face_recognization import face_reconization
from attendance import attendance



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\1_REkyBlBoacF-qn65zhIzVg.jpg")
        img=img.resize((500,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=250)

        #second image
        img1=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\R.png")
        img1=img1.resize((500,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=250)

        #third image
        img2=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\bigstock-Face-Detection-And-Recognition-194513554.jpg")
        img2=img2.resize((500,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=250)

        #bg change
        img3=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\technology-binary-numbers-code-wallpaper-preview.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=250,width=1530,height=790)

  
        title_lbl=Label(bg_img,text="FACE RECOGNITION & ATTENDANCE SYSTEM SOWFWARE",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\D430_50_073_1200.jpg")
        img4=img4.resize((190,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=90,width=190,height=190)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=150,y=270,width=190,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\recog.jpg")
        img5=img5.resize((190,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=90,width=190,height=190)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=400,y=270,width=190,height=40)

        #attendance system
        img6=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\Attendance-banner-07.png")
        img6=img6.resize((190,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=90,width=190,height=190)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=680,y=270,width=190,height=40)

        #train data
        img7=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\OIP (4).jpeg")
        img7=img7.resize((190,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=950,y=90,width=190,height=190)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=950,y=270,width=190,height=40)

        #photos
        img9=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\3934a03adf47472d834c0689320e2090.jpg")
        img9=img9.resize((190,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=1200,y=90,width=190,height=190)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1200,y=270,width=190,height=40)

        #exit
        img8=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\va-code-exit-sign-nhe-15973_1000.gif")
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.exit)
        b1.place(x=690,y=320,width=170,height=170)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=690,y=490,width=170,height=40)


    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return    


    #  Functions Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_reconization(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)




if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()