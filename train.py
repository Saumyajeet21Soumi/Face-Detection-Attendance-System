from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        bg_img=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\1614776.webp")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=50,width=1530,height=790)

        b1_1=Button(self.root,text="TAP TO TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=440,width=1530,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #greyscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Trainning",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifier & save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Trainning Datasets are Completed!!!")


           


if __name__ =="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()