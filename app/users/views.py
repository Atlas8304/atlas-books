from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator

from .forms import RegisterUserForm
from .models import UserReadingList


def register_request(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUserForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="users/login.html",
        context={"login_form": form},
    )


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def add_to_list(request, book_id):
    if request.method == "POST":
        user_list = UserReadingList.objects.get(user=request.user)
        user_list.books.add(book_id)
    return redirect(f"/books/{book_id}")

class MyBooksView(View):
    def get(self, request):
        books = UserReadingList.objects.get(user=request.user).books.all()
        search_query = request.GET.get("q", "")
        if search_query:
            books = books.filter(
                Q(title__icontains=search_query)
                | Q(author__first_name__icontains=search_query)
                | Q(author__last_name__icontains=search_query)
            )

        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            template_name="users/user_reading_list.html",
            context={"page_obj": page_obj, "search_query": search_query},
        )