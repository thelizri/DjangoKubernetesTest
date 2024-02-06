from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
