from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_prometheus.models import ExportModelOperationsMixin
from ckeditor.fields import RichTextField


# Create your models here.
class Post(ExportModelOperationsMixin("post"), models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title + " | " + str(self.author)
