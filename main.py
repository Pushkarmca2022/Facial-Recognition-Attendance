from tkinter import *
from tkinter import ttk
import tkinter
import tkinter
from datetime import datetime
from PIL import Image, ImageTk
from student import Face_student_System
import os
from train import train
from face_recognition import face_recogition
from attendance import attendace
from developer import developer
from help import helps


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # First
        img = Image.open(r"D:\python_Tickinter\img\11.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second
        img1 = Image.open(r"D:\python_Tickinter\img\12.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # threed
        img2 = Image.open(r"D:\python_Tickinter\img\11.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)
        # bg imgages
        img3 = Image.open(r"D:\python_Tickinter\img\20.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=45)
        # ========================time=============

        # def time():
        #     string = strftime('%H:%M:%S %p')
        #     title_lbl.config(text=string)
        #     title_lbl.after(1000, time)

        # Student button
        img4 = Image.open(r"D:\python_Tickinter\img\16.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        # Detect face button
        img5 = Image.open(r"D:\python_Tickinter\img\11.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Label(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Detect face button", command=self.face_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        # Attendace face button
        img6 = Image.open(r"D:\python_Tickinter\img\21.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Label(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendace face ", command=self.atten_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        # Help face button
        img8 = Image.open(r"D:\python_Tickinter\img\23.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Label(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Dest", command=self.helps_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        # Train face button
        img9 = Image.open(r"D:\python_Tickinter\img\20.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Label(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=200, y=350, width=220, height=200)

        b1_1 = Button(bg_img, text="Train Data", command=self.trains, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=540, width=220, height=40)
        # photo face button
        img10 = Image.open(r"D:\python_Tickinter\img\2.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Label(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=500, y=350, width=220, height=200)

        b1_1 = Button(bg_img, command=self.open_img, text="Photos", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=540, width=220, height=40)
        # Developer
        img11 = Image.open(r"D:\python_Tickinter\img\12.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Label(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=800, y=350, width=220, height=200)

        b1_1 = Button(bg_img, text="Developer", command=self.develop_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=540, width=220, height=40)
        # Exit
        img12 = Image.open(r"D:\python_Tickinter\img\22.jpg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Label(bg_img, image=self.photoimg12, cursor="hand2")
        b1.place(x=1100, y=350, width=220, height=200)

        b1_1 = Button(bg_img, text="Exit", command=self.iExit, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=540, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

        # *************Furncton button***********

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_student_System(self.new_window)

    def trains(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recogition(self.new_window)

    def atten_data(self):
        self.new_window = Toplevel(self.root)
        self.app = attendace(self.new_window)

    def develop_data(self):
        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)

    def helps_data(self):
        self.new_window = Toplevel(self.root)
        self.app = helps(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
