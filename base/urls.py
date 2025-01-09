from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cards_list'),
    path('update_card/<str:pk>/', views.updateCard, name="update_card"),
    path('delete/<str:pk>/', views.deleteCard, name="delete"),
]
