from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

import os
import numpy as np
import cv2


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img_top = Image.open(r"D:\python_Tickinter\img\12.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=55, width=1530, height=325)

        img__bottom = Image.open(r"D:\python_Tickinter\img\19.jpg")
        img__bottom = img__bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg__bottom = ImageTk.PhotoImage(img__bottom)

        bg_img = Label(self.root, image=self.photoimg__bottom)
        bg_img.place(x=0, y=440, width=1530, height=325)
# button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier,  cursor="hand2", font=(
            "times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ===============train the classir5e and ========
        clf = cv2.face.LBPHFaceRecognizer_create()
        #clf = cv2.face.createLBPHFaceRecognizer()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("restul", "train dtasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()
