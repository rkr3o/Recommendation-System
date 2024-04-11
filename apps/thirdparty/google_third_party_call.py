import json
import random
import requests
from apps.constant.constant import Recommendation

import requests

class GooglePlaces:
    def __init__(self, description, user_location):
        self.url = Recommendation.ThirdParty.URL
        self.key = Recommendation.ThirdParty.KEY
        self.params = {"query": description, "key": self.key, "location": f"{user_location['lat']},{user_location['lng']}"}
        self.response_data = None
        self.response_json = []
        self.description = description
        self.is_success = False
        self.status_code = None
        self.generate_data = []
    
    def __call__(self):
        self.third_party_call()
        self.process_response()

    def third_party_call(self):
        self.response = requests.get(self.url, params=self.params)
        if self.response.status_code == 200:
            self.status_code = self.response.status_code
            self.response_json = self.response.json().get("results", [])

    def process_response(self):
        if self.status_code == 200:
            self.is_success = True
            self.generate_response_data(self.response_json)
            print(self.generate_data)
            self.response_data = json.dumps(self.generate_data)
            print(self.response_data)
        else:
            if self.status_code == 400:
                self.response_data = {"message": "Bad request. Check your query."}
            elif self.status_code == 403:
                self.response_data = {"message": "API key is invalid or has been disabled."}
            elif self.status_code == 429:
                self.response_data = {"message": "You've exceeded your quota."}
            else:
                self.response_data = {"message": "Unexpected error. Please try again later."}

    def generate_response_data(self, filtered_data):
        for place in filtered_data:
            filtered_place = {
                "name": place.get("name", "Unknown"),
                "address": place.get("formatted_address", "Address not available"),
                "rating": place.get("rating", "Rating not available"),
                "total_ratings": place.get("user_ratings_total", "Total ratings not available"),
                "business_status": place.get("business_status", "Business status not available"),
                "opening_hours": place.get("opening_hours", {}).get("open_now", "Opening hours not available"),
                "types": place.get("types", "Types not available"),
                "photo_reference": place.get("photos", [{}])[0].get("photo_reference", "Photo reference not available"),
                "location": place.get("geometry", {}).get("location", {}),
            }
            self.generate_data.append(filtered_place)
        return self.generate_data

    
             