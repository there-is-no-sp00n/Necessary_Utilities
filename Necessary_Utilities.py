class Necessary_Utilities():
    def __init__(self):
        pass

    @staticmethod
    def convert_datetime_to_date_list(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0].split('-')                               # only take the date segment and split it by '-'
        date = [int(i) for i in date]                           # list comprehension to typecast the string date elements to int

        return date                                             # return to caller

    @staticmethod
    def convert_datetime_to_string(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0]                                          # only take the date segment
        
        return date
        
