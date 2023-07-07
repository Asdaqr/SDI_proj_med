from datetime import datetime as dt
import pickle


# This part of the code is exclusively the back end

class Medicine:
    """Class serves as identifier for the medical thing
    User inputs date, and """

    def __init__(self, name, identifier, date, category, dosage, delta=None, duration=None, schedule=None):
        self.name = name
        self.id = identifier
        self.start = dt.today()
        self.type = category
        self.dosage = dosage
        self.delta = delta
        self.duration = duration
        self.schedule = schedule
        if self.delta is None and self.schedule is None:
            raise Exception("No schedule or delta has been given")


class Medicine_Manager:
    """Controls what medicines are available"""

    def __init__(self):
        self.med_list = []  # insert the medicines by looping over pickl

    def add_med(self, name, identifier, category, dosage, delta, duration, schedule):
        new_med = Medicine(name, identifier, category, dosage, delta, duration, schedule)
        self.med_list.append(new_med)
        self.pickl_save()

    def remove_med(self, name, identifier):
        for med in self.med_list:
            if med.id == identifier:
                self.med_list.remove(med)
                self.pickl_save()

    def pickl_save(self):
        pass

    def get_list(self):
        return self.med_list

