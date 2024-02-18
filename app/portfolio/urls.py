from django.urls import path
from .views import index, generic

urlpatterns = [
    path("", index, name="portfolio_index"),
    path("generic", generic, name="generic"),
]
