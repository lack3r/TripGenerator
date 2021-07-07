from trip_direction import TripDirection
from single_trip import SingleTrip


class FormattedLineGenerator:

    @staticmethod
    def get_formatted_row(date, trips, direction, rate):
        trip = FormattedLineGenerator.get_trip_based_on_day(date, trips)

        if trip is None:
            return None

        if direction == TripDirection.GOING:
            from_place = trip['From']
            to_place = trip['To']
        else:
            from_place = trip['To']
            to_place = trip['From']

        single_trip = SingleTrip(date, from_place, to_place, rate, trip['Reason'], trip['DistanceInKm'])
        return str(single_trip)

    @staticmethod
    def is_workday(date):
        return 0 <= date.weekday() <= 4

    @staticmethod
    def is_saturday(date):
        return date.weekday() == 5

    @staticmethod
    def is_sunday(date):
        return date.weekday() == 6

    @staticmethod
    def get_trip_based_on_day(date, trips):
        trip = None
        if FormattedLineGenerator.is_workday(date):
            trip = trips['WeekDayTrip']
        elif FormattedLineGenerator.is_saturday(date):
            trip = trips['SaturdayTrip']
        elif FormattedLineGenerator.is_sunday(date):
            trip = trips['SundayTrip']
        return trip
