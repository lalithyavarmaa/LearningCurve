import mysql.connector
from tkinter import *
from tkinter import messagebox
import os
from addcontentpage import AddContentForm

class ContentPage:
    def __init__(self, branch_name):
        self.education_window = Tk()
        self.education_window.title("Content Page")
        self.education_window.geometry('1000x550+200+75')
        self.education_window.configure(bg="black")
        self.education_window.resizable(False, False)

        self.branch_name = branch_name

        self.setup_ui()

    def setup_ui(self):
        self.search_frame = Frame(self.education_window, bg="black")
        self.search_frame.pack(pady=10)

        self.search_label = Label(self.search_frame, text="Search Content:", bg="black", fg="white", font=("Arial", 12))
        self.search_label.grid(row=0, column=0, padx=10, pady=5)

        self.search_entry = Entry(self.search_frame, bg="white", fg="black", font=("Arial", 12))
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = Button(self.search_frame, text="Search", bg='#82447A', fg='white', border=0, command=self.search_content)
        self.search_button.grid(row=0, column=2, padx=10, pady=5)

        self.contents_frame = Frame(self.education_window, bg="black")
        self.contents_frame.pack(pady=10)

        self.content_label = Label(self.contents_frame, text=f"Contents for {self.branch_name}:", bg="black", fg="white", font=("Arial", 21, "bold"))
        self.content_label.grid(row=0, column=0, padx=10, pady=5)

        self.content_headers = ["Sno", "Branch", "Subject Name", "Topic Name", "Year", "Source"]

        self.fetch_content_data()

        self.add_content_button = Button(self.education_window, text="Add Content", bg='#82447A', fg='white', border=0, command=self.add_content_form, font=("Arial", 12))
        self.add_content_button.pack(pady=10)

        self.back_button = Button(self.education_window, text="Back", bg='#82447A', fg='white', border=0, command=self.go_back)
        self.back_button.pack()
        self.back_button.place(x=10, y=10)

    def fetch_content_data(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password08",
                database="LearningCurve"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM content WHERE `Branch`=%s", (self.branch_name,))
            content_data = cursor.fetchall()
            cursor.close()
            db.close()

            self.display_content(content_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch content data: {e}")

    def display_content(self, content_data):
        for widget in self.contents_frame.winfo_children():
            widget.destroy()

        for i, header in enumerate(self.content_headers):
            header_label = Label(self.contents_frame, text=header, bg="black", fg="white", font=("Arial", 12, "bold"))
            header_label.grid(row=1, column=i, padx=10, pady=5)

        def open_file(file_path):
            try:
                os.startfile(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

        for i, row in enumerate(content_data, start=2):
            for j, value in enumerate(row):
                if j == 5: 
                    file_name = os.path.basename(value) 
                    source_label = Label(self.contents_frame, text=file_name, bg="black", fg="white", font=("Arial", 10), cursor="hand2")
                    source_label.grid(row=i, column=j, padx=10, pady=5)
                    source_label.bind("<Button-1>", lambda event, file_path=value: open_file(file_path))
                else:
                    label = Label(self.contents_frame, text=value, bg="black", fg="white", font=("Arial", 10))
                    label.grid(row=i, column=j, padx=10, pady=5)

    def search_content(self):
        query = self.search_entry.get().lower()
        if query.strip() == "":
            self.fetch_content_data()
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password08",
                database="LearningCurve"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM content WHERE LOWER(Sno) LIKE %s OR LOWER(Subject Name) LIKE %s OR LOWER(Topic Name) LIKE %s OR LOWER(Year) LIKE %s AND `Branch`=%s", ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%', self.branch_name))
            content_data = cursor.fetchall()
            cursor.close()
            db.close()

            self.display_content(content_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search content: {e}")

    def add_content_form(self):
        add_content_form = AddContentForm()

    def go_back(self):
        self.education_window.destroy()

    def run(self):
        self.education_window.mainloop()

