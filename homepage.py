from tkinter import Label, Button, Tk
from PIL import Image, ImageTk
from educationpage import EducationPage
from addcontentpage import AddContentForm
from addeventpage import AddEventForm
from event import EventsPage
class HomePage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Home Page")
        self.root.geometry("1000x550+200+75")
        self.root.configure(bg="black")

        self.setup_ui()

    def setup_ui(self):
        logo_image = Image.open("login.png")
        logo_photo = ImageTk.PhotoImage(logo_image.resize((150, 150))) 
        self.label_logo = Label(self.root, image=logo_photo, bg="black")
        self.label_logo.image = logo_photo
        self.label_logo.grid(row=0, column=0, padx=(250, 0), pady=10)

        self.label_heading = Label(self.root, text="LearningCurve", font=("Californian FB", 36), fg="#82447A", bg="black")
        self.label_heading.grid(row=0, column=1, padx=(0, 0), pady=10)

        self.btn_education = Button(self.root, text="Education", font=("Californian FB", 24), bg="#82447A", fg="white", highlightthickness=0, highlightbackground="#2C3E50", command=self.open_education_page)
        self.btn_education.grid(row=1, column=0, padx=(150, 10), pady=(10, 0), sticky="ew")

        self.btn_add_content = Button(self.root, text="+Add Content", font=("Californian FB", 12), bg="black", fg="#82447A", highlightthickness=0, highlightbackground="#2C3E50", command=self.add_content_form)
        self.btn_add_content.grid(row=1, column=1, padx=(10, 150), pady=(10, 0), sticky="ew")

        self.btn_events = Button(self.root, text="Events", font=("Californian FB", 24), bg="#82447A", fg="white", highlightthickness=0, highlightbackground="#2C3E50", command=self.open_event_page)
        self.btn_events.grid(row=2, column=1, padx=(50, 10), pady=(10, 0), sticky="ew")

        self.btn_add_event = Button(self.root, text="+Add Event", font=("Californian FB", 12), bg="black", fg="#82447A", highlightthickness=0, highlightbackground="#2C3E50",command=self.add_event_form)
        self.btn_add_event.grid(row=2, column=2, padx=(10, 150), pady=(10, 0), sticky="ew")

        self.btn_guidance = Button(self.root, text="Guidance", font=("Californian FB", 24), bg="#82447A", fg="white", highlightthickness=0, highlightbackground="#2C3E50")
        self.btn_guidance.grid(row=3, column=2, padx=(50, 0), pady=(10, 0), sticky="ew")

    def open_education_page(self):
        self.root.destroy()  
        EducationPage().run()

    def add_content_form(self):
        add_content_form = AddContentForm()

    def add_event_form(self):
        add_event_form = AddEventForm()

    def open_event_page(self):
        self.root.destroy()
        EventsPage().run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    homepage = HomePage()
    homepage.run()
