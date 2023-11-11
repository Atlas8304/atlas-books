from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import NewPostForm


class Post(generic.ListView):
    queryset = BlogPost.objects.filter(published_state=1).order_by("-creation_date")
    template_name = "blog/index.html"


class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = "blog/post_focused.html"


@login_required(login_url="/login")
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.slug = obj.title.replace(' ', '-').lower()
            # TODO: Remove after adding Draft review/publish capability
            obj.published_state = 1
            obj.save()
            return redirect("blog")
    form = NewPostForm()
    return render(
        request=request,
        template_name="blog/post_new.html",
        context={"new_post_form": form},
    )
