from tkinter import*
from tkinter import ttk
from unicodedata import name
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np 



class Face_Recoginition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x790+0+0")
        self.root.title("Automatic Attendance Sysytem")

        title_lbl=Label(self.root,text="FACE RECOGNTION  ",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1410,height=50)
        #1stLeft sede image
        img_left=Image.open(r"Project_Image\facial-recognitiongirl.jpg")
        img_left=img_left.resize((600,710),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=50,width=600,height=710)
        

        #2ndRight side Image
        img_right=Image.open(r"Project_Image\process.webp")
        img_right=img_right.resize((800,710),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=600,y=50,width=800,height=710)

        # Button 
        # img5=Image.open(r"Project_Image\istockphoto.jpg")
        # img5=img5.resize((250,180),Image.Resampling.LANCZOS)
        # self.photoimg5=ImageTk.PhotoImage(img5)
        # b1=Button(f_lbl,image=self.photoimg5,cursor="hand2")
        # b1.place(x=0,y=420,width=250,height=180)
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=600,width=250,height=50)

    #Attendace maeked
    def mark_attendance(self,s,n,r,d):
        with open("rupesh.csv","r+",newline="\n") as f :
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((s not in name_list) and (n not in name_list) and (r not in name_list) and (d  not in name_list)):
                now =datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstring=now.strftime("%H:%M:%S:")
                f.writelines(f"\n{s},{r},{n},{d},{dtstring},{d1},Present")




    #Face Recogniton
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color, text, clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) 

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) #formulaa confidence

                conn=mysql.connector.connect(host="localhost",username="root",password="#@Rupesh22@#",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT studentSNo FROM student where studentSNo="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)

                my_cursor.execute("SELECT studentName FROM student where studentSNo="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("SELECT enrollNo FROM student where studentSNo="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("SELECT dep FROM student where studentSNo="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>75:
                    cv2.putText(img,f"studentSNo:{s}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0,0,(255,255,255),3)
                    cv2.putText(img,f"studentName:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0,0,(255,255,255),3)
                    cv2.putText(img,f"enrollNo:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0,0,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0,0,(255,255,255),3)
                    self.mark_attendance(s,r,n,d)

                else:
                
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Student ",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0,0,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
            #DO not reapet your self
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1,1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()




if __name__ ==  "__main__":
    root=Tk()
    obj=Face_Recoginition(root)
    root.mainloop()          