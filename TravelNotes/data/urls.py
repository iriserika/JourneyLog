from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_home_page),
    path(r'signup', views.signup, name='signup'),

]
