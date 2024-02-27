from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.utils import timezone
from datetime import timedelta


# Utility function to query all sensor data
def query_all():
    return SensorData.objects.all().order_by("time")


def query_data(days=0, seconds=0, minutes=0, hours=0, weeks=0):
    time = timezone.now() - timedelta(
        days=days,
        seconds=seconds,
        minutes=minutes,
        hours=hours,
        weeks=weeks,
    )
    return SensorData.objects.filter(time__gte=time).order_by("time")


def chart_view(request, queryset):
    # Prepare data for the chart
    time_labels = [data.time.strftime("%m-%d %H:%M:%S") for data in queryset]
    temperatures = [data.temperature for data in queryset]
    humidity = [data.humidity for data in queryset]
    light = [data.light for data in queryset]
    packet_string = [str(data) for data in queryset]

    # Serialize data to JSON format
    time_labels_json = json.dumps(time_labels, cls=DjangoJSONEncoder)
    temperatures_json = json.dumps(temperatures, cls=DjangoJSONEncoder)
    humidity_json = json.dumps(humidity, cls=DjangoJSONEncoder)
    light_json = json.dumps(light, cls=DjangoJSONEncoder)

    # Pass data to the template
    context = {
        "time_labels": time_labels_json,
        "temperatures": temperatures_json,
        "humidity": humidity_json,
        "light": light_json,
        "packet_string": packet_string,
    }
    return render(request, "charts/index.html", context)


# Create your views here.
def index(request):
    queryset = query_all()
    return chart_view(request, queryset)


def data_by_minute(request, minutes=1):
    queryset = query_data(minutes=minutes)
    return chart_view(request, queryset)


def data_by_hour(request, hours=1):
    queryset = query_data(hours=hours)
    return chart_view(request, queryset)


def data_by_day(request, days=1):
    queryset = query_data(days=days)
    return chart_view(request, queryset)


def data_by_week(request, weeks=1):
    queryset = query_data(weeks=weeks)
    return chart_view(request, queryset)


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
