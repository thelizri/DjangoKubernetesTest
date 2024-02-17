from django.db import models


class SensorData(models.Model):
    packet_number = models.IntegerField()  # Packet counter (reset when S1 is pressed)
    node = models.IntegerField()  # Wireless Sensor Board identifier*
    tx_id = (
        models.IntegerField()
    )  # The ID number broadcasted by the TX91501 transmitter (factory programmed).
    time = models.DateTimeField(auto_now_add=True)
    delta_time = (
        models.DurationField()
    )  # Time differential between received packets. A separate counter is used for each node
    rssi = (
        models.FloatField()
    )  # Received Signal Strength Indicator – the received signal strength from an RF power source
    temperature = models.FloatField()  # Temperature (Fahrenheit )
    humidity = models.IntegerField()  # Relative Humidity (%)
    light = models.IntegerField()  # Ambient luminance (Lux)
    external_voltage = models.FloatField()  # External sensor reading

    def __str__(self):
        return f"Packet #{self.packet_number} from Node {self.node}"
