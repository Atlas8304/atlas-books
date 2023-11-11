from . import views
from django.urls import path

urlpatterns = [path("register", views.register_request, name="register")]
