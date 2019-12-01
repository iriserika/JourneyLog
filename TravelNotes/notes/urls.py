from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('weekend/', views.post_weekend, name='post_weekend'),
    path('short/', views.post_short, name='post_short'),
    path('long/', views.post_long, name='post_long'),
    path('gap/', views.post_gap, name='post_gap'),
]