from django.urls import path

from application.auth import RegisterView, LoginToken, LogoutView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginToken.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
