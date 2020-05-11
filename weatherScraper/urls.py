from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('weather_query', views.search, name="weatherQuery")
]
