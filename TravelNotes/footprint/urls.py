from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_footprint),
    path('add_location_to_db', views.add_location)
]
