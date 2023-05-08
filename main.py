import os
import cv2
import tkinter
import numpy as np
from tkinter import*
import mysql.connector
import ttkbootstrap as tb
from csv import DictWriter
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox
from Student import Student
from attendance import attendance

class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        #self.root.attributes('-fullscreen', True)
        self.root.state("zoomed")
        self.root.wm_iconbitmap("face.ico")

        #Title l1
        title_lbl=tb.Label(self.root,text="Face Recognization & Attendace System",font=("Helvetica",36,"bold"),bootstyle="primary")
        title_lbl.place(x=400,y=0,width=1530,height=100)
#======================================Student Button=================================
        img1=tb.Image.open(r"resources\Student.png")
        img1=img1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=tb.Button(self.root,image=self.photoimg1,cursor="hand2",command=self.student_details,bootstyle="primary-outline")
        b1.place(x=550,y=200,width=220,height=220)

        b2=tb.Button(self.root,text="Student Details",cursor="hand2",command=self.student_details,bootstyle="primary-outline")
        b2.place(x=550,y=425,width=220,height=40)
#======================================Trainmodule Button==============================
        img2=tb.Image.open(r"resources\Trainmodule.png")
        img2=img2.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b3=tb.Button(self.root,image=self.photoimg2,cursor="hand2",command=self.train_classifier,bootstyle="primary-outline")
        b3.place(x=850,y=200,width=220,height=220)

        b4=tb.Button(self.root,text="Train Module",cursor="hand2",command=self.train_classifier,bootstyle="primary-outline")
        b4.place(x=850,y=425,width=220,height=40)
#======================================FaceDetection Button============================
        img3=tb.Image.open(r"resources\FaceDetection.png")
        img3=img3.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b5=tb.Button(self.root,image=self.photoimg3,cursor="hand2",command=self.face_detect,bootstyle="primary-outline")
        b5.place(x=1150,y=200,width=220,height=220)

        b6=tb.Button(self.root,text="Face Detection",cursor="hand2",command=self.face_detect,bootstyle="primary-outline")
        b6.place(x=1150,y=425,width=220,height=40)
#======================================Attendance Button===============================
        img4=tb.Image.open(r"resources\Attendance.png")
        img4=img4.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b7=tb.Button(self.root,image=self.photoimg4,cursor="hand2",command=self.attendace_btn,bootstyle="primary-outline")
        b7.place(x=550,y=500,width=220,height=220)

        b8=tb.Button(self.root,text="Attendance",cursor="hand2",command=self.attendace_btn,bootstyle="primary-outline")
        b8.place(x=550,y=725,width=220,height=40)
#======================================Photos Button===================================
        img5=tb.Image.open(r"resources\Photos.png")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b9=tb.Button(self.root,image=self.photoimg5,cursor="hand2",command=self.open_img,bootstyle="primary-outline")
        b9.place(x=850,y=500,width=220,height=220)

        b10=tb.Button(self.root,text="Photos",cursor="hand2",command=self.open_img,bootstyle="primary-outline")
        b10.place(x=850,y=725,width=220,height=40)
#======================================Exit Button======================================
        img6=tb.Image.open(r"resources\Exit.png")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b11=tb.Button(self.root,image=self.photoimg6,cursor="hand2",command=self.ExitP,bootstyle="primary-outline")
        b11.place(x=1150,y=500,width=220,height=220)

        b12=tb.Button(self.root,text="Exit",cursor="hand2",command=self.ExitP,bootstyle="primary-outline")
        b12.place(x=1150,y=725,width=220,height=40)
#=====================================Function for Buttons===============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendace_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def open_img(self):
        os.startfile("data_img")

    def ExitP(self):
        self.ExitP=tkinter.messagebox.askyesno("Exit","Are you sure you want to exit!!!",parent=self.root)
        if self.ExitP>0:
            self.root.destroy()
        else:
            return
#=====================================Function for Traing==================================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
#===========================================Train Classifier=======================================
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)
#=====================================Function for Attendance===================================
    def attendance(self,n,r):
        current_datetime = datetime.now().strftime("%d-%m-%y-%I-%M-%p")
        str_current_datetime = str(current_datetime)
        file_name = "Attendance/"+str_current_datetime+".csv"

        with open(file_name,"a+",newline='') as f:
            dict_writer = DictWriter(f, fieldnames=['Name', 'Enroll No', 'Date','Time', 'Attendence'])
            if os.stat(file_name).st_size == 0:        #if file is not empty than header write else not
                dict_writer.writeheader()   

            f.seek(0) 
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if ((n not in name_list)) and ((r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%I:%M:%p")
                f.writelines(f"\n{n}, {r}, {d1}, {dtString}, Present")       
#==============================Function for Face Detection=============================
    def face_detect(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                if confidence>77:
                    cv2.putText(img,f"Name: {n}",(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(241,37,172),2)
                    cv2.putText(img,f"Enroll_No: {r}",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(241,37,172),2)
                    self.attendance(n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
                    cv2.putText(img,"Unknown Face",(x,y-50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(241,37,172),2)
                
                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
#==============================Main=============================
if __name__ == "__main__":
    root = tb.Window("Face Recognization & Attendace System","superhero")
    obj=Face_Recognization_System(root)
    root.mainloop()