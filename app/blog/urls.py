from django.urls import path

from . import views

urlpatterns = [
    # TODO: Remove when proper Splash Page Added
    path("", views.Post.as_view(), name="blog"),
    path("blog/", views.Post.as_view(), name="blog"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("blog/new", views.new_post, name="post_new"),
]
