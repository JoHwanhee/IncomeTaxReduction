import datetime

class paser:
    def six_digits_to_datetime(self, reg_number):
        if len(reg_number) < 0:
            raise ValueError('empty string')

        if len(reg_number) is not 6:
            raise ValueError('string is not suitable length (need 6 digit, ex: 930220 )')

        if not reg_number:
            raise ValueError('empty string')

        if not reg_number.isdecimal():
            raise ValueError('no decimal string')

        year = reg_number[:2]
        month = reg_number[3:4]
        day = reg_number[5:6]

        return datetime.datetime(int(year), int(month), int(day) + 1)