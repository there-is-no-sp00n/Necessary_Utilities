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
    def convert_datetime_to_date_string(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0]                                          # only take the date segment
        
        return date

    @staticmethod
    def convert_datetime_return_year(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0].split('-')                               # only take the date segment and split it by '-'
        year = int(date[0])                                     # extract the year as an int

        return year                                             # return to caller

    @staticmethod
    def convert_datetime_return_month(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0].split('-')                               # only take the date segment and split it by '-'
        month = int(date[1])                                    # extract the month as an int

        return month                                            # return to caller

    @staticmethod
    def convert_datetime_return_day(datetime):
        date = str(datetime)                                    # convert datetime data to string
        date = date.split(' ')                                  # seperate the time and date segments
        date = date[0].split('-')                               # only take the date segment and split it by '-'
        day = int(date[2])                                      # extract the year as an int

        return day                                              # return to caller
        
    @staticmethod
    def convert_datetime_to_time_list(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'

        return time

    @staticmethod
    def convert_datetime_to_time_string(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1]                                          # only take the time segment
        
        return time

    @staticmethod
    def convert_datetime_return_hour(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        hour = int(time[0])                                     # extract the hour as an int

        return hour

    @staticmethod
    def convert_datetime_return_minute(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        minute = int(time[1])                                   # extract the hour as an int

        return minute

    @staticmethod
    def convert_datetime_return_second_int(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        second = int(float(time[2]))                                   # extract the hour as an int

        return second

    @staticmethod
    def convert_datetime_return_second_float(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        second = float(time[2])                                 # extract the hour as an int

        return second