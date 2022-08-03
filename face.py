  
# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk


# class Face_Recognition_System:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1500x700+0+0")
#         self.root.title("Face Recognition Sysytem")

#         if __name__ ==  "__main__":
#     root=Tk()
#     obj=Face_Recognition_System(root)
#     root.mainloop()  
        
         #First Image Upload

    #     img1=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img1=img1.resize((500,130),image.ANTIALIAS)
    #     self.photoimg1=ImageTK.PhotoImage(img1)
       
    #     f_lbl=Label(self.root,image=self.photoimg)
    #     f_lbl.place(x=0,y=0,width=500,height=130)
       
       
    #     #Second Image Upload
        
    #     img2=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img2=img2.resize((500,130),image.ANTIALIAS)
    #     self.photoimg2=ImageTK.PhotoImage(img2)
       
    #     f_lbl=Label(self.root,image=self.photoimg)
    #     f_lbl.place(x=500,y=0,width=500,height=130)
       
       
       
    #     #Third Image Upload
        
    #     img3=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img3=img3.resize((500,130),image.ANTIALIAS)
    #     self.photoimg3=ImageTK.PhotoImage(img3)
       
    #     f_lbl=Label(self.root,image=self.photoimg)
    #     f_lbl.place(x=1000,y=0,width=500,height=130)
       
       
    #    #background Image
        
    #     img4=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img4=img4.resize((1530,710),image.ANTIALIAS)
    #     self.photoimg4=ImageTK.PhotoImage(img4)
       
    #     bg_img=Label(self.root,image=self.photoimg)
    #     bg_img.place(x=0,y=130,width=1530,height=710)
        
        
    #    #Face Recognition Attendance System 
       
    #     title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
    #     title_lbl.place(x=0,y=0,width=1530,height=450)
        
        
        
    #     #Student button
        
    #     img5=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img5=img5.resize((1530,710),image.ANTIALIAS)
    #     self.photoimg5=ImageTK.PhotoImage(img5)
        
    #     b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
    #     b1.place(x=200,y=100,width=220,height=220)
        
    #     b1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    #     b1.place(x=200,y=300,width=220,height=40)
        
        
    #     #Detect Face Button
        
    #     img6=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img6=img6.resize((1530,710),image.ANTIALIAS)
    #     self.photoimg6=ImageTK.PhotoImage(img6)
        
    #     b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
    #     b1.place(x=500,y=100,width=220,height=220)
        
    #     b1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    #     b1.place(x=500,y=300,width=220,height=40)
        
        
        
    #     #Attendance Button
        
    #     img7=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img7=img7.resize((1530,710),image.ANTIALIAS)
    #     self.photoimg7=ImageTK.PhotoImage(img7)
        
    #     b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
    #     b1.place(x=800,y=100,width=220,height=220)
        
    #     b1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    #     b1.place(x=800,y=300,width=220,height=40)
        
        
    #      #Help  Button
        
    #     img8=Image.open(r"D:\Year\2022 image\3. march\IMG_20220309_182551_823.jpg")
    #     img8=img8.resize((1530,710),image.ANTIALIAS)
    #     self.photoimg8=ImageTK.PhotoImage(img8)
        
    #     b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
    #     b1.place(x=1100,y=100,width=220,height=220)
        
    #     b1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    #     b1.place(x=1100,y=300,width=220,height=40)
        



        
# if __name__ ==  "__main__":
#     root=Tk()
#     obj=Face_Recognition_System(root)
#     root.mainloop()        
        

import mysql.connector as c
con=c.connector.connect(host="localhost",username="root",passwd="",database=" face_recognizer")
if con.is_connector():
    print("success")
else:
    print("not success")
               