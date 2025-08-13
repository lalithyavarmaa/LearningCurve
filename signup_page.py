import mysql.connector
from tkinter import *
from tkinter import messagebox
import re

class SignUpPage:
    def __init__(self, root):
        self.root = root
        self.root.title('SignUp')
        self.root.geometry('1000x550+200+75')
        self.root.configure(bg='black')
        self.root.resizable(True, True)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password08",
            database="LearningCurve"
        )

        self.cursor = self.db.cursor()

        self.img = PhotoImage(file='images/login.png')
        self.label_image = Label(self.root, image=self.img, border=0, bg='white')
        self.label_image.place(x=10, y=10)

        self.frame = Frame(self.root, width=400, height=400, bg='white')
        self.frame.place(x=500, y=50)

        heading = Label(self.frame, text='Sign up', fg='#82447A', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0, 'end')
        def on_leave(e):
            if self.user.get() == '':
                self.user.insert(0, 'Username')

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
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

        self.code = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind("<FocusIn>", on_enter)
        self.code.bind("<FocusOut>", on_leave)

        def on_enter(e):
            self.confirm_code.delete(0, 'end')
            self.confirm_code.config(show='•')
        def on_leave(e):
            if self.confirm_code.get() == '':
                self.confirm_code.insert(0, 'Confirm Password')
                self.confirm_code.config(show='')

        self.confirm_code = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_code.place(x=30, y=220)
        self.confirm_code.insert(0, 'Confirm Password')
        self.confirm_code.bind("<FocusIn>", on_enter)
        self.confirm_code.bind("<FocusOut>", on_leave)

        Button(self.frame, width=39, pady=7, text='Sign up', bg='#82447A', fg='white', border=0, command=self.signup).place(x=35, y=280)
        label = Label(self.frame, text='Already have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
        label.place(x=60, y=340)

        signin = Button(self.frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#82447A', command=self.open_sign_in_page)
        signin.place(x=200, y=340)

    def signup(self):
        username = self.user.get()
        password = self.code.get()
        confirm = self.confirm_code.get()
        match1 = re.search(r'[0-9][0-9]\w', username)

        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror('Error', 'Username already exists')
            return

        if match1 and match1.start() == 0 and len(username) == 10 and len(password) >= 6 and password == confirm:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.db.commit()
            messagebox.showinfo('Signup', 'Successfully Signed Up')
        else:
            messagebox.showerror('Invalid','Username or Password do not match')

    def open_sign_in_page(self):
        from signin_page import SignInPage
        self.root.destroy()
        SignInPage()
