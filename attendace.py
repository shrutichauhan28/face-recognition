from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x690+0+0")
        self.root.title("Attendance")

        # -----------TextVariables-------------------
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend = StringVar()

        # This part is image labels setting start
        # first header image
        img = Image.open(
            r"images\lil.png")
        img = img.resize((1550, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1550, height=130)

        # backgorund image
        bg1 = Image.open(r"images\lil.png")
        bg1 = bg1.resize((1550, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1550, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Attendance Panel", font=(
            "verdana", 30, "bold"), bg="white", fg="purple")
        title_lb1.place(x=0, y=0, width=1550, height=45)

        # ========================Section Creating==================================

        # Creating Frame
        main_frame = Frame(bg_img, bd=2, bg="white")  # bd mean border
        main_frame.place(x=5, y=55, width=1550, height=720)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("verdana", 12, "bold"), fg="black")
        left_frame.place(x=10, y=10, width=700, height=480)

        # ==================================Text boxes and Combo Boxes====================

        # Student id
        studentId_label = Label(
            left_frame, text="Std-ID:", font=("verdana", 12, "bold"), fg="purple", bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(
            left_frame, textvariable=self.var_id, width=15, font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student Roll
        student_roll_label = Label(left_frame, text="Roll.No:", font=(
            "verdana", 12, "bold"), fg="purple", bg="white")
        student_roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(
            left_frame, textvariable=self.var_roll, width=15, font=("verdana", 12, "bold"))
        student_roll_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Student Name
        student_name_label = Label(
            left_frame, text="Std-Name:", font=("verdana", 12, "bold"), fg="purple", bg="white")
        student_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        student_name_entry = ttk.Entry(
            left_frame, textvariable=self.var_name, width=15, font=("verdana", 12, "bold"))
        student_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        dep_label = Label(left_frame, text="Department:", font=(
            "verdana", 12, "bold"), fg="purple", bg="white")
        dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        dep_entry = ttk.Entry(
            left_frame, textvariable=self.var_dep, width=15, font=("verdana", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # time
        time_label = Label(left_frame, text="Time:", font=(
            "verdana", 12, "bold"), fg="purple", bg="white")
        time_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(
            left_frame, textvariable=self.var_time, width=15, font=("verdana", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Date
        date_label = Label(left_frame, text="Date:", font=(
            "verdana", 12, "bold"), fg="purple", bg="white")
        date_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(
            left_frame, textvariable=self.var_date, width=15, font=("verdana", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Attendance
        student_attend_label = Label(
            left_frame, text="Attendance-status:", font=("verdana", 12, "bold"), fg="purple", bg="white")
        student_attend_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        attend_combo = ttk.Combobox(left_frame, textvariable=self.var_attend, width=13, font=(
            "verdana", 12, "bold"), state="readonly")
        attend_combo["values"] = ("Status", "Present", "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # =========================button section========================

        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=690, height=60)

        # Import button
        save_btn = Button(btn_frame,  command=self.importCsv,
                          text="Import CSV", width=12, font=(
                              "verdana", 12, "bold"), fg="white", bg="black")
        save_btn.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        # Export button
        update_btn = Button(btn_frame,  command=self.exportCsv,
                            text="Export CSV", width=12, font=(
                                "verdana", 12, "bold"), fg="white", bg="black")
        update_btn.grid(row=0, column=1, padx=6, pady=8, sticky=W)

        # Update button
        del_btn = Button(btn_frame,  # command=self.action,
                         text="Update", width=12, font=(
                             "verdana", 12, "bold"), fg="white", bg="black")
        del_btn.grid(row=0, column=2, padx=6, pady=10, sticky=W)

        # reset button
        reset_btn = Button(btn_frame,  command=self.reset_data,
                           text="Reset", width=12, font=(
                               "verdana", 12, "bold"), fg="white", bg="black")
        reset_btn.grid(row=0, column=3, padx=6, pady=10, sticky=W)

        # Right section=======================================================

        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("verdana", 12, "bold"), fg="black")
        right_frame.place(x=720, y=10, width=620, height=480)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame
        # Searching System in Right Label Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=600, height=360)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # create table
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        # ===========width_table===============

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

        # ===========Face_Data=================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

 # =-================Import csvv===========
    def importCsv(self, event=""):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln)as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # =-================Import csvv===========
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="")as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo(
                        "Data Export", "Your data exported to "+os.path.basename(fln)+"\nsuccessfully.")
        except Exception as es:
            messagebox.showerror(
                "Error", f"due to:{str(es)}", parent=self.root)

            # =========cursor========

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]

        self.var_id.set(rows[0])
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attend.set(rows[6])

        # reset.........

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
