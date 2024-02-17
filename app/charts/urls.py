from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorDataViewSet, index

router = DefaultRouter()
router.register(r"data", SensorDataViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
]
