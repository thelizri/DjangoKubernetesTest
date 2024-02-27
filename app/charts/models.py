from django.db import models
from django.utils import timezone


class SensorData(models.Model):
    packet_number = models.IntegerField()  # Packet counter (reset when S1 is pressed)
    node = models.IntegerField()  # Wireless Sensor Board identifier
    time = models.DateTimeField(auto_now_add=True)
    delta_time = models.DurationField(
        null=True, blank=True
    )  # Time differential between received packets
    rssi = models.FloatField(
        null=True, blank=True
    )  # Received Signal Strength Indicator
    temperature = models.FloatField(null=True, blank=True)  # Temperature (Fahrenheit )
    humidity = models.IntegerField(null=True, blank=True)  # Relative Humidity (%)
    light = models.IntegerField(null=True, blank=True)  # Ambient luminance (Lux)
    external_voltage = models.FloatField(
        null=True, blank=True
    )  # External sensor reading

    def __str__(self):
        local_time = timezone.localtime(self.time)
        return f"Date: {local_time.strftime('%Y-%m-%d %H:%M:%S')}, Packet: {self.packet_number}, Node: {self.node}, Temp: {self.temperature}°F, Humid: {self.humidity}%, Light: {self.light} lx"


from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=SensorData)
def sensor_data_post_save(sender, instance, created, *args, **kwargs):
    if created:  # Only proceed if a new instance was created
        channel_layer = get_channel_layer()
        message = {
            "packet": str(instance),
            "time": instance.time.strftime("%m-%d %H:%M:%S"),
            "temperature": instance.temperature,
            "humidity": instance.humidity,
            "light": instance.light,
        }
        async_to_sync(channel_layer.group_send)(
            "sensor_data", {"type": "sensor_data", "message": message}
        )
