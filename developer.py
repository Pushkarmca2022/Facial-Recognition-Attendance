from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

from PIL import Image, ImageTk


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Developer", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img_top = Image.open(r"D:\python_Tickinter\img\12.png")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=55, width=1530, height=720)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=900, y=0, width=500, height=550)

        img_top1 = Image.open(r"D:\python_Tickinter\img\30.png")
        img_top1 = img_top1.resize((300, 300), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        bg_img = Label(main_frame, image=self.photoimg_top1)
        bg_img.place(x=250, y=0, width=200, height=200)

        dev_label = Label(main_frame, text="Hello My name,Pushkar", font=(
            "times new roman", 13, "bold"))
        dev_label.place(x=0, y=5)
        dev_label1 = Label(main_frame, text="I am full stack developer", font=(
            "times new roman", 13, "bold"))
        dev_label1.place(x=0, y=40)

        # developer face buttion

        img_top2 = Image.open(r"D:\python_Tickinter\img\1.jpeg")
        img_top2 = img_top2.resize((500, 300), Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        bg_img = Label(main_frame, image=self.photoimg_top2)
        bg_img.place(x=0, y=210, width=500, height=300)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
