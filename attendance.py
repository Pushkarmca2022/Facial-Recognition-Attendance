from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

import os
import numpy as np
import cv2
import csv
from tkinter import filedialog

mydata = []


class attendace:
    def __init__(self, root):
        self.root = root

        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_depart = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_roll = StringVar()

        img = Image.open(r"D:\python_Tickinter\img\11.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)
        # Second
        img1 = Image.open(r"D:\python_Tickinter\img\12.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)
# bg images
        img3 = Image.open(r"D:\python_Tickinter\img\20.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1320, heigh=510)
        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=490)
        class_student_frame = LabelFrame(
            left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course InFormation", font=(
                "times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=160, width=650, height=300)

        # Attendanceld
        studentid_lable = Label(class_student_frame, text="Attendanceld:", font=(
            "times new roman", 12, "bold"))
        studentid_lable.grid(row=0, column=0, padx=10, sticky=W)
        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1)
        # roll
        studentname_lable = Label(class_student_frame, text="roll:", font=(
            "times new roman", 12, "bold"))
        studentname_lable.grid(row=0, column=2, padx=10, sticky=W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # name
        class_div_lable = Label(class_student_frame, text="Name:", font=(
            "times new roman", 12, "bold"))
        class_div_lable.grid(row=1, column=0, padx=10, sticky=W)
        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=1, column=1)
        # Department
        roll_no_lable = Label(class_student_frame, text="Department:", font=(
            "times new roman", 12, "bold"))
        roll_no_lable.grid(row=1, column=2, padx=10, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_depart, width=20, font=(
            "times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, sticky=W)
        # student Grender
        

        
        # time
        dob_lable = Label(class_student_frame, text="Time", font=(
            "times new roman", 12, "bold"))
        dob_lable.grid(row=2, column=0, padx=10,  pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_time, width=20, font=(
            "times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=1, padx=5, pady=5,  sticky=W)
        # Date

        email_lable = Label(class_student_frame, text="Date:", font=(
            "times new roman", 12, "bold"))
        email_lable.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_date, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=2, column=3, padx=5,  pady=5, sticky=W)

        # student Grender
        class_div_lable = Label(class_student_frame, text="Attendance Status:", font=(
            "times new roman", 12, "bold"))
        class_div_lable.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        dep_combo1 = ttk.Entry(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"))
       
        dep_combo1.grid(row=3, column=1, padx=2, pady=10)

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=640, height=70)

        # save
        save_btn = Button(btn_frame,  text="ImportCsv", command=self.importCsv, width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        save_btn.grid(row=0, column=0)
        # Exportcsv
        update_btn = Button(btn_frame, command=self.exportcsv,  text="Exportcsv", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)
        # delete
        delete_btn = Button(btn_frame, text="Update", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)
        # reset
        reset_btn = Button(btn_frame, command=self.reset_data,  text="Rest", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=230, width=640, height=70)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=690, y=10, width=600, height=490)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=110, width=600, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame, column=("dep", "course", "year", "sem", "id", "name", "divison", "roll", "gen", "dob", "email", "phone", "address", "teacher", "photo"))
          
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Student Id")
        self.student_table.heading("course", text="Roll Number")
        self.student_table.heading("year", text="Name")
        self.student_table.heading("sem", text="Depart Name")
        self.student_table.heading("id", text="Time")
        self.student_table.heading("name", text="Date")
        self.student_table.heading("divison", text="Status")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gen", text="GEN")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="PHONE")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PHOTO")
        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("divison", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gen", width=100)

        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        #self.fetch_data()
        #self.student_table.pack(fill=BOTH, expand=1)
        #self.student_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)

        

    def importCsv(self):

        global mydata
        mydata.clear()

        fin = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV file", "*csv"), ("All file", "*.*")),  parent=self.root)

        with open(fin) as myfile:
            csvreads = csv.reader(myfile, delimiter=",")
            for i in csvreads:
                mydata.append(i)

            self.fetchData(mydata)

    # export csv
    def exportcsv(self):
        try:

            if len(mydata) < 1:
                messagebox.showerror("No Data", "No datq foned to export")
                return False
            fin = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV file", "*csv"), ("All file", "*.*")),  parent=self.root)
            with open(fin, mode="w", newline="\n")as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "you data Exported")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        rows = content['values']
        self.var_std_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_std_name.set(rows[2])
        self.var_depart.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_gender.set(rows[6])

    def reset_data(self):
        self.var_std_id.set("")
        self.var_roll.set("")
        self.var_std_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_gender.set("")


if __name__ == "__main__":
    root = Tk()
    obj = attendace(root)
    root.mainloop()
