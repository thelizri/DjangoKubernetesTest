from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import BlogPostForm


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
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    template_name = "edit_blog_post.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
