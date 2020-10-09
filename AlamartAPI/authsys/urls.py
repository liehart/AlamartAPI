from django.urls import path

from AlamartAPI.authsys.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]