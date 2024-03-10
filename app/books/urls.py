from django.urls import path

from books.views import BooksView

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="list"),
]