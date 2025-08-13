import mysql.connector
from tkinter import *
from tkinter import messagebox
import re
from homepage import HomePage

class SignInPage:
    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        self.root.geometry('1000x550+200+75')
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password08",
            database="LearningCurve"
        )

        self.cursor = self.db.cursor()

        self.img = PhotoImage(file='images/login.png')
        self.label_image = Label(self.root, image=self.img, bg='black')
        self.label_image.place(x=10, y=10)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text='Sign-in', fg='purple', bg='white', font=("Microsoft YaHei UI Light", 21))
        heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0, 'end')
        def on_leave(e):
            if self.user.get() == '':
                self.user.insert(0, 'Password')

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        def on_enter(e):
            self.code.delete(0, 'end')
            self.code.config(show='•')
        def on_leave(e):
            if self.code.get() == '':
                self.code.insert(0, 'Password')
                self.code.config(show='')

        self.code = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.code.place(x=30, y=150) 
        self.code.insert(0, 'Password')
        self.code.bind("<FocusIn>", on_enter)
        self.code.bind("<FocusOut>", on_leave)

        Button(self.frame, width=39, pady=7, text='Sign in', bg='#82447A', border=0, command=self.signin).place(x=35, y=204)

        label = Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)

        sign_up = Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#82447A', command=self.open_sign_up_page)
        sign_up.place(x=215, y=270)

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.root.destroy()  
            HomePage().run()
        else:
            messagebox.showerror("Invalid", "Invalid username or password")

    def open_sign_up_page(self):
        from signup_page import SignUpPage
        self.root.destroy()
        SignUpPage(Tk())

