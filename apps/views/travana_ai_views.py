import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.controller.travana_ai_controller import TravanaAiController


class TravanaAi(APIView):
    def post(self, request):
        description = request.data.get("description", "")
        controller_instance = TravanaAiController(description)
        controller_instance()
        response_data = json.loads(controller_instance.response_data)
        return Response(response_data, status=status.HTTP_200_OK)
