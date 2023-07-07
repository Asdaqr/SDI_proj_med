import tkinter as tk
import backend
import datetime as dt
import helper
import pickle


class DayList:
    def __init__(self, dayofw, frame):
        self.day = dayofw
        self.checklist = tk.Listbox(frame)  # add stylization alter
        self.date = None

    def check_off_item(self):
        self.checklist.delete(tk.ANCHOR)


class MainProgram(backend.MedicineManager):
    def __init__(self):
        super().__init__()
        self.dov = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.dov_abbr = ['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.', 'Sun.']

        self.days = []

        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Medicine Notifier")
        self.root.resizable(True, True)

        # separate root into 3 frames - top, middle, and bottom

        top_frame = tk.Frame(self.root)
        main_frame = tk.Frame(self.root)
        bottom_frame = tk.Frame(self.root)

        for i, day in enumerate(self.dov_abbr):
            new_day = DayList(day, main_frame)
            self.days.append(new_day)
            # grid and stylization code go here I'll do it later

