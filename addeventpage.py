import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import datetime

class AddEventForm:
    def __init__(self):
        self.add_event_window = Toplevel()
        self.add_event_window.title("Add Event")
        self.add_event_window.configure(bg="black")
        self.add_event_window.resizable(False, False)
        self.setup_ui()
        self.center_window()

    def center_window(self):
        window_width = 600
        window_height = 400
        screen_width = self.add_event_window.winfo_screenwidth()
        screen_height = self.add_event_window.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.add_event_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    def setup_ui(self):
        padx_value = 20
        pady_value = 10

        event_name_label = Label(self.add_event_window, text="Event Name:", bg="white")
        event_name_label.grid(row=0, column=0, padx=padx_value, pady=pady_value, sticky="we")
        self.event_name_entry = Entry(self.add_event_window, bg="white")
        self.event_name_entry.grid(row=0, column=1, padx=padx_value, pady=pady_value, sticky="we")

        club_name_label = Label(self.add_event_window, text="Club Name:", bg="white")
        club_name_label.grid(row=1, column=0, padx=padx_value, pady=pady_value, sticky="we")
        self.club_name_entry = Entry(self.add_event_window, bg="white")
        self.club_name_entry.grid(row=1, column=1, padx=padx_value, pady=pady_value, sticky="we")

        date_label = Label(self.add_event_window, text="Date (YYYY-MM-DD):", bg="white")
        date_label.grid(row=2, column=0, padx=padx_value, pady=pady_value, sticky="we")
        self.date_entry = Entry(self.add_event_window, bg="white")
        self.date_entry.grid(row=2, column=1, padx=padx_value, pady=pady_value, sticky="we")

        time_label = Label(self.add_event_window, text="Time (HH:MM):", bg="white")
        time_label.grid(row=3, column=0, padx=padx_value, pady=pady_value, sticky="we")
        self.time_entry = Entry(self.add_event_window, bg="white")
        self.time_entry.grid(row=3, column=1, padx=padx_value, pady=pady_value, sticky="we")

        venue_label = Label(self.add_event_window, text="Venue:", bg="white")
        venue_label.grid(row=4, column=0, padx=padx_value, pady=pady_value, sticky="we")
        self.venue_entry = Entry(self.add_event_window, bg="white")
        self.venue_entry.grid(row=4, column=1, padx=padx_value, pady=pady_value, sticky="we")

        add_button = Button(self.add_event_window, text="Add", bg='#82447A', fg='white', border=0, command=self.add_event)
        add_button.grid(row=5, column=0, columnspan=2, padx=padx_value, pady=pady_value, sticky="we")

    def add_event(self):
        event_name = self.event_name_entry.get()
        club_name = self.club_name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        venue = self.venue_entry.get()

        try:
            event_date = datetime.strptime(date, '%Y-%m-%d')
            current_date = datetime.now()
            if event_date < current_date:
                messagebox.showerror("Error", "Event date cannot be in the past.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password08",
                database="LearningCurve" 
            )

            cursor = db.cursor()

            insert_query = "INSERT INTO events (EventName, ClubName, Date, Time, Venue) VALUES (%s, %s, %s, %s, %s)"

            event_data = (event_name, club_name, date, time, venue)

            cursor.execute(insert_query, event_data)

            db.commit()

            cursor.close()
            db.close()

            messagebox.showinfo("Success", "Event added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add event: {error}")

if __name__ == "__main__":
    root = Tk()
    add_event_form = AddEventForm(root)
    root.mainloop()
