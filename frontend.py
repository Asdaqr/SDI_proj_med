import tkinter as tk
import backend
import datetime as dt
import helper

root = tk.Tk()
root.geometry("1920x1080")

# separate root into 3 frames - top, middle, and bottom

main_frame = tk.Frame(root)


class DayList:
    def __init__(self, dayofw, frame):
        self.day = dayofw
        self.checklist = tk.Listbox(frame)  # add stylization alter
        self.date = None


dov = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dov_abbr = ['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.', 'Sun.']

days = []

for i, day in enumerate(dov_abbr):
    new_day = DayList(day, main_frame)
    days.append(new_day)
    # grid and stylization code go here i'll do it later


