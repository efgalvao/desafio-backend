from django.urls import path
from api.views import TravelVIEW, UpdateTravelVIEW

urlpatterns = [
path('viagem/', TravelVIEW.as_view()),
path('viagem/<int:pk>', UpdateTravelVIEW.as_view() ),
]
