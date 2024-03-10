from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from books.models import Book


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 4)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            template_name="books/list.html",
            context={"page_obj": page_obj, "search_query": search_query}
        )