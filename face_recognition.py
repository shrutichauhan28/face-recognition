from tkinter import*
import re
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Face_recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face recognition Panel")

        title_lbl = Label(self.root, text="Face Recognition", font=(
            "times new roman", 25, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=60)

        # backgorund image
        bg1 = Image.open(r"images\gui.jpg")
        bg1 = bg1.resize((1550, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=60, width=1550, height=768)

        # button

        std_img_btn = Image.open(r"images\fact.webp")
        std_img_btn = std_img_btn.resize((400, 280), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog,
                        image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=400, height=280)

        b1_1 = Button(bg_img, text="Face detect", command=self.face_recog,
                      cursor="hand2", font=(
                          "times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=600, y=440, width=400, height=40)

        # =====================Attendance===================

    def mark_attendance(self, i, r, s, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((s not in name_list)) and ((d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {s},{d}, {dtString}, {d1}, Present")

        # =========================Face recognition===================

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    username='root', password='Mysql123', host='localhost', database='face_recognization')
                my_cursor = conn.cursor()
                t = "+"

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                s = my_cursor.fetchone()
                s = str(id)
                s = t.join(s)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = str(id)
                r = t.join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = str(id)
                d = t.join(d)

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = str(id)
                i = t.join(i)

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Name:{s}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Dep:{d}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, s, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y-5),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

                return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
