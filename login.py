from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from main import Face_Recognition_System
from register import register
from forgespass import forgespass


class Login_window:
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
      # secon image
        img1 = Image.open(r"D:\python_Tickinter\img\30.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "time new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        username_lbl = Label(frame, text="username", font=(
            "time new roman", 15, "bold"), fg='white', bg='black')
        username_lbl.place(x=70, y=155)

        self.textuser = Entry(frame, font=(
            "time new roman", 15, "bold"))
        self.textuser.place(x=40, y=200, width=270)

        # label2
        username_lbl = Label(frame, text="password", font=(
            "time new roman", 15, "bold"), fg='white', bg='black')
        username_lbl.place(x=70, y=255)

        self.textpass = Entry(frame, font=(
            "time new roman", 15, "bold"))
        self.textpass.place(x=40, y=300, width=270)
# Login
        loginbtn = Button(frame, text="Login", command=self.login, font=(
            "time new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activebackground="red", activeforeground="white")

        loginbtn.place(x=110, y=350, width=120, height=35)
        # register
        regbtn = Button(frame, text="New User Register", command=self.register, font=(
            "time new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")

        regbtn.place(x=20, y=390, width=160)

        # forgespass
        regbtn = Button(frame, text="Forget Password", command=self.forepass, font=(
            "time new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")

        regbtn.place(x=20, y=410, width=160)

    def login(self):
        if self.textuser.get() == "pk" and self.textpass.get() == "123":
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)
        #elif:
             #messagebox.showinfo("Invalid","Invalid user and password")
         #    print("aaaa")

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)

    def forepass(self):
        self.new_window = Toplevel(self.root)
        self.app = forgespass(self.new_window)


if __name__ == '__main__':
    root = Tk()
    app = Login_window(root)
    root.mainloop()
