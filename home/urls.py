from django.urls import path, include
from .views import signupfunc, loginfunc, logoutfunc, homefunc, gofunc, backfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('home/', homefunc, name='home'),
    path('go/', gofunc, name='go'),
    path('back/', backfunc, name='back'),
]
