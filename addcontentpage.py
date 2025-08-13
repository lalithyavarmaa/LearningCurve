import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import Tk, Toplevel, Button, Label, Entry, OptionMenu, StringVar, messagebox

class AddContentForm:
    def __init__(self):
        self.add_content_window = Toplevel()
        self.add_content_window.title("Add Content")
        self.add_content_window.geometry("600x400+400+200")
        self.add_content_window.configure(bg="black")
        self.add_content_window.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        padx_value = 20
        pady_value = 10

        branch_label = Label(self.add_content_window, text="Branch:", bg="white")
        branch_label.grid(row=0, column=0, padx=padx_value, pady=pady_value, sticky="w")
        branch_options = ["CSE", "IT", "AI", "ECE", "EEE", "CE", "ME"]
        self.branch_var = StringVar(self.add_content_window)
        self.branch_var.set(branch_options[0])
        branch_dropdown = OptionMenu(self.add_content_window, self.branch_var, *branch_options)
        branch_dropdown.grid(row=0, column=1, padx=padx_value, pady=pady_value, sticky="w")

        year_label = Label(self.add_content_window, text="Year:", bg="white")
        year_label.grid(row=1, column=0, padx=padx_value, pady=pady_value, sticky="w")
        year_options = ["1st", "2nd", "3rd", "4th"]
        self.year_var = StringVar(self.add_content_window)
        self.year_var.set(year_options[0])
        year_dropdown = OptionMenu(self.add_content_window, self.year_var, *year_options)
        year_dropdown.grid(row=1, column=1, padx=padx_value, pady=pady_value, sticky="w")

        self.subject_label = Label(self.add_content_window, text="Subject Name:", bg="white")
        self.subject_label.grid(row=2, column=0, padx=padx_value, pady=pady_value, sticky="w")
        self.subject_entry = Entry(self.add_content_window, bg="white")
        self.subject_entry.grid(row=2, column=1, padx=padx_value, pady=pady_value, sticky="w")

        self.topic_label = Label(self.add_content_window, text="Topic Name:", bg="white")
        self.topic_label.grid(row=3, column=0, padx=padx_value, pady=pady_value, sticky="w")
        self.topic_entry = Entry(self.add_content_window, bg="white")
        self.topic_entry.grid(row=3, column=1, padx=padx_value, pady=pady_value, sticky="w")

        upload_button = Button(self.add_content_window, text="Upload Source", bg='#82447A', fg='white', border=0, command=self.upload_file)
        upload_button.grid(row=4, column=0, columnspan=2, padx=padx_value, pady=pady_value, sticky="we")

        self.source_label = Label(self.add_content_window, text="No file selected", bg="white")
        self.source_label.grid(row=5, column=0, columnspan=2, padx=padx_value, pady=pady_value, sticky="we")

        add_button = Button(self.add_content_window, text="Add", bg='#82447A', fg='white', border=0, command=self.add_content)
        add_button.grid(row=6, column=0, columnspan=2, padx=padx_value, pady=pady_value, sticky="we")

    def upload_file(self):
        self.add_content_window.withdraw()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                                filetypes=(("PDF files", "*.pdf"), ("Word files", "*.docx"), ("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        self.add_content_window.deiconify()
        if file_path:
            self.source_label.config(text=file_path)

    def add_content(self):
        branch = self.branch_var.get()
        year = self.year_var.get()
        subject = self.subject_entry.get()
        topic = self.topic_entry.get()
        source = self.source_label.cget("text")

        if year and subject and topic and source != "No file selected":
            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="password08",
                    database="LearningCurve"
                )

                cursor = db.cursor()

                insert_query = "INSERT INTO content (Branch, SubjectName, TopicName, Year, Source) VALUES (%s, %s, %s, %s, %s)"

                content_data = (branch, subject, topic, year, source)

                cursor.execute(insert_query, content_data)

                db.commit()

                cursor.close()
                db.close()

                messagebox.showinfo("Success", "Content added successfully!")
            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Failed to add content: {error}")
        else:
            messagebox.showerror("Error", "Please fill all fields and upload a file.")