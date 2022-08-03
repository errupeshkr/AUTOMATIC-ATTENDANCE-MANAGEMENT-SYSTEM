from ast import Pass
from importlib.resources import path
import os
from platform import release
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX, CascadeClassifier, VideoCapture, destroyAllWindows, imshow, imwrite, waitKey
import mysql.connector
from numpy import delete
import cv2 


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automatic Attendance Sysytem")
# Variables
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar()    
        self.var_semester=StringVar() 
        self.var_studentSNo=StringVar()
        self.var_studentName=StringVar() 
        self.var_enrollNo=StringVar() 
        self.var_classSection=StringVar()    
        self.var_gender=StringVar() 
        self.var_studentDOB=StringVar()
        self.var_emailId=StringVar() 
        self.var_address=StringVar() 
        self.var_phoneNo=StringVar() 
        self.var_tgName=StringVar()    
        # self.var_photo=StringVar() 
        self.var_radio1=StringVar()

    #First Image Upload
        img=Image.open(r"Project_Image\frms.jpg")
        img=img.resize((500,190),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150) 

    #Second1 Image Upload
        img1=Image.open(r"Project_Image\recogniation.jpg")
        img1=img1.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1) 
        f_lbl.place(x=490,y=0,width=500,height=150) 


    #Third Image Upload
        img2=Image.open(r"Project_Image\images.jpg")
        img2=img2.resize((500,170),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=950,y=0,width=500,height=150)

    #background Image Upload
        img3=Image.open(r"Project_Image\bg.webp")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT STSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1430,height=35)
        
    #main frame in student 
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=45,width=1320,height=520)
        #left label frame
        Left_lframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Left_lframe.place(x=10,y=10,width=650,height=550)

        
    #image add in leftside
        img_left=Image.open(r"Project_Image\hand.webp")
        img_left=img_left.resize((640,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_lframe,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=80)
        
    #current course information
        current_course_frame=LabelFrame(Left_lframe ,bd=2,relief=RIDGE,text="Current Course information",font=("times new roman",15,"bold"))
        current_course_frame.place(x=10,y=80 ,width=620,height=100)
    #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        dep_label.grid(row=0,column=0,padx=2,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer Science & Engineering","Electrical Engineering","Civil Engineering","Mechanical Engineering","Electronics and Communication Engineering","Artificial Intelligence Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=2)


    #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        course_label.grid(row=0,column=2,padx=2,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly",width=15)
        course_combo["values"]=("Select Course","Bachelor of Technology","Bachelor in Engineering","Master of Technology","Master of Engineering","Bachelor of Pharmacy","Master of Pharmacy")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10, pady=2,sticky=W)


    #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        year_label.grid(row=1,column=0,padx=2,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2019 - 2023","2020 - 2024","2021 - 2025","2022 - 2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=2)


    #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",15,"bold"),state="readonly",width=15)
        semester_combo["values"]=("Select Semester","1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10, pady=2,sticky=W)


    #Class student information (170 positon of frame, 280 is height of frame)
        class_student_frame=LabelFrame(Left_lframe ,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",15,"bold"))
        class_student_frame.place(x=10,y=175 ,width=620,height=300)

    #student serial no
        studentSNo_label=Label(class_student_frame,text="Student S.No. :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        studentSNo_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)
    #student s.no. entry
        studentSNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentSNo,font=("times new roman",15,"bold"),width=15)
        studentSNo_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)


    #student Name
        studentName_label=Label(class_student_frame,text="Student Name :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        studentName_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)
    #student name entry
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentName,font=("times new roman",15,"bold"),width=15)
        studentName_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

    #Class section
        classSection_label=Label(class_student_frame,text="Class Section :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        classSection_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)
    #student Class section entry
        classSection_entry=ttk.Entry(class_student_frame,textvariable=self.var_classSection,font=("times new roman",15,"bold"),width=15)
        classSection_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)


    #student Enrollment numbber
        enrollNo_label=Label(class_student_frame,text="Enrollment No. :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        enrollNo_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)
    #student Enrollment numbber entry
        enrollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_enrollNo,font=("times new roman",15,"bold"),width=15)
        enrollNo_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)    


    #Student Gender
        gender_label=Label(class_student_frame,text="Gender :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        gender_label.grid(row=2,column=0,padx=2,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),state="readonly",width=13)
        gender_combo["values"]=("Select ","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
    #     gender_label=Label(class_student_frame,text="Gender :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
    #     gender_label.grid(row=2,column=0,padx=2,pady=5,sticky=W)
    # #student Gender entry
    #     gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),width=15)
    #     gender_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)


    #student Date Of Birth
        studentDOB_label=Label(class_student_frame,text="Date Of Birth :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        studentDOB_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)
    #student Date Of Birth entry
        studentDOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentDOB,font=("times new roman",15,"bold"),width=15)
        studentDOB_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W) 

    
    #Student Email i
        emailId_label=Label(class_student_frame,text="Email id :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        emailId_label.grid(row=3,column=0,padx=2,pady=5,sticky=W)
    #student Email id entry
        emailId_entry=ttk.Entry(class_student_frame,textvariable=self.var_emailId,font=("times new roman",15,"bold"),width=15)
        emailId_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)


    #student Phone number
        phoneNo_label=Label(class_student_frame,text="phone No. :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        phoneNo_label.grid(row=3,column=2,padx=2,pady=5,sticky=W)
    #student phone number entry
        phoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phoneNo,font=("times new roman",15,"bold"),width=15)
        phoneNo_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)


     #Student Address
        address_label=Label(class_student_frame,text="Address :",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        address_label.grid(row=4,column=0,padx=2,pady=5,sticky=W)
    #student Address entry
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,font=("times new roman",15,"bold"),width=15)
        address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)


    #student T.G. name
        tgName_label=Label(class_student_frame,text="T.G. Name ",font=("times new roman",15,"bold"),bg="white",fg="darkgreen")
        tgName_label.grid(row=4,column=2,padx=2,pady=5,sticky=W)
    #student T.G. name entry
        tgName_entry=ttk.Entry(class_student_frame,textvariable=self.var_tgName,font=("times new roman",15,"bold"),width=15)
        tgName_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)   


    #ratio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,column=1)

    #Button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=650,height=70)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        upate_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        upate_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=250,width=650,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1) 
    
    #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=670,y=10,width=640,height=500)

        img_right=Image.open(r"C:\Users\Rupesh Chauhary\Downloads\rightpic.jpg")
        img_right=img_right.resize((640,100),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=100)

    #=====================SEARCH SYSTEM==============
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        search_frame.place(x=5,y=100,width=630,height=70)
    #==============search by label=============
        search_label=Label(search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
    #============== combobox for select=============
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Roll_No. ","Phone_No. ")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)
    #==============enter the data===============
        search_entry=ttk.Entry(search_frame,width=13,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    #==============Button for search ===============
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)
    #==============Button for showall ===============
        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)

    #=====================TABLE FRAME==============
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=630,height=300)
    #==============ttk.scrollbar module for scolling HOLI VERT ===============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","semester","studentSNo","studentName","classSection","enrollNo","gender","studentDOB","emailId","phoneNo","address","tgName","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("studentSNo",text="Student S.No.")
        self.student_table.heading("studentName",text="Student Name")
        self.student_table.heading("classSection",text="Class Section")
        self.student_table.heading("enrollNo",text="Enrollment No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("studentDOB",text="Date Of Birth")
        self.student_table.heading("emailId",text="Email Id")
        self.student_table.heading("phoneNo",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("tgName",text="T.G. Name")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("studentSNo",width=100)
        self.student_table.column("studentName",width=100)
        self.student_table.column("classSection",width=100)
        self.student_table.column("enrollNo",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("studentDOB",width=100)
        self.student_table.column("emailId",width=100)
        self.student_table.column("phoneNo",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("tgName",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
    #make function for save/data adding
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentSNo.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"  or self.var_semester.get()=="Select Semester"or self.var_enrollNo.get()=="" or self.var_phoneNo.get()=="":
        # if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentSNo.get()=="": 
            messagebox.showerror("Error!","All Field are required",parent=self.root)
        else:
            try:
            #   messagebox.showinfo("Success","WelcomeTo SN3R")
                conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_studentSNo.get(),
                                                                                                             self.var_studentName.get(),
                                                                                                             self.var_classSection.get(),
                                                                                                             self.var_enrollNo.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_studentDOB.get(),
                                                                                                             self.var_emailId.get(),
                                                                                                             self.var_phoneNo.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_tgName.get(),
                                                                                                             self.var_radio1.get()
                                                                                                           ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!",f"Due To :{str(es)}",parent=self.root)
# Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    #GET CURSOR
    def get_cursor(self,event=""):
        Cursor_focus=self.student_table.focus()
        content=self.student_table.item(Cursor_focus) #contain store in entry fill
        data=content["values"]
        self.var_dep.set(data[0]),  
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]), 
        self.var_studentSNo.set(data[4]),  
        self.var_studentName.set(data[5]),
        self.var_classSection.set(data[6]),
        self.var_enrollNo.set(data[7]),
        self.var_gender.set(data[8]), 
        self.var_studentDOB.set(data[9]),  
        self.var_emailId.set(data[10]),
        self.var_phoneNo.set(data[11]),
        self.var_address.set(data[12]),
        self.var_tgName.set(data[13]),  
        # self.var_photo.set(data[14]),
        self.var_radio1.set(data[14]),
       
#     #UPDATE FUNCTION
#     #UPDATE FUNCTION
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentSNo.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"  or self.var_semester.get()=="Select Semester"or self.var_enrollNo.get()=="" or self.var_phoneNo.get()=="":
        # if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentSNo.get()=="": 
            messagebox.showerror("Error!","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update >0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database="face_recognizer")
                    my_cursor=conn.cursor()  
                    my_cursor.execute("Update student set dep=%s,course=%s,year=%s,semester=%s,studentName=%s,classSection=%s,enrollNo=%s,gender=%s,studentDOB=%s,emailId=%s,phoneNo=%s,address=%s,tgName=%s,photo=%s where studentSNo=%s",(
                                                                                                
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_studentName.get(),
                                                                                                             self.var_classSection.get(),
                                                                                                             self.var_enrollNo.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_studentDOB.get(),
                                                                                                             self.var_emailId.get(),
                                                                                                             self.var_phoneNo.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_tgName.get(),
                                                                                                             self.var_radio1.get(),
                                                                                                             self.var_studentSNo.get()
                                                                                                            # self.var_photo.get()
                                                                                                            ))
                else:
                 if not Update: 
                    return
                messagebox.showinfo("Sucsess", "Student Details Update has been completed successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)
                
    #DELETE FUNCTION
    def delete_data(self):
        if self.var_studentSNo.get()=="": 
            messagebox.showerror("Error!","Student Serial Number must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                if delete >0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database=" face_recognizer")
                    my_cursor=conn.cursor()  
                    sql="delete from student where studentSNo=%s"
                    val=(self.var_studentSNo.get(), )
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student Details has been  deleted successfulluy ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)

    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentSNo.set("")
        self.var_studentName.set("")
        self.var_classSection.set("")
        self.var_enrollNo.set("")
        self.var_gender.set("Select")
        self.var_studentDOB.set("")
        self.var_emailId.set("")
        self.var_phoneNo.set("")
        self.var_address.set("")
        self.var_tgName.set("")
        self.var_radio1.set("")


    # Generate data set or take photo samples 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentSNo.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"  or self.var_semester.get()=="Select Semester"or self.var_enrollNo.get()=="" or self.var_phoneNo.get()=="":
            messagebox.showerror("Error!","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set dep=%s,course=%s,year=%s,semester=%s,studentName=%s,classSection=%s,enrollNo=%s,gender=%s,studentDOB=%s,emailId=%s,phoneNo=%s,address=%s,tgName=%s,photo=%s where studentSNo=%s",(
                                                                                                
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_studentName.get(),
                                                                                                             self.var_classSection.get(),
                                                                                                             self.var_enrollNo.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_studentDOB.get(),
                                                                                                             self.var_emailId.get(),
                                                                                                             self.var_phoneNo.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_tgName.get(),
                                                                                                             self.var_radio1.get(),
                                                                                                             self.var_studentSNo.get()==id+1
                                                                                                            # self.var_photo.get() 
                                                                                                        ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            #Load predifiend data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor -1.3
                    #Minimal Neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)     
                img_id=0
                while True:
                   ret,my_frame=cap.read()
                   if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(350,350))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/Ranjeet."+str(id)+"."+str(img_id)+".jpg"    
                        cv2.imwrite(file_name_path,face) #imwrite fn for writting on face
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                        cv2.imshow("Cropped Face",face)

                   if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets have been completed successfully! ")
            except Exception as es:
                messagebox.showerror("Error!",f"Due to :{str(es)}",parent=self.root)        







if __name__ ==  "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 

    # pady mean social distancing like diff b/w to button
    #pillow  python image in library
    #ANTIALIAS IS DESRIPTEF DUE TO USE  Resampling.LANCZOS
    # opencv module import cv2