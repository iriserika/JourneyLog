from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_favorites, name='show_favorites'),
    path('add/<int:fk>/', views.add_favorite, name='add_favorite'),
    path('remove/<int:fk>/', views.remove_favorite, name='remove_favorite'),
]
