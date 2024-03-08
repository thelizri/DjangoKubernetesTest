from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


# Create your views here.
class Index(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date_created"]


class PostView(DetailView):
    model = Post
    template_name = "blog/post.html"


class AddPost(CreateView):
    model = Post
    template_name = "blog/add_blog_post.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    template_name = "blog/edit_blog_post.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePost(DeleteView):
    model = Post
    template_name = "blog/delete_blog_post.html"
    success_url = reverse_lazy("index")
