from tkinter import Toplevel, Frame, Label, Button, Entry, Tk
from tkinter import messagebox
import mysql.connector
from addeventpage import AddEventForm

class EventsPage:
    def __init__(self):
        self.root = Tk()
        self.root.title('EVENTS PAGE')
        self.root.geometry('1000x550+200+75')
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password08",
                database="LearningCurve"
            )
            cursor = db.cursor()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to connect to database: {error}")
            self.root.destroy()
            return

        try:
            cursor.execute("SELECT * FROM events WHERE Date >= CURDATE()")
            events_data = cursor.fetchall()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to fetch events from database: {error}")
            self.root.destroy()
            return

        search_frame = Frame(self.root, bg="black")
        search_frame.pack(pady=10)

        search_label = Label(search_frame, text="Search Events:", bg="black", fg="white", font=("Arial", 12))
        search_label.grid(row=0, column=0, padx=10, pady=5)

        search_entry = Entry(search_frame, bg="white", fg="black", font=("Arial", 12))
        search_entry.grid(row=0, column=1, padx=10, pady=5)

        search_button = Button(search_frame, text="Search", bg='#82447A', fg='white', border=0, command=lambda: self.search_events(search_entry.get(), events_frame))
        search_button.grid(row=0, column=2, padx=10, pady=5)

        events_frame = Frame(self.root, bg="black")
        events_frame.pack(pady=10)

        events_label = Label(events_frame, text="Upcoming Events:", bg="black", fg="white", font=("Arial", 21, "bold"))
        events_label.grid(row=0, column=0, padx=10, pady=5)

        event_headers = ["Sno", "Event Name", "Club Name", "Date", "Time", "Venue"]
        for i, header in enumerate(event_headers):
            header_label = Label(events_frame, text=header, bg="black", fg="white", font=("Arial", 12, "bold"))
            header_label.grid(row=1, column=i, padx=10, pady=5)

        for i, event_data in enumerate(events_data, start=2):
            for j, value in enumerate(event_data):
                label = Label(events_frame, text=value, bg="black", fg="white", font=("Arial", 10))
                label.grid(row=i, column=j, padx=10, pady=5)

        add_event_button = Button(self.root, text="Add Event", bg='#82447A', fg='white', border=0, command=self.add_event_form, font=("Arial", 12))
        add_event_button.pack(pady=10)

        self.back_button = Button(self.root, text="Back", bg='#82447A', fg='white', border=0, command=self.go_back)
        self.back_button.pack()
        self.back_button.place(x=10, y=10)

    def search_events(self, query, events_frame):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password08",
                database="LearningCurve" 
            )
            cursor = db.cursor()
            query = f"%{query}%" 
            cursor.execute("SELECT * FROM events WHERE ClubName LIKE %s OR EventName LIKE %s", (query, query))
            events_data = cursor.fetchall()

            for widget in events_frame.winfo_children():
                widget.destroy()

            event_headers = ["Sno", "Event Name", "Club Name", "Date", "Time", "Venue"]
            for i, header in enumerate(event_headers):
                header_label = Label(events_frame, text=header, bg="black", fg="white", font=("Arial", 12, "bold"))
                header_label.grid(row=1, column=i, padx=10, pady=5)

            for i, event_data in enumerate(events_data, start=2):
                for j, value in enumerate(event_data):
                    label = Label(events_frame, text=value, bg="black", fg="white", font=("Arial", 10))
                    label.grid(row=i, column=j, padx=10, pady=5)
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to search events: {error}")

    def add_event_form(self):
        add_event_form = AddEventForm()

    def go_back(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
