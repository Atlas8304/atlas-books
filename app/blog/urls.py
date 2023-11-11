from . import views
from django.urls import path

urlpatterns = [
    path("blog/", views.BlogPostList.as_view(), name="blog"),
    path("<slug:slug>/", views.BlogPostFocused.as_view(), name="post_focused"),
]
