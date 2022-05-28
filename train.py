from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox


class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Panel")

        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=40)

        img_top = Image.open(
            r"images\face-off-banner.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1530, height=720)

        # train button

        std_img_btn = Image.open(r"images\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(f_lbl, command=self.train_classifier,
                        image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=400, height=280)

        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="white", fg="blue")
        b1_1.place(x=600, y=490, width=400, height=60)

    def train_classifier(self):
        data_dir = ("Dataimgs")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale img
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ====================Train classifier==============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training Dataset Completed!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
