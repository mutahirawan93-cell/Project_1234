from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
 

class Face_Recognition_System:

        def __init__(self):
                self.root = root
                self.root.geometry("1530x790+0+0")
                self.root.title("Attendance System using Face Recognition For Student")
        
# First img
        img = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/university.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.Photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.Photoimage)
        f_lbl.place(x=0, y=0, width=500, height=130)

# second img
        img1 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/facial.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=500, y=0, width=500, height=130)

# third img
        img2 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/recognition.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=1000, y=0, width=550, height=130)
        
# bg-img
        img3 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/background.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE SYSTEM USING FACE RECOGNITION", font=("time new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

# Student button
        img4 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/student portal.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimage4, command=self.student_portals, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Students Portals", command=self.student_portals, cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

# Detect face button
        img5 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/facial recognition.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimage5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        # Attendance face button
        img6 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/Attendance.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimage6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

# help button
        img7 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/helpdesk.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimage7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # train face button
        img8 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/train data")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimage8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

# Photos button
        img9 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images /photos.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimage9, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)
# Developer button
        img10 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images/developer.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimage10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)
# Exit button
        img11 = Image.open(r"C:\Users\Admin\Desktop\Attendance System using  Face Recognition\Images /exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimage11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimage11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("time new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)


#================Functions buttons===============
def student_portals(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        

if __name__ == "__main__":
   root = Tk()
   obj = Face_Recognition_System(root)
   root.mainloop()
 
