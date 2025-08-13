import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from content import ContentPage
class EducationPage:
    def __init__(self):
        self.root = Tk()
        self.root.title('Education PAGE')
        self.root.geometry('1000x550+200+75')
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.image_frame = Frame(self.root, bg='black')
        self.image_frame.pack()

        self.img_cse = PhotoImage(file='images/CSE.png')
        self.img_it = PhotoImage(file='images/IT.png')
        self.img_ai = PhotoImage(file='images/AI.png')
        self.img_ece = PhotoImage(file='images/ECE.png')
        self.img_eee = PhotoImage(file='images/EEE.png')
        self.img_ce = PhotoImage(file='images/CE.png')
        self.img_me = PhotoImage(file='images/ME.png')

        self.label_cse = Label(self.image_frame, image=self.img_cse, bg='black', cursor="hand2")
        self.label_it = Label(self.image_frame, image=self.img_it, bg='black', cursor="hand2")
        self.label_ai = Label(self.image_frame, image=self.img_ai, bg='black', cursor="hand2")
        self.label_ece = Label(self.image_frame, image=self.img_ece, bg='black', cursor="hand2")
        self.label_eee = Label(self.image_frame, image=self.img_eee, bg='black', cursor="hand2")
        self.label_ce = Label(self.image_frame, image=self.img_ce, bg='black', cursor="hand2")
        self.label_me = Label(self.image_frame, image=self.img_me, bg='black', cursor="hand2")

        self.label_cse.grid(row=0, column=0, padx=15, pady=15)
        self.label_it.grid(row=0, column=1, padx=15, pady=15)
        self.label_ai.grid(row=0, column=2, padx=15, pady=15)
        self.label_ece.grid(row=1, column=0, padx=15, pady=15)
        self.label_eee.grid(row=1, column=1, padx=15, pady=15)
        self.label_ce.grid(row=1, column=2, padx=15, pady=15)
        self.label_me.grid(row=2, column=1, padx=15, pady=15)

        self.label_cse.bind("<Button-1>", lambda event, branch_name="CSE": self.open_topics_page(branch_name))
        self.label_it.bind("<Button-1>", lambda event, branch_name="IT": self.open_topics_page(branch_name))
        self.label_ai.bind("<Button-1>", lambda event, branch_name="AI": self.open_topics_page(branch_name))
        self.label_ece.bind("<Button-1>", lambda event, branch_name="ECE": self.open_topics_page(branch_name))
        self.label_eee.bind("<Button-1>", lambda event, branch_name="EEE": self.open_topics_page(branch_name))
        self.label_ce.bind("<Button-1>", lambda event, branch_name="CE": self.open_topics_page(branch_name))
        self.label_me.bind("<Button-1>", lambda event, branch_name="ME": self.open_topics_page(branch_name))

        def change_cursor(event):
            event.widget.config(cursor="hand2")

        def reset_cursor(event):
            event.widget.config(cursor="")

        self.label_cse.bind("<Enter>", change_cursor)
        self.label_it.bind("<Enter>", change_cursor)
        self.label_ai.bind("<Enter>", change_cursor)
        self.label_ece.bind("<Enter>", change_cursor)
        self.label_eee.bind("<Enter>", change_cursor)
        self.label_ce.bind("<Enter>", change_cursor)
        self.label_me.bind("<Enter>", change_cursor)

        self.label_cse.bind("<Leave>", reset_cursor)
        self.label_it.bind("<Leave>", reset_cursor)
        self.label_ai.bind("<Leave>", reset_cursor)
        self.label_ece.bind("<Leave>", reset_cursor)
        self.label_eee.bind("<Leave>", reset_cursor)
        self.label_ce.bind("<Leave>", reset_cursor)
        self.label_me.bind("<Leave>", reset_cursor)

        self.back_button = Button(self.homepage, text="Back", bg='#82447A', fg='white', border=0, command=self.go_back)
        self.back_button.pack()
        self.back_button.place(x=10, y=10)

    def open_topics_page(self, branch_name):
        content_page = ContentPage(branch_name)
        content_page.run()
    
    def go_back(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
