from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from main import Face_Recognition_System


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x720+0+0")
        # First
        img = Image.open(r"D:\python_Tickinter\img\12.jpg")
        img = img.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)
        reg_lable=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        reg_lable.place(x=20,y=20)



if __name__ == '__main__':
    root = Tk()
    app = register(root)
    root.mainloop()
