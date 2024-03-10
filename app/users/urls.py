from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "users"
urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),#
    path("mylist", login_required(views.MyBooksView.as_view(), login_url="login"), name="mylist"),
    path("<int:book_id>/addtolist", views.add_to_list, name="addtolist"),
]
