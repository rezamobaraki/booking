import requests
from django.urls import reverse


class SearchBooking(object):

    def __init__(self, pick_up_location, drop_off_location, pick_up_date,
                 drop_off_date, time_pick, time_drop):
        self.pick_up_location = pick_up_location
        self.drop_off_location = drop_off_location
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
        url = reverse('core:cities-list')
        response = requests.get('http://127.0.0.1:8000/' + url, {'search': self.pick_up_location})
        json_data = response.json()
        return json_data.get('results')[0].get('latitude'), json_data.get('results')[0].get('longitude')

    def drop_off_location_points(self):
        url = reverse('core:cities-list')
        response = requests.get('http://127.0.0.1:8000/' + url, {'search': self.drop_off_location})
        json_data = response.json()
        return json_data.get('results')[0].get('latitude'), json_data.get('results')[0].get('longitude')
