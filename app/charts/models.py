from django.db import models


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
        return f"Packet #{self.packet_number} from Node {self.node}"
