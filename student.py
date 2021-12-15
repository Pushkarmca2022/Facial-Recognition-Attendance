from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

from PIL import Image, ImageTk


class Face_student_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition SystemS")
        # ***********Variables**************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        

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

        title_lbl = Label(bg_img, text="Student Management System", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1320, heigh=510)
        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=490)
# ////////////////////////////////////////////////////////////
        # Current course  Information
        current_course_frame = LabelFrame(
            left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course InFormation", font=(
                "times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=5, width=650, height=150)
        # Department
        dep_lable = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"))
        dep_lable.grid(row=0, column=0)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="read only")
        dep_combo["values"] = ("Select Department", "coumputer", "it")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)
        # course
        dep_lable = Label(current_course_frame, text="couser", font=(
            "times new roman", 12, "bold"))
        dep_lable.grid(row=0, column=2)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="read only")
        dep_combo["values"] = ("Select course", "MCA", "BCA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        dep_lable = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"))
        dep_lable.grid(row=1, column=0)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="read only")
        dep_combo["values"] = ("Select Year", "2019", "2020")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, padx=2, pady=10)
        # Semester
        dep_lable = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"))
        dep_lable.grid(row=1, column=2)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="read only")
        dep_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # class Student informtation
        class_student_frame = LabelFrame(
            left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course InFormation", font=(
                "times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=160, width=650, height=300)
        # student id
        studentid_lable = Label(class_student_frame, text="StudentID:", font=(
            "times new roman", 12, "bold"))
        studentid_lable.grid(row=0, column=0, padx=10, sticky=W)
        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1)
        # student name
        studentname_lable = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 12, "bold"))
        studentname_lable.grid(row=0, column=2, padx=10, sticky=W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        # student didvision
        class_div_lable = Label(class_student_frame, text="didvision:", font=(
            "times new roman", 12, "bold"))
        class_div_lable.grid(row=1, column=0, padx=10, sticky=W)
        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=1, column=1)
        # roll no
        roll_no_lable = Label(class_student_frame, text="Roll no:", font=(
            "times new roman", 12, "bold"))
        roll_no_lable.grid(row=1, column=2, padx=10, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, sticky=W)
# /////////////////////////
        # student Grender
        class_div_lable = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 12, "bold"))
        class_div_lable.grid(row=2, column=0, padx=10, pady=5, sticky=W)
      #  studentid_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_gender, font=(
       #     "times new roman", 12, "bold"))
       # studentid_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        dep_combo1 = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="read only")
        dep_combo1["values"] = ("Select Department", "Male", "FaMale", "Other")
        dep_combo1.current(0)
        dep_combo1.grid(row=2, column=1, padx=2, pady=10)
        # DOB
        dob_lable = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 12, "bold"))
        dob_lable.grid(row=2, column=2, padx=10,  pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5,  sticky=W)
       # Email

        email_lable = Label(class_student_frame, text="Email:", font=(
            "times new roman", 12, "bold"))
        email_lable.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=5,  pady=5, sticky=W)
        # Phone No:
        phone_lable = Label(class_student_frame, text="Phone No:", font=(
            "times new roman", 12, "bold"))
        phone_lable.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5,  sticky=W)
        # Address
        address_lable = Label(class_student_frame, text="Address:", font=(
            "times new roman", 12, "bold"))
        address_lable.grid(row=4, column=0, padx=10, pady=5,  sticky=W)
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        # Teacher Nmae:
        teacher_lable = Label(class_student_frame, text="Teacher", font=(
            "times new roman", 12, "bold"))
        teacher_lable.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=(
            "times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # radio button
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(
            class_student_frame,  variable=self.var_radio1,text="Y", value="yes")
        Radiobutton1.grid(row=5, column=1,padx=5, pady=5)
       
        Radiobutton2 = ttk.Radiobutton(
            class_student_frame,variable=self.var_radio1, text="No", value="No")
        Radiobutton2.grid(row=5, column=2)

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=640, height=70)
# save
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        save_btn.grid(row=0, column=0)
        # Update
        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)
        # delete
        delete_btn = Button(btn_frame, command=self.delete_data, text="delete", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)
        # reset
        reset_btn = Button(btn_frame, command=self.reset_data, text="Rest", width=15, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=230, width=640, height=70)
# Take photo Sample
        take_photo_btn = Button(btn_frame1, text="Take photo Sample", command=self.generate_data, width=35, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        take_photo_btn.grid(row=0, column=0)
        # update photo sameple
        update_photo_btn = Button(btn_frame1, text="Update photo Sameple", width=35, font=(
            "times new roman", 13, "bold"), bg='blue', fg='white')
        update_photo_btn.grid(row=0, column=1)


# /////////////////////////////////////
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=690, y=10, width=600, height=490)


# ////////////////////////////////////////////////////////////
        # *******************Serach System********************
        search_frame = LabelFrame(Right_frame, bd=2, bg='white', relief=RIDGE, text="Search System", font=(
            "times new roman", 12, "bold"))
        search_frame.place(x=5, y=10, width=580, height=100)

        search_lable = Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="red")
        search_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="read only")
        search_combo["values"] = ("Select ", "Roll_No", "Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "times new roman", 12, "bold"), bg='blue')
        search_btn.grid(row=0, column=3)
        showAll_btn = Button(search_frame, text="Show All", width=12, font=(
            "times new roman", 12, "bold"), bg='blue')
        showAll_btn.grid(row=1, column=3)
        # **************table frame*********************
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
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="semester")
        self.student_table.heading("id", text="Studnetid")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("divison", text="Divison")
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
        self.fetch_data()

    # ***************Function decreattion******************
    def add_data(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror(
                "Error", "All files are required", parent=self.root)
        else:
           # messagebox.showinfo( "Success", "Welcom Code with", parent=self.root)
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(
                    ),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(
                   ),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student add", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "error", f"Due to:{str(es)}", parent=self.root)
    # **********fatch dta********

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="face")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

            conn.commit()
        conn.close()
# ==============get cursor===============

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
		#self.var_radio1.set(data[14])

# =================Update cursor========
    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="", database="face")
            my_cursor = conn.cursor()
            my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,id=%s,name=%s,divison=%s,roll=%s,gen=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s where id=%s",
                              (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(
                    ),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(
                   ),self.var_teacher.get(),self.var_std_id.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)

# ==============deleter=funtion======
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "error", "student id musti br required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Studnet deleter page", "Do you want to delter", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="face")
                    my_cursor = conn.cursor()

                    sql = "delete from student where id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Delere", "successfull", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

# ==============rest==============
    def reset_data(self):
        self.var_dep.set("Select Department")
    
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
    # ==============Generrate data set or take photo smaple==============

    def generate_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="", database="face")
            my_cursor1 = conn.cursor()
            my_cursor1.execute("select * from student")
            myresult = my_cursor1.fetchall()
            id = 0
            for x in myresult:
                id += 1
            my_cursor1.execute("update student set dep=%s,course=%s,year=%s,sem=%s,id=%s,name=%s,divison=%s,roll=%s,gen=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where id=%s",
                              (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(
                    ),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(
                   ),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            # ====Load preifind data on face =====
            face_classifier = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml")

            def face_cropped(img):
                print("-1-1-1-")
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                for(x, y, w, h) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            print("111")
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1

                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    print("44")
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    print("55555555")
                    file_name_path = "data/user." + \
                        str(id)+"."+str(img_id)+".jpg"
                    print("6666")
                    cv2.imwrite(file_name_path, face)
                    print("222222")
                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Crooped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("restu", "Genereting data sets commled!!!!!")

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due 444 to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_student_System(root)
    root.mainloop()
