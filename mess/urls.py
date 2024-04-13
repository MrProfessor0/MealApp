from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('mess/', views.MessView.as_view()),
    path('mess/<int:id>/', views.MessView.as_view()),
]
