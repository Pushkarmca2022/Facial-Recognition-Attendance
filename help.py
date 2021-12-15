from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

from PIL import Image, ImageTk


class helps:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img_top = Image.open(r"D:\python_Tickinter\img\1.jpeg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=55, width=1530, height=720)

        # Frame

        # developer face buttion
        dev_label1 = Label(bg_img, text="Email:Pushakrmca2019@gmail.com", font=(
            "times new roman", 13, "bold"), fg='blue')
        dev_label1.place(x=550, y=260)


if __name__ == "__main__":
    root = Tk()
    obj = helps(root)
    root.mainloop()
