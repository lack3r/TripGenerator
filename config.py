import json
import datetime
import locale


class Config:

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'el_GR.UTF-8')

        self.output_directory = '.'
        self.months = []
        self.year = ""
        self.rate = 0.0
        self.days_to_exclude = []
        self.trips = []
        self.date_format = '%d/%m/%Y'

    def read(self, file):

        with open(file, encoding='utf8') as config_file:
            config = json.load(config_file)
        self.output_directory = config['OutputDirectory']
        self.months = config['Months']
        self.year = config['Year']
        self.rate = config['Rate']
        public_holidays = list(map(lambda x: x['Date'], config['PublicHolidays']))
        other_days_to_exclude = config['OtherDaysToExclude']
        days_to_exclude = public_holidays + other_days_to_exclude
        self.days_to_exclude = list(map(lambda x: datetime.datetime.strptime(x, '%Y%m%d'), days_to_exclude))
        self.trips = config['Trips']
