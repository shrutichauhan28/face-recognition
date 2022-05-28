from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendace import Attendance


class Face_Recognization_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x720+0+0")
        self.root.title("Face recognization")

        img = Image.open(
            r"images\bak.jfif")
        img = img.resize((1500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1500, height=130)

        # ...........background img...........
        img3 = Image.open(
            r"images\bak.jfif")
        img3 = img3.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=710)

        # ...........titlebox...........
        title_lbl = Label(bg_img, text="Face Recognition Attendance System", font=(
            "Merriweather", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1500, height=45)

       # Topbutton1..attendance....
        img4 = Image.open(
            r"images\cap.png")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.studentdetails, cursor="hand2")
        b1.place(x=200, y=200, width=180, height=180)

        b1_1 = Button(bg_img, text="Student Details", command=self.studentdetails, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=200, y=350, width=180, height=30)

        # trainbutton.....Train.......
        img8 = Image.open(
            r"images\robii2.png")
        img8 = img8.resize((180, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    command=self.train_pannels, cursor="hand2")
        b1.place(x=500, y=200, width=180, height=180)

        b1_1 = Button(bg_img, text="Train", command=self.train_pannels, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=500, y=350, width=180, height=30)

        # Topbutton2.....Facedetect.....
        img5 = Image.open(
            r"images\facee.png")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    command=self.face_rec, cursor="hand2")
        b1.place(x=800, y=200, width=180, height=180)

        b1_1 = Button(bg_img, text="Face Detector", command=self.face_rec, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=800, y=350, width=180, height=30)

        # Topbutton3........Attendnce.....
        img6 = Image.open(
            r"images\att1.png")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    command=self.attendance_data, cursor="hand2")
        b1.place(x=1100, y=200, width=180, height=180)

        b1_1 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1100, y=350, width=180, height=30)

    # ==============Function buttons==================

    def studentdetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def iexit(self):
        self.iexit = tkinter.messagebox.askyesno(
            "Face recognition", "Are you sure want to exit", parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization_system(root)
    root.mainloop()
