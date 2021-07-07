import locale
from config import Config
from monthly_trip_file_generator import MonthlyTripFileGenerator

locale.setlocale(locale.LC_ALL, 'el_GR.UTF-8')

config = Config()
config.read('vivlio_diakinisis_config.json')

for month in config.months:
    monthly_trip_file_generator = MonthlyTripFileGenerator(month, config.year, config.output_directory)
    monthly_trip_file_generator.generate_monthly_trip_file(config)


