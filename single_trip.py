import calendar


class SingleTrip:
    date_format = '%d/%m/%Y'

    def __init__(self, date, from_place, to_place, rate, reason, distance_in_km):
        self.__date = date
        self.__from_place = from_place
        self.__to_place = to_place
        self.__rate = rate
        self.__reason = reason
        self.__distance_in_km = distance_in_km

    def __str__(self):
        return self.__date.strftime(SingleTrip.date_format) + '\t' \
               + calendar.day_name[self.__date.weekday()] + '\t' \
               + self.__from_place + '\t' \
               + self.__to_place + '\t' \
               + str(self.__distance_in_km) \
               + '\t' + self.__reason + '\t' \
               + "{0:.2f}".format(self.__rate) \
               + '\t' + "{0:.2f}".format(self.__calculate_trip_money()) \
               + '\t' + '' + '\t'

    def __calculate_trip_money(self):
        return self.__distance_in_km * self.__rate
