from django.urls import path, include
from .views import signupfunc, loginfunc, homefunc, gofunc, backfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('home/', homefunc, name='home'),
    path('go/', gofunc, name='go'),
    path('back/', backfunc, name='back'),
]
