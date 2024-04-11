from django.urls import path

from apps.views.recommendation_views import RecommendActivities
from apps.views.travana_ai_views import TravanaAi

urlpatterns = [
    path("recommend/", RecommendActivities.as_view(), name="recommend_activities"),
    path("recommend/travana-ai", TravanaAi.as_view(), name="travana_ai"),
]
