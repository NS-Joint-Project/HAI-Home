from django.urls import path, include
from .views import homefunc

urlpatterns = [
    path('home/', homefunc, name='home'),
]
