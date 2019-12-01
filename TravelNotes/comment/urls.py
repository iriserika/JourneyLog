from django.urls import path
from . import views

urlpatterns = [
    path('new/<int:fk>/', views.comment_new, name='comment_new'),
    path('edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]