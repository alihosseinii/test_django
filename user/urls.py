from django.urls import path
from .views import SingupView, LoginView


urlpatterns = [
    path('singup/', SingupView.as_view(), name="singup"),
    path('login/', LoginView.as_view(), name="login"),
]