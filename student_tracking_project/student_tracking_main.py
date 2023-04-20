from tkinter import *
import tkinter as tk
from tkinter import messagebox
import student_tracking_func
import student_tracking_gui

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,400) #(Height, Width)
        self.master.maxsize(500,400)
        self.master.title("Student Tracking")
        self.master.configure(bg="#6abab1")

        student_tracking_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
