from django.urls import path
from .views import Index, PostView, AddPost

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("add_post/", AddPost.as_view(), name="add_post"),
]
