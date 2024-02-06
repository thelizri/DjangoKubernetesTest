from django.urls import path
from .views import Index, PostView, AddPost, EditPost

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("edit_post/<int:pk>", EditPost.as_view(), name="edit_post"),
]
