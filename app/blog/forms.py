from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": CKEditorWidget(attrs={"class": "form-control"}),
        }
