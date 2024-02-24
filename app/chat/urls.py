from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="chat_index"),
    path("<str:room_name>/", views.room_view, name="chat_room"),
]
