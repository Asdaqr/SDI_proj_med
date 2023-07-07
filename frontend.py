import tkinter as tk
import backend
import datetime as dt
import helper

root = tk.Tk()
root.geometry("1920x1080")


# seperate root into 3 frames - top, middle, and bottom

class day_of_week:
    def __init__(self, day, frame):
        self.day = day
        self.checklist = tk.Listbox(frame)  # add stylization alter

dov = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i,day in enumerate(dov):
    pass
