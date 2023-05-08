import os
import csv
from tkinter import*
import mysql.connector
import ttkbootstrap as tb
from tkinter import messagebox
from tkinter import filedialog

mydata=[]

class attendance:
    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        self.root.wm_iconbitmap("face.ico")

        #variables
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_AS=StringVar()

        #Title l1
        title_lbl=tb.Label(self.root,text="Student Attendace Details",font=("Helvetica",36,"bold"),bootstyle="primary")
        title_lbl.place(x=600,y=0,width=1530,height=100)

        #Main Frame
        main_frame=tb.Frame(self.root,bootstyle="dark")
        main_frame.place(x=10,y=100,width=1890,height=800)

        #Left side frame
        Left_frame=tb.LabelFrame(main_frame,relief=RIDGE,text="Attendace Entery",bootstyle="primary")
        Left_frame.place(x=10,y=10,width=820,height=780)

        #Entry Details frame
        EntryDetails_frame=tb.LabelFrame(Left_frame,relief=RIDGE,text="Edit Details",bootstyle="primary")
        EntryDetails_frame.place(x=10,y=0,width=800,height=200)

        #Student_name Label & Entry Fild
        Name_label=tb.Label(EntryDetails_frame,text="Name :",font=("Helvetica",12),bootstyle="light")
        Name_label.grid(row=0,column=0, padx=10,pady=10,sticky=W)

        Name_Entry=tb.Entry(EntryDetails_frame,textvariable=self.var_name,font=("Helvetica",12),bootstyle="primary")
        Name_Entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Student_Enroll Label & Entry Fild
        Enroll_label=tb.Label(EntryDetails_frame,text="Enroll_No :",font=("Helvetica",12),bootstyle="light")
        Enroll_label.grid(row=0,column=2, padx=10,pady=10,sticky=W)

        Enroll_Entry=tb.Entry(EntryDetails_frame,textvariable=self.var_roll,font=("Helvetica",12,),bootstyle="primary")
        Enroll_Entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Time Label & Entry Fild
        Time_label=tb.Label(EntryDetails_frame,text="Time :",font=("Helvetica",12),bootstyle="light")
        Time_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        Time_Entry=tb.Entry(EntryDetails_frame,textvariable=self.var_time,font=("Helvetica",12),bootstyle="primary")
        Time_Entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Date Label & Entry Fild
        Date_label=tb.Label(EntryDetails_frame,text="Date :",font=("Helvetica",12),bootstyle="light")
        Date_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        Date_Entry=tb.Entry(EntryDetails_frame,textvariable=self.var_date,font=("Helvetica",12),bootstyle="primary")
        Date_Entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Attendace Status Label & Combobox
        AS_label=tb.Label(EntryDetails_frame,text="Attendace Status :",font=("Helvetica",12),bootstyle="light")
        AS_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        AS_combo=tb.Combobox(EntryDetails_frame,textvariable=self.var_AS,font=("Helvetica",12),state="readonly",width=18,height=40,bootstyle="primary")
        AS_combo['values']=("Select Status","Present","Absent")
        AS_combo.current(0)
        AS_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        #Table frame
        tablel_frame=tb.Frame(Left_frame,bootstyle="dark")
        tablel_frame.place(x=10,y=210,width=800,height=440)

        scrolll_x=tb.Scrollbar(tablel_frame,orient=HORIZONTAL,bootstyle="primary-round")
        scrolll_y=tb.Scrollbar(tablel_frame,orient=VERTICAL,bootstyle="primary-round")

        #create table 
        self.attendanceReportl = tb.Treeview(tablel_frame,column=("Name","Enroll_No","Date","Time","Attend"),xscrollcommand=scrolll_x.set,yscrollcommand=scrolll_y.set,bootstyle='dark')

        scrolll_x.pack(side=BOTTOM,fill=X)
        scrolll_y.pack(side=RIGHT,fill=Y)
        scrolll_x.config(command=self.attendanceReportl.xview)
        scrolll_y.config(command=self.attendanceReportl.yview)

        self.attendanceReportl.heading("Name",text="Std-Name")
        self.attendanceReportl.heading("Enroll_No",text="Enroll.No")
        self.attendanceReportl.heading("Date",text="Date")
        self.attendanceReportl.heading("Time",text="Time")
        self.attendanceReportl.heading("Attend",text="Attend-status")
        self.attendanceReportl["show"]="headings"

        # Set Width of Colums 
        self.attendanceReportl.column("Name",width=100,anchor=CENTER)
        self.attendanceReportl.column("Enroll_No",width=100,anchor=CENTER)
        self.attendanceReportl.column("Date",width=100,anchor=CENTER)
        self.attendanceReportl.column("Time",width=100,anchor=CENTER)
        self.attendanceReportl.column("Attend",width=100,anchor=CENTER)
        
        self.attendanceReportl.pack(fill=BOTH,expand=1)

        #Button Frame
        btn_frame=tb.LabelFrame(Left_frame,relief=RIDGE,text="Operation",bootstyle="primary")
        btn_frame.place(x=10,y=660,width=800,height=90)

        btn1_frame=tb.Frame(btn_frame,bootstyle="dark")
        btn1_frame.place(x=5,y=0,width=785,height=60)

        #Import Button
        Importbtn=tb.Button(btn_frame,text="Import .csv",command=self.importCsv,width=25,bootstyle="primary-outline")
        Importbtn.grid(row=0,column=0,padx=10,pady=10,ipadx=10,sticky=W)

        #insert Button
        inbtn=tb.Button(btn_frame,text="Insert in DataBase",width=25,command=self.insert_data,bootstyle="primary-outline")
        inbtn.grid(row=0,column=1,padx=10,pady=10,ipadx=10,sticky=W)

        #Reset Button
        Resetbtn=tb.Button(btn_frame,text="Reset",command=self.reset_data,width=25,bootstyle="primary-outline")
        Resetbtn.grid(row=0,column=2,padx=10,pady=10,ipadx=10,sticky=W)

        #Right side frame
        Right_frame=tb.LabelFrame(main_frame,text="Attendace Details From Database",bootstyle="primary")
        Right_frame.place(x=850,y=10,width=1030,height=780)

        #Button Frame
        btn1_frame=tb.LabelFrame(Right_frame,relief=RIDGE,text="Operation on DataBase",bootstyle="primary")
        btn1_frame.place(x=10,y=660,width=1010,height=90)

        btn1_frame=tb.Frame(btn1_frame,bootstyle="dark")
        btn1_frame.place(x=10,y=0,width=990,height=60)

        #Update Button
        Updatebtn=tb.Button(btn1_frame,text="Update",command=self.update_data,width=25,bootstyle="primary-outline")
        Updatebtn.grid(row=0,column=1,padx=35,pady=15,ipadx=30,sticky=W)

        #Delete Button
        deletebtn=tb.Button(btn1_frame,text="Delete",command=self.delete_data,width=25,bootstyle="primary-outline")
        deletebtn.grid(row=0,column=2,padx=10,pady=10,ipadx=30,sticky=W)

        #Export Button
        Expbtn=tb.Button(btn1_frame,text="Export to CSV",command=self.export_to_csv,width=25,bootstyle="primary-outline")
        Expbtn.grid(row=0,column=3,padx=30,pady=10,ipadx=30,sticky=W)

        #Table frame
        table_frame=tb.Frame(Right_frame,bootstyle="dark")
        table_frame.place(x=10,y=5,width=1010,height=650)

        scroll_x=tb.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="primary-round")
        scroll_y=tb.Scrollbar(table_frame,orient=VERTICAL,bootstyle="primary-round")

        #create table 
        self.attendanceReport = tb.Treeview(table_frame,column=("ID","Name","Enroll_No","Date","Time","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,bootstyle='dark')

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="ID")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Enroll_No",text="Enroll.No")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"

        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100,anchor=CENTER)
        self.attendanceReport.column("Name",width=100,anchor=CENTER)
        self.attendanceReport.column("Enroll_No",width=100,anchor=CENTER)
        self.attendanceReport.column("Date",width=100,anchor=CENTER)
        self.attendanceReport.column("Time",width=100,anchor=CENTER)
        self.attendanceReport.column("Attend",width=100,anchor=CENTER)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
