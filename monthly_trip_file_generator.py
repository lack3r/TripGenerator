import os
import locale
import datetime
import calendar
from trip_direction import TripDirection
from formatted_line_generator import FormattedLineGenerator


class MonthlyTripFileGenerator:

    def __init__(self, month, year, output_directory):
        locale.setlocale(locale.LC_ALL, 'el_GR.UTF-8')
        self.__month = month
        self.__year = year
        self.__output_file_path = self.__calculate_output_file_path(output_directory)

    def generate_monthly_trip_file(self, config):
        days = self.__calculate_working_days_in_month(config)
        title = self.__create_header()
        output_file = open(self.__output_file_path, 'w', encoding='utf8')
        self.__write_file_content(config, days, output_file, title)
        output_file.close()

    def __calculate_output_file_path(self, output_directory):
        return os.path.expanduser(
            output_directory + '/' + str(self.__year) + '' + f'{self.__month:02}' + '_vivlio_diakinisis.csv')

    def __write_file_content(self, config, days, output_file, title):
        output_file.write(title)
        self.__write_days_in_file(config, days, output_file)

    def __write_days_in_file(self, config, days, output_file):
        for date in days:
            self.__add_go_and_return_rows(config, date, output_file)

    def __calculate_working_days_in_month(self, config):
        first_day_of_the_month = 1
        last_day_of_the_month = calendar.monthrange(self.__year, self.__month)[1]
        start_date = datetime.datetime(self.__year, self.__month, first_day_of_the_month)
        end_date = datetime.datetime(self.__year, self.__month, last_day_of_the_month)
        days = MonthlyTripFileGenerator.__get_days_in_range(start_date, end_date, config.days_to_exclude)
        return days

    @staticmethod
    def __get_days_in_range(start_date, end_date, excluded=None):
        if excluded is None:
            excluded = []
        current_date = start_date
        days = []
        while current_date.date() <= end_date.date():
            if current_date not in excluded:
                days.append(current_date)
            current_date += datetime.timedelta(days=1)
        return days

    @staticmethod
    def __create_header():
        title = 'Ημερομηνία\tΗμέρα\tΑπό\tΠρος\tΧιλιόμετρα\tΣκοπός\tRate/km\tΑποζημίωση\tΣημειώσεις\n'
        return title

    def __add_go_and_return_rows(self, config, date, output_file):
        self.__add_go_line_in_file(config, date, output_file)
        self.__add_return_line_in_file(config, date, output_file)

    def __add_go_line_in_file(self, config, date, output_file):
        self.__add_line_in_file(config, date, TripDirection.GOING, output_file)

    def __add_return_line_in_file(self, config, date, output_file):
        self.__add_line_in_file(config, date, TripDirection.RETURNING, output_file)

    def __add_line_in_file(self, config, date, trip_direction, output_file):
        formatted_row = FormattedLineGenerator.get_formatted_row(date, config.trips, trip_direction, config.rate)
        if formatted_row is not None:
            output_file.write(formatted_row + '\n')
