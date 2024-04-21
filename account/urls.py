from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:id>/', views.UserView.as_view()),
]
