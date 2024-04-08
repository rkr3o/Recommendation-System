from django.urls import path
from .views import RecommendActivities
 
urlpatterns = [
    path('recommend/', RecommendActivities.as_view(), name='recommend_activities'),
]
