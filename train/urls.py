from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShowTrainList, ShowCity

router = DefaultRouter()
router.register("", ShowTrainList)

router2 = DefaultRouter()
router2.register("", ShowCity)

urlpatterns = [
     path("trains/", include(router.urls)),
     path("city/", include(router2.urls)),
]