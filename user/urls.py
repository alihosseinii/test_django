from django.urls import path
from .views import SingupView, LoginView, UserProfileView


urlpatterns = [
    path('singup/', SingupView.as_view(), name="singup"),
    path('login/', LoginView.as_view(), name="login"),
    path('info/', UserProfileView.as_view(), name="info"),
]