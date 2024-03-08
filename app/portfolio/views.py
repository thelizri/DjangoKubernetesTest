from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Portfolio


# Create your views here.
def index(request):
    tiles_data = []
    titles = ["Magna", "Lorem"]
    base_image_path = "portfolio/images/pic{:02}.jpg"  # Using string formatting to generate image paths
    description = (
        "Sed nisl arcu euismod sit amet nisi lorem etiam dolor veroeros et feugiat."
    )
    link_url = "generic"

    # Assuming you want to create 12 tiles based on your example
    for i in range(1, 13):
        tile = {
            # "style": "style{}".format(i),
            "title": titles[i % 2],
            "image_url": base_image_path.format(i),
            "description": description,
            "link_url": link_url,
        }
        tiles_data.append(tile)

    return render(request, "portfolio/index.html", {"tiles": tiles_data})


def generic(request):
    return render(request, "portfolio/generic.html")


class ProjectListView(ListView):
    model = Portfolio
    template_name = "portfolio/index.html"


class ProjectDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/detailview.html"
