from django.urls import path,include
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
]
