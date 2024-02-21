from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SensorDataViewSet,
    index,
    data_by_hour,
    data_by_day,
    data_by_week,
    data_by_minute,
)

router = DefaultRouter()
router.register(r"data", SensorDataViewSet)

urlpatterns = [
    path("", index, name="chart_index"),
    path("minutes/<int:minutes>/", data_by_minute, name="data_by_minute"),
    path("hours/<int:hours>/", data_by_hour, name="data_by_hour"),
    path("days/<int:days>/", data_by_day, name="data_by_day"),
    path("weeks/<int:weeks>/", data_by_week, name="data_by_week"),
    path("api/", include(router.urls)),
]
