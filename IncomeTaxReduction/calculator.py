from parser import paser

class calculator:
    def __init__(self, jumin_number, office_start_date, military_started_date, military_end_time):
        p = paser()
        self.jumin_number = p.six_digits_to_datetime(jumin_number)
        self.office_start_date = p.six_digits_to_datetime(office_start_date)
        self.military_started_date = p.six_digits_to_datetime(military_started_date)
        self.military_end_time = p.six_digits_to_datetime(military_end_time)

    def age_at_join(self, datetime):
        pass

    def during_time_in_military(self, datetime):
        pass

    def days_of_age(self, datetime):
        pass

    def Applicability(self):
        pass