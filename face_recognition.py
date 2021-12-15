from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime


class face_recogition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text=" Face Recognition System", font=(
            "times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img_top = Image.open(r"D:\python_Tickinter\img\11.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=55, width=650, height=700)

        img__bottom = Image.open(r"D:\python_Tickinter\img\20.jpg")
        img__bottom = img__bottom.resize((950, 700), Image.ANTIALIAS)
        self.photoimg__bottom = ImageTk.PhotoImage(img__bottom)

        bg_img = Label(self.root, image=self.photoimg__bottom)
        bg_img.place(x=650, y=55, width=950, height=700)
# button

        b1_1 = Button(bg_img, text="Face RecognitionS", command=self.face_recog,  cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=350, y=600, width=200, height=40)
    # =======================attendance===================

    def mark_attendance(self, r, n,i,d):
        with open("pushkar.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if((r not in name_list)) and (n not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},preset")

        # ===========face recognition=================

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/3000)))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="face")
                my_cursor = conn.cursor()
                print(id)
                
                
                
                
                my_cursor.execute("select name from student where id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                my_cursor.execute("select roll from student where id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("select dep from student where id="+str(id))
                zp = my_cursor.fetchone()
                zp = "+".join(zp)

               

                if confidence > 77:
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(r, n,id,zp)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_recogition(root)
    root.mainloop()
