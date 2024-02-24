from django.urls import path
from .views import Index, PostView, AddPost, EditPost, DeletePost

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("add/", AddPost.as_view(), name="add_post"),
    path("edit/<int:pk>", EditPost.as_view(), name="edit_post"),
    path("del/<int:pk>", DeletePost.as_view(), name="delete_post"),
]
