'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''


import requests


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

        return time                                             # return to caller

    @staticmethod
    def convert_datetime_to_time_string(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1]                                          # only take the time segment
        
        return time                                             # return to caller

    @staticmethod
    def convert_datetime_return_hour(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        hour = int(time[0])                                     # extract the hour as an int

        return hour                                             # return to caller

    @staticmethod
    def convert_datetime_return_minute(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        minute = int(time[1])                                   # extract the hour as an int

        return minute                                           # return to caller

    @staticmethod
    def convert_datetime_return_second_int(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        second = int(float(time[2]))                            # extract the hour as an int

        return second                                           # return to caller

    @staticmethod
    def convert_datetime_return_second_float(datetime):
        time = str(datetime)                                    # convert datetime data to string
        time = time.split(' ')                                  # seperate the time and date segments
        time = time[1].split(':')                               # only take the time segment and split it by ':'
        second = float(time[2])                                 # extract the hour as an int

        return second                                           # return to caller



    @staticmethod
    def get_ip_continent_code(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            continent_code = js['continentCode']
            return continent_code
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_continent(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            continent = js['continent']
            return continent
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_country_code(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            country_code = js['countryCode']
            return country_code
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_country(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            country = js['country']
            return country
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_region(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            region = js['region']
            return region
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_region_name(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            region_name = js['regionName']
            return region_name
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_city(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            city = js['city']
            return city
        except Exception as e:
            return "Unknown"

    @staticmethod
    def get_ip_zip(ip_address):
        try:
            response = requests.get("http://ip-api.com/json/{}".format(ip_address))
            js = response.json()
            zip = js['zip']
            return zip
        except Exception as e:
            return "Unknown"


'''

Copyright 2021, Aninda Zaman, All rights reserved.

'''