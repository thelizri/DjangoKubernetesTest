from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("prometheus/", include("django_prometheus.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("authentication.urls"), name="auth"),
    path("", include("blog.urls"), name="blog"),
    path("charts/", include("charts.urls"), name="charts"),
    path("portfolio/", include("portfolio.urls"), name="portfolio"),
]
