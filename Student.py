import cv2
from tkinter import*
import mysql.connector
from tkinter import ttk
import ttkbootstrap as tb
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        #self.root.attributes('-fullscreen', True)
        self.root.state("zoomed")
        self.root.wm_iconbitmap("face.ico")
        
        #veriables
        self.var_dep=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_Student_id=StringVar()
        self.var_EnrollNo=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_MobileNo=StringVar()
        self.var_DOB=StringVar()
        self.var_Address=StringVar()

        #Title l1
        title_lbl=tb.Label(self.root,text="Student Details",font=("Helvetica",36,"bold"),bootstyle="primary")
        title_lbl.place(x=750,y=0,width=1530,height=100)

        #Main Frame
        main_frame=tb.Frame(self.root,bootstyle="dark")
        main_frame.place(x=15,y=100,width=1890,height=800)

        #Left side frame
        Left_frame=tb.LabelFrame(main_frame,relief=RIDGE,text="Student Details Entery",bootstyle="primary")
        Left_frame.place(x=10,y=10,width=800,height=650)

        #Course Details frame
        CourseDetails_frame=tb.LabelFrame(Left_frame,relief=RIDGE,text="Course Details",bootstyle="primary")
        CourseDetails_frame.place(x=10,y=10,width=775,height=140)

        #Department Label & Combobox
        dep_label=tb.Label(CourseDetails_frame,text="Department :",font=("Helvetica",12),bootstyle="light")
        dep_label.grid(row=0,column=0, padx=10,pady=10,sticky=W)

        dep_combo=tb.Combobox(CourseDetails_frame,textvariable=self.var_dep,font=("Helvetica",12),state="readonly",bootstyle="primary")
        dep_combo['values']=("Select Department","Computer","IT","Civil","Michanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year Label & Combobox
        dep_label=tb.Label(CourseDetails_frame,text="Year :",font=("Helvetica",12),bootstyle="light")
        dep_label.grid(row=0,column=2, padx=10,pady=10,sticky=W)

        dep_combo=tb.Combobox(CourseDetails_frame,textvariable=self.var_Year,font=("Helvetica",12),state="readonly",bootstyle="primary")
        dep_combo['values']=("Select Year","1st","2nd","3rd","4th")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semeser Label & Combobox
        dep_label=tb.Label(CourseDetails_frame,text="Semester :",font=("Helvetica",12),bootstyle="light")
        dep_label.grid(row=1,column=0, padx=10,pady=10,sticky=W)

        dep_combo=tb.Combobox(CourseDetails_frame,textvariable=self.var_Sem,font=("Helvetica",12),state="readonly",bootstyle="primary")
        dep_combo['values']=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Student_id Label & Entry Fild
        std_label=tb.Label(CourseDetails_frame,text="Student ID :",font=("Helvetica",12),bootstyle="light")
        std_label.grid(row=1,column=2, padx=2,pady=10,sticky=W)
        
        std_Entry=tb.Entry(CourseDetails_frame,textvariable=self.var_Student_id,width=21,font=("Helvetica",12),bootstyle="primary")
        std_Entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student Details frame
        StudentDetails_frame=tb.LabelFrame(Left_frame,relief=RIDGE,text="Student Details",bootstyle="primary")
        StudentDetails_frame.place(x=10,y=155,width=775,height=300)

        #Enrollment No. Label & Entry Fild
        EnrolNo_label=tb.Label(StudentDetails_frame,text="Enrollment No. :",font=("Helvetica",12),bootstyle="light")
        EnrolNo_label.grid(row=0,column=0, padx=10,pady=10,sticky=W)

        EnrolNo_Entry=tb.Entry(StudentDetails_frame,textvariable=self.var_EnrollNo,width=20,font=("Helvetica",12),bootstyle="primary")
        EnrolNo_Entry.grid(row=0,column=1,pady=10,sticky=W)

        #Name Label & Entry Fild
        Name_label=tb.Label(StudentDetails_frame,text="Name :",font=("Helvetica",12),bootstyle="light")
        Name_label.grid(row=0,column=2, padx=10,pady=10,sticky=W)

        Name_Entry=tb.Entry(StudentDetails_frame,textvariable=self.var_Name,width=20,font=("Helvetica",12),bootstyle="primary")
        Name_Entry.grid(row=0,column=3,pady=10,sticky=W)

        #Division Label & Combobox
        Division_label=tb.Label(StudentDetails_frame,text="Division :",font=("Helvetica",12),bootstyle="light")
        Division_label.grid(row=1,column=0, padx=10,pady=10,sticky=W)

        div_combo=tb.Combobox(StudentDetails_frame,textvariable=self.var_Div,font=("Helvetica",12),state="readonly",width=18,bootstyle="primary")
        div_combo['values']=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,pady=10,sticky=W)

        #Gender Label & Combobox
        Gender_label=tb.Label(StudentDetails_frame,text="Gender :",font=("Helvetica",12),bootstyle="light")
        Gender_label.grid(row=1,column=2, padx=10,pady=10,sticky=W)

        Gender_combo=tb.Combobox(StudentDetails_frame,textvariable=self.var_Gender,font=("Helvetica",12),state="readonly",width=18,bootstyle="primary")
        Gender_combo['values']=("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=1,column=3,pady=10,sticky=W)

        #Email Label & Entry Fild
        Email_label=tb.Label(StudentDetails_frame,text="Email :",font=("Helvetica",12),bootstyle="light")
        Email_label.grid(row=2,column=0, padx=10,pady=10,sticky=W)

        Email_Entry=tb.Entry(StudentDetails_frame,textvariable=self.var_Email,font=("Helvetica",12),bootstyle="primary")
        Email_Entry.grid(row=2,column=1,pady=10,sticky=W)

        #Mobile No. Label & Entry Fild
        MobileNo_label=tb.Label(StudentDetails_frame,text="(M) No. :",font=("Helvetica",12),bootstyle="light")
        MobileNo_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        MobileNo_Entry=tb.Entry(StudentDetails_frame,textvariable=self.var_MobileNo,font=("Helvetica",12),bootstyle="primary")
        MobileNo_Entry.grid(row=2,column=3,pady=10,sticky=W)

        #DOB No. Label & Entry Fild
        DOB_label=tb.Label(StudentDetails_frame,text="DOB :",font=("Helvetica",12),bootstyle="light")
        DOB_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        DOB_Entry=tb.Entry(StudentDetails_frame,textvariable=self.var_DOB,font=("Helvetica",12),bootstyle="primary")
        DOB_Entry.grid(row=3,column=1,pady=10,sticky=W)

        #Address Label & Entry Fild
        Address_label=tb.Label(StudentDetails_frame,text="Address :",font=("Helvetica",12),bootstyle="light")
        Address_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        Address_Entry=ttk.Entry(StudentDetails_frame,textvariable=self.var_Address,width=20,font=("Helvetica",12),bootstyle="primary")
        Address_Entry.grid(row=3,column=3,pady=10,sticky=W)

        self.var_radio1=StringVar()
        radiobtn1=tb.Radiobutton(StudentDetails_frame,variable=self.var_radio1,text="Take Photo Sample.",value="Yes",bootstyle="primary")
        radiobtn1.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        #radio Buttons2
        radiobtn2=tb.Radiobutton(StudentDetails_frame,variable=self.var_radio1,text="No Photo Sample.",value="No",bootstyle="primary")
        radiobtn2.grid(row=4,column=1,padx=10,pady=10,sticky=W)

         #Button Frame
        btn_frame=tb.LabelFrame(Left_frame,relief=RIDGE,text="Operation",bootstyle="primary")
        btn_frame.place(x=10,y=460,width=775,height=150)

        #Save Button
        Savebtn=tb.Button(btn_frame,text="Save",width=18,command=self.Add_data,bootstyle="primary-outline")
        Savebtn.place(x=10,y=10,width=240,height=40)

        #Update Button
        Updatebtn=tb.Button(btn_frame,text="Update",command=self.update_data,width=18,bootstyle="primary-outline")
        Updatebtn.place(x=265,y=10,width=240,height=40)

        #Delete Button
        Deletebtn=tb.Button(btn_frame,text="Delete",width=18,command=self.delete_data,bootstyle="primary-outline")
        Deletebtn.place(x=520,y=10,width=240,height=40)

        #TakePhoto Button
        TakePhotobtn=tb.Button(btn_frame,text="Take Photo Sample",width=18,command=self.generate_dataset,bootstyle="primary-outline")
        TakePhotobtn.place(x=130,y=70,width=240,height=40)

        #Reset Button
        Resetbtn=tb.Button(btn_frame,text="Reset",width=18,command=self.reset_data,bootstyle="primary-outline")
        Resetbtn.place(x=390,y=70,width=240,height=40)

        #Right side frame
        Right_frame=tb.LabelFrame(main_frame,relief=RIDGE,text="Student Details",bootstyle="primary")
        Right_frame.place(x=820,y=10,width=1060,height=780)

        #variables
        self.var_search=StringVar()

        #Search System
        #Search Details frame
        SearchDetails_frame=tb.LabelFrame(Right_frame,relief=RIDGE,text="Search Details",bootstyle="primary")
        SearchDetails_frame.place(x=10,y=10,width=1040,height=180)

        src_label=tb.Label(SearchDetails_frame,text="Enter Enroll No. to search student details :",font=("Helvetica",12),bootstyle="light")
        src_label.place(x=10,y=10)

        #Search Button
        Searchbtn=tb.Button(SearchDetails_frame,text="Search",width=18,command=self.search_data,bootstyle="primary-outline")
        Searchbtn.place(x=10,y=50,width=240,height=40)

        Search_Entry=tb.Entry(SearchDetails_frame,textvariable=self.var_search,width=20,font=("Helvetica",12),bootstyle="primary")
        Search_Entry.place(x=270,y=50,width=240,height=40)

        #Show Button
        Showbtn=tb.Button(SearchDetails_frame,text="Show All Data",width=18,command=self.fetch_data,bootstyle="primary-outline")
        Showbtn.place(x=10,y=100,width=240,height=40)

        #Table frame
        table_frame=tb.Frame(Right_frame,bootstyle="dark")
        table_frame.place(x=10,y=200,width=1040,height=550)

        scroll_x=tb.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="primary-round")
        scroll_y=tb.Scrollbar(table_frame,orient=VERTICAL,bootstyle="primary-round")

        self.student_table=tb.Treeview(table_frame,column=("Student_id","Name","EnrollNo","Div","Sem","Dept","Year","Gender","DOB","MobileNo","Address","Email","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,bootstyle='dark')
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Student_id",text="Student_id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("EnrollNo",text="Enrollment")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("MobileNo",text="Mobile No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        # Set Width of Colums 
        self.student_table.column("Student_id",width=150,anchor=CENTER)
        self.student_table.column("Name",width=150,anchor=CENTER)
        self.student_table.column("EnrollNo",width=150,anchor=CENTER)
        self.student_table.column("Div",width=150,anchor=CENTER)
        self.student_table.column("Sem",width=150,anchor=CENTER)
        self.student_table.column("Dept",width=150,anchor=CENTER)
        self.student_table.column("Year",width=150,anchor=CENTER)
        self.student_table.column("Gender",width=150,anchor=CENTER)
        self.student_table.column("DOB",width=150,anchor=CENTER)
        self.student_table.column("MobileNo",width=150,anchor=CENTER)
        self.student_table.column("Address",width=150,anchor=CENTER)
        self.student_table.column("Email",width=150,anchor=CENTER)
        self.student_table.column("Photo",width=150,anchor=CENTER)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# ==================Function Decleration==============================

#Add data function
    def Add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_EnrollNo.get()=="" or self.var_Name.get()=="":
            messagebox.showerror("Eroor","All fields must be filld",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                self.var_Student_id.get(),
                self.var_Name.get(),
                self.var_EnrollNo.get(),
                self.var_Div.get(),
                self.var_Sem.get(),
                self.var_dep.get(),
                self.var_Year.get(),
                self.var_Gender.get(),
                self.var_DOB.get(),
                self.var_MobileNo.get(),
                self.var_Address.get(),
                self.var_Email.get(),
                self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Saved","Student Details Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #fetch data fuction
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    #get cursor function
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_Student_id.set(data[0])
        self.var_Name.set(data[1]),
        self.var_EnrollNo.set(data[2]),
        self.var_Div.set(data[3]),
        self.var_Sem.set(data[4]),
        self.var_dep.set(data[5]),
        self.var_Year.set(data[6]),
        self.var_Gender.set(data[7]),
        self.var_DOB.set(data[8]),
        self.var_MobileNo.set(data[9]),
        self.var_Address.set(data[10]),
        self.var_Email.set(data[11]),
        self.var_radio1.set(data[12]),
        
    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_EnrollNo.get()=="" or self.var_Name.get()=="":
            messagebox.showerror("Eroor","All fields must be filld",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details ?",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                     my_cursor=conn.cursor()
                     my_cursor.execute("UPDATE student SET Name=%s,Roll_No=%s,Division=%s,Semester=%s,Department=%s,Year=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Email=%s,PhotoSample=%s where Student_ID=%s",(
                        self.var_Name.get(),
                        self.var_EnrollNo.get(),
                        self.var_Div.get(),
                        self.var_Sem.get(),
                        self.var_dep.get(),
                        self.var_Year.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_MobileNo.get(),
                        self.var_Address.get(),
                        self.var_Email.get(),
                        self.var_radio1.get(),
                        self.var_Student_id.get()
                         ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Updated","Student details are updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Delete Function
    def delete_data(self):
        if self.var_Student_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete!","Do you want to delete Student details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Student details are Deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset Function
    def reset_data(self):
        self.var_Student_id.set("")
        self.var_Name.set(""),
        self.var_EnrollNo.set(""),
        self.var_Div.set("Select Division"),
        self.var_Sem.set("Select Semester"),
        self.var_dep.set("Select Department"),
        self.var_Year.set("Select Year"),
        self.var_Gender.set("Select Gender"),
        self.var_DOB.set(""),
        self.var_MobileNo.set(""),
        self.var_Address.set(""),
        self.var_Email.set(""),
        self.var_radio1.set(""),


     # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","Please Enter Enrollment number of the student",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
                my_cursor = conn.cursor()  
                sql = "SELECT Student_ID,Name,Roll_No,Division,Semester,Department,Year,Gender,DOB,Mobile_No,Address,Email,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_EnrollNo.get()=="" or self.var_Name.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myreslut = my_cursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                my_cursor.execute("UPDATE student SET Name=%s,Roll_No=%s,Division=%s,Semester=%s,Department=%s,Year=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Email=%s,PhotoSample=%s where Student_ID=%s",(
                        self.var_Name.get(),
                        self.var_EnrollNo.get(),
                        self.var_Div.get(),
                        self.var_Sem.get(),
                        self.var_dep.get(),
                        self.var_Year.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_MobileNo.get(),
                        self.var_Address.get(),
                        self.var_Email.get(),
                        self.var_radio1.get(),
                        self.var_Student_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



if __name__ == "__main__":
    root = tb.Window("Student Details","superhero")
    obj=Student(root)
    root.mainloop()