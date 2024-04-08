from typing import Any

from activities.hugging_face_call import HuggingFaceApi
from .google_third_party_call import GooglePlaces

class RecommendationController:
    def __init__(self, description={} ,location = {}, is_place = False) -> None:
        self.description = description
        self.response_data = None
        self.third_party_instance = None
        self.is_place = is_place
        self.location = location
     
    def call_third_party_methods(self):
        if self.is_place:
            self.third_part_instance = GooglePlaces(self.description, self.location)
            self.third_part_instance()
        else:
            self.third_part_instance = HuggingFaceApi(self.description)
            self.third_part_instance()

        if self.third_part_instance.is_success:
            self.response_data = self.third_part_instance.response_data
        else:
            self.response_data = self.third_part_instance.response_data