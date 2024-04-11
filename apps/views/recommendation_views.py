import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.controller.recommend_activities_controller import RecommendationController


class RecommendActivities(APIView):
    def post(self, request):
        description = request.data.get("description", "")
        location = request.data.get("userLocation", {})
        controller_instance = RecommendationController(
            description, location, is_place=True
        )
        controller_instance.call_third_party_methods()
        response_data = json.loads(controller_instance.response_data)
        return Response(response_data, status=status.HTTP_200_OK)