#=====================================Function CSV============================
#=========================Fetch Data & Import data =============================
    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReportl.delete(*self.attendanceReportl.get_children())
        for i in rows:
            self.attendanceReportl.insert("",END,values=i)
            print(i)
        
    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=f"\Attendance",title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            next(csvread)
            next(csvread)
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
## ===========================fatch data form mysql attendance================
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from csv_data")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()
##=============================Cursur Function for mysql======================================
    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_time.set(data[4]),
        self.var_date.set(data[3]),
        self.var_AS.set(data[5]) 
#=============================Insert Attendance form csv to my sql============================
    def insert_data(self):
            if not self.attendanceReportl.get_children():
                messagebox.showinfo("Empty", "No data in Table")
            else:
                try:
                    # loop over the Treeview rows and insert them into the database
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    for child in  self.attendanceReportl.get_children():
                        data =  self.attendanceReportl.item(child)["values"]
                        mycursor.execute("INSERT INTO csv_data (Name, Enroll,Date,time,Attendace) VALUES (%s, %s, %s,%s,%s)", data)
                    # commit the changes and close the connection
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
## =============================Delete Attendance form my sql==================================
    # delete selected row from Treeview and MySQL database
    def delete_data(self):
        if not self.attendanceReport.get_children():
                messagebox.showinfo("Empty", "No data in Table")
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                # get selected row ID
                selected_item = self.attendanceReport.selection()[0]
                row_data = self.attendanceReport.item(selected_item)['values']
                id = row_data[0]
                # execute SQL query to delete row from table
                mycursor.execute("DELETE FROM csv_data WHERE id=%s", (id,))
                conn.commit()
                conn.close()
                # delete row from Treeview
                self.attendanceReport.delete(selected_item)
                messagebox.showinfo("Success","Record is Deleted from Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
##===============================update function for mysql database==============================
    def update_data(self):
        if self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_AS.get()=="Select Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    # get selected row ID
                    selected_item = self.attendanceReport.selection()[0]
                    row_data = self.attendanceReport.item(selected_item)['values']
                    id = row_data[0]
                    mycursor.execute("update csv_data set Name=%s,Enroll=%s,Date=%s,Time=%s,Attendace=%s where id=%s",( 
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_date.get(),
                    self.var_time.get(),
                    self.var_AS.get(),
                    id
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
##===============================Function to export data from DB to CSV file=================
    def export_to_csv(self):
        try:
            # Select all rows from table
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM csv_data")
            rows = mycursor.fetchall()
            filename=filedialog.asksaveasfilename(initialdir=f"\Attendance",title="Save CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),defaultextension=".csv",parent=self.root) 
            # Prompt user to select a filename and location to save the CSV file
            if filename:
                try:
                    # Write rows to CSV file
                    with open(filename, 'w', newline='\n') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['ID', 'Name', 'Enroll', 'Date', 'Time', 'Attendance'])
                        for row in rows:
                            writer.writerow(row)
                    messagebox.showinfo("Success", "Data exported to CSV file.")
                except Exception as e:
                    messagebox.showerror("Error", "Failed to export data to CSV file.\n\nError message: {}".format(str(e)))
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
##===============================Reset All Entry Field=======================
    def reset_data(self):
        self.var_name.set("")
        self.var_roll.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_AS.set("Select Status")

if __name__ == "__main__":
    root = tb.Window("Attendace","superhero")
    obj=attendance(root)
    root.mainloop()