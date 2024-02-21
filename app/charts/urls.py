from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorDataViewSet, index, data_by_hour, data_by_day

router = DefaultRouter()
router.register(r"data", SensorDataViewSet)

urlpatterns = [
    path("", index, name="chart_index"),
    path("<int:hours>/", data_by_hour, name="data_by_hour"),
    path("day/<int:days>/", data_by_day, name="data_by_day"),
    path("api/", include(router.urls)),
]
