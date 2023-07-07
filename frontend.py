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

        self.top_frame = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        for i, day in enumerate(self.dov_abbr):
            new_day = DayList(day, self.main_frame)
            self.days.append(new_day)
            # grid and stylization code go here I'll do it later

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
