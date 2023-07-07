import tkinter as tk
from tkinter import ttk
import backend
import datetime as dt
import helper
import pickle


class DayList:
    def __init__(self, frame, columns, names):
        self.checklist = ttk.Treeview(frame, columns=columns, show='headings')  # add stylization alter
        self.date = tk.StringVar()

        # loops over both the days and abbreviation, we work with days and display abbreviation
        for day, abbrv in zip(columns, names):
            self.checklist.heading(day, text=abbrv)


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

        self.top_frame = ttk.Frame(self.root)
        self.main_frame = ttk.Frame(self.root)
        self.bottom_frame = ttk.Frame(self.root)

        self.window = DayList(self.main_frame, self.dov_abbr, names=self.dov_abbr)

    def remove_from_list(self, name, med_id):
        self.remove_med(name, med_id)
        pass

    def add_to_list(self, name, identifier, category, dosage, delta, duration, schedule):
        self.add_med(name, identifier, category, dosage, delta, duration, schedule)
        pass

    def change_screen(self):
        pass

    def notify(self):
        pass
