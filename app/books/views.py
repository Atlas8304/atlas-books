from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.db.models import Q

from books.models import Book, Genre, Author


class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        genres = Genre.objects.all()
        authors = Author.objects.all()

        search_query = request.GET.get("q", "")
        filter_author_id = request.GET.get("author", "")
        filter_rating = request.GET.get("rating", "")
        filter_genre_id = request.GET.get("genre", "")
        if search_query:
            books = books.filter(
                Q(title__icontains=search_query)
                | Q(author__first_name__icontains=search_query)
                | Q(author__last_name__icontains=search_query)
            )
        elif filter_author_id or filter_rating or filter_genre_id:
            kwargs = {}
            if filter_author_id:
                kwargs.update({"author__id": filter_author_id})
            if filter_genre_id:
                kwargs.update({"genre__id": filter_genre_id})
            if filter_rating:
                kwargs.update({"rating__gte": filter_rating})
            books = books.filter(**kwargs)
        
        books = books.order_by("title")

        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            template_name="books/list.html",
            context={
                "page_obj": page_obj,
                "search_query": search_query,
                "genres": genres,
                "authors": authors,
            },
        )


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)

        return render(
            request, template_name="books/detail.html", context={"book": book}
        )
