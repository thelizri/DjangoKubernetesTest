from django.db import models
from django.urls import reverse


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio-detail-view", kwargs={"pk": self.pk})
