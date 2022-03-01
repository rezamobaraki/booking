class SearchBooking(object):

    def __init__(self, pick_up_location, pick_up_location_lat,
                 pick_up_location_long, drop_off_location, drop_off_location_lat,
                 drop_off_location_long, pick_up_date, drop_off_date, time_pick, time_drop
                 ):
        self.pick_up_location = pick_up_location
        self.pick_up_location_long = pick_up_location_long
        self.pick_up_location_lat = pick_up_location_lat
        self.drop_off_location = drop_off_location
        self.drop_off_location_lat = drop_off_location_lat
        self.drop_off_location_long = drop_off_location_long
        self.pick_up_date = pick_up_date
        self.drop_off_date = drop_off_date
        self.time_pick = self.clean_time(time_pick)
        self.time_drop = self.clean_time(time_drop)

    def __str__(self):
        return f"({self.pick_up_location}) => ({self.drop_off_location})"

    @staticmethod
    def clean_time(time):
        time = time.replace('am', '') if 'am' in time else time.replace('pm', '')
        return time

    def pick_up_timestamp(self):
        return f"{self.pick_up_date} {self.time_pick}"

    def drop_off_timestamp(self):
        return f"{self.drop_off_date} {self.time_drop}"

    def pick_up_location_points(self):
        return self.pick_up_location_lat, self.pick_up_location_long

    def drop_off_location_points(self):
        return self.drop_off_location_lat, self.pick_up_location_long

    def get_query_params(self, request):
        pick_up_lat, pick_up_long = self.pick_up_location_points()
        drop_off_lat, drop_off_long = self.drop_off_location_points()
        querystring = {
            "drop_off_datetime": self.drop_off_timestamp(),
            "sort_by": request.data.get('sort_by', "recommended"),
            "pick_up_datetime": self.pick_up_timestamp(),
            "pick_up_latitude": pick_up_lat,
            "from_country": request.data.get('from_country', "it"),
            "locale": request.data.get('locale', "en-gb"),
            "drop_off_latitude": drop_off_lat,
            "drop_off_longitude": pick_up_long,
            "pick_up_longitude": drop_off_long,
            "currency": request.data.get('currency', "USD")
        }
        return querystring

    @classmethod
    def get_headers(cls):
        headers = {
            'x-rapidapi-host': "booking-com.p.rapidapi.com",
            'x-rapidapi-key': "910e503bf3msh01b90ab3b1811d8p15372bjsn7670471df649"
        }
        return headers
