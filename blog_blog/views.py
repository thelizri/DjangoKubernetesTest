from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.
class Index(ListView):
    model = Post
    template_name = "index.html"
    ordering = ["-date_created"]


class PostView(DetailView):
    model = Post
    template_name = "post.html"


class AddPost(CreateView):
    model = Post
    template_name = "add_blog_post.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
