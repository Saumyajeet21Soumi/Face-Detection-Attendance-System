from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first image
        img=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\OIP (2).jpeg")
        img=img.resize((500,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=250)

        #second image
        img1=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\guy-using-laptop-for-e-learning.jpg")
        img1=img1.resize((500,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=250)

        #third image
        img2=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\tumblr_nz7yvnG1TX1r2bqv4o1_640.png")
        img2=img2.resize((500,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=250)

        #bg change
        img3=Image.open(r"C:\Users\Soumi\Desktop\Face Detection System\project pic\Color-Block-Wallpaper.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=250,width=1530,height=790)

  
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=50,y=50,width=1400,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=470)  


        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=660,height=130)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold")) 
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=140,width=665,height=300)

        #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_id,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student Name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"))
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_nmae_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        student_nmae_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=20)
        class_div_combo["values"]=("A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No.
        roll_no_label=Label(class_student_frame,text="Roll NO:",font=("times new roman",13,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=20)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no.
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=670,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=670,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Right_frame.place(x=700,y=10,width=680,height=470)  

        #search system
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=0,width=710,height=70)   

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No","Address","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)

        #table 
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=80,width=680,height=360) 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student2_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student2_table.xview)
        scroll_y.config(command=self.student2_table.yview)

        self.student2_table.heading("dep",text="Department")
        self.student2_table.heading("course",text="Course")
        self.student2_table.heading("year",text="Year")
        self.student2_table.heading("sem",text="Semester")
        self.student2_table.heading("id",text="StudentId")
        self.student2_table.heading("name",text="Name")
        self.student2_table.heading("div",text="Division")
        self.student2_table.heading("roll",text="Roll")
        self.student2_table.heading("gender",text="Gender")
        self.student2_table.heading("dob",text="Date of Birth")
        self.student2_table.heading("email",text="Email")
        self.student2_table.heading("phone",text="Phone")
        self.student2_table.heading("address",text="Address")
        self.student2_table.heading("teacher",text="Teacher")
        self.student2_table.heading("photo",text="PhotoSampleStatus")
        self.student2_table["show"]="headings"


        self.student2_table.column("dep",width=100)
        self.student2_table.column("course",width=100)
        self.student2_table.column("year",width=100)
        self.student2_table.column("sem",width=100)
        self.student2_table.column("id",width=100)
        self.student2_table.column("name",width=100)
        self.student2_table.column("div",width=100)
        self.student2_table.column("roll",width=100)
        self.student2_table.column("gender",width=100)
        self.student2_table.column("dob",width=100)
        self.student2_table.column("email",width=100)
        self.student2_table.column("phone",width=100)
        self.student2_table.column("address",width=100)
        self.student2_table.column("teacher",width=100)
        self.student2_table.column("photo",width=100)

        self.student2_table.pack(fill=BOTH,expand=1)
        self.student2_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #functions Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="N#@98wrft45",database="face_detection")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_id.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()                                                                                                         
                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="N#@98wrft45",database="face_detection")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student2")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student2_table.delete(*self.student2_table.get_children())
            for i in data:
                self.student2_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student2_table.focus()
        content=self.student2_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update fuction
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="N#@98wrft45",database="face_detection")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student2 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                     self.var_id.get()

                                                                                                                                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Student Details update complete",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

    #Delete Function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="N#@98wrft45",database="face_detection")
                    my_cursor=conn.cursor()
                    sql="delete from student2 where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #generated data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="N#@98wrft45",database="face_detection")
                my_cursor=conn.cursor()
                my_cursor.execute("select*from student2")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student2 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                     self.var_id.get()==id+1

                                                                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predifiend data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropprd(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for(x,h,w,y) in faces:
                        face_cropprd=img[y:y+h,x:x+w]
                        return face_cropprd
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropprd(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropprd(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"DUe to:{str(es)}",parent=self.root)


if __name__ =="__main__":
    root=Tk()
    obj= student(root)
    root.mainloop()