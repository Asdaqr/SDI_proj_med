import tkinter as tk
import backend
import datetime as dt
import helper
import pickle

root = tk.Tk()
root.geometry("1920x1080")
root.title("Medicine Notifier")
root.resizable(True, True)

# separate root into 3 frames - top, middle, and bottom

top_frame = tk.Frame(root)
main_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)


class DayList:
    def __init__(self, dayofw, frame):
        self.day = dayofw
        self.checklist = tk.Listbox(frame)  # add stylization alter
        self.date = None

    def check_off_item(self):
        self.checklist.delete(tk.ANCHOR)


class MainProgram(backend.Medicine_Manager):
    def __init__(self):
        super().__init__()
        self.dov = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dov_abbr = ['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.', 'Sun.']

        self.days = []

        for i, day in enumerate(self.dov_abbr):
            new_day = DayList(day, main_frame)
            self.days.append(new_day)
            # grid and stylization code go here I'll do it later

# dov = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# dov_abbr = ['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.', 'Sun.']

# days = []

# meds = backend.Medicine_Manager()  # Max, write code that stores the medicine from pickl file in backend
# med_list = meds.get_list()
