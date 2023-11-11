from django.views import generic
from .models import BlogPost


class Post(generic.ListView):
    queryset = BlogPost.objects.filter(published_state=1).order_by("-creation_date")
    template_name = "blog/index.html"


class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = "blog/post_focused.html"
