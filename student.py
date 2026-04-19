from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTK
from tkinter import messagebox



class Student:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System Using Face Recognition")
#==============Variable===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_subject=StringVar()
        self.var_registration=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_teacher=StringVar()

        #First img
        img=Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/student in class.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTK.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#second img
        img1=Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/studentjpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTK.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

#third img
        img2=Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/recognition.jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
        self.photoimg2=ImageTK.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg-img
        img3=Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/student background.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTK.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Portal",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/student background.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTK.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

          # Current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

# Department
        dep_label=Label(current_course_frame,text="Department",font=("time new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="read only",width=20)
        
        dep_combo["values"]=("Select Department","Computer Science","Civil Engineering","Pharmacy","BBA","DPT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
#course
        Course_label=Label(current_course_frame,text="Course",font=("time new roman",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course ,font=("time new roman",13,"bold"),state="read only",width=20)
        
        Course_combo["values"]=("Select Course","AI","SE","CBSP","BSCE","B.Pharm","Physical Therapists")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#year
        year_label=Label(current_course_frame,text="Year",font=("time new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",13,"bold"),state="read only",width=20)
        
        year_combo["values"]=("Select Year","2020-21","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#Semester
        
        semester_label=Label(current_course_frame,text="Semester",font=("time new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",13,"bold"),state="read only",width=20)
        
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

#StudentId
        
        studentId_label=Label(class_student_frame,text="Student ID:",font=("time new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("time new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#Student name
        
        studentName_label=Label(class_student_frame,text="Student Name:",font=("time new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("time new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

# Subject
        
        class_Subject_label=Label(class_student_frame,text="Subject:",font=("time new roman",13,"bold"),bg="white")
        class_Subject_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_Subject_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_subject,font=("time new roman",13,"bold"))
        class_Subject_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Registration No
        
        roll_no_label=Label(class_student_frame,text="Registration No:",font=("time new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_registration,font=("time new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
#Gender
        
        gender_label=Label(class_student_frame,text="Gender:",font=("time new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("time new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
#DOB
        
        dob_label=Label(class_student_frame,text="DOB:",font=("time new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("time new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#Email
        
        email_label=Label(class_student_frame,text="Email:",font=("time new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("time new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

 #Phone No
        
        phone_label=Label(class_student_frame,text="Phone No:",font=("time new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("time new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

 #Address
        
        address_label=Label(class_student_frame,text="Address:",font=("time new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("time new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
#Teacher Name
        
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("time new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry= ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("time new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


# Radio Buttons
        self.var_radio1=StringVar()

        radiobtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)


        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio2,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

#Button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Portal",font=("time new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)

        img_right=Image.open(r"C:\Users\Mega Providers\Desktop\Attendance system using face recognition\images/student background.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTK.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
#  ============Search System===========================
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("time new roman",15,"bold"),bg="orange",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",13,"bold"),state="read only",width=15)
        
        search_combo["values"]=("Select","Registration No","First Name","Email","Phone No:")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry= ttk.Entry(search_frame,width=15,font=("time new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=8,font=("time new roman",12,"bold"),bg="darkgreen",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("time new roman",12,"bold"),bg="darkgreen",fg="white")
        showAll_btn.grid(row=0,column=4)

 # ================table frame=====================

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","semester","name","id","subject","registration","gender","dob","email","gender","phone no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("registration",text="Registration")
        self.student_table.heading("subject",text="Subject")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo SampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("registration",width=100)
        self.student_table.column("subject",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)

#==============Function decration============== 
 
    def add_data(self):
       if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.var_std_id.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
         pass
         
          






if __name__== "__main__":
 root=Tk()
 obj= Student(root)
 root.mainloop()


