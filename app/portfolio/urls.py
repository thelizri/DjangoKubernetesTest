from django.urls import path
from .views import index, generic, ProjectDetailView, ProjectListView

urlpatterns = [
    path("", ProjectListView.as_view(), name="portfolio_index"),
    path("generic", generic, name="generic"),
    path("proj/<int:pk>", ProjectDetailView.as_view(), name="portfolio-detail-view"),
]
