from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("prometheus/", include("django_prometheus.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("authentication.urls"), name="auth"),
    path("", include("blog.urls"), name="blog"),
    path("charts/", include("charts.urls"), name="charts"),
    path("portfolio/", include("portfolio.urls"), name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
