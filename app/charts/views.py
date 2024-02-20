from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.
def index(request):
    # Fetch sensor data
    queryset = SensorData.objects.all().order_by("time")

    # Prepare data for the chart
    time_labels = [data.time.strftime("%Y-%m-%d %H:%M:%S") for data in queryset]
    temperatures = [data.temperature for data in queryset]
    humidity = [data.humidity for data in queryset]
    light = [data.light for data in queryset]
    packet_number = [data.packet_number for data in queryset]

    # Serialize data to JSON format
    time_labels_json = json.dumps(time_labels, cls=DjangoJSONEncoder)
    temperatures_json = json.dumps(temperatures, cls=DjangoJSONEncoder)
    humidity_json = json.dumps(humidity, cls=DjangoJSONEncoder)
    light_json = json.dumps(light, cls=DjangoJSONEncoder)
    packet_number_json = json.dumps(packet_number, cls=DjangoJSONEncoder)

    # Pass data to the template
    context = {
        "time_labels": time_labels_json,
        "temperatures": temperatures_json,
        "humidity": humidity_json,
        "light": light_json,
        "packet_number": packet_number_json,
    }
    return render(request, "charts/index.html", context)


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
