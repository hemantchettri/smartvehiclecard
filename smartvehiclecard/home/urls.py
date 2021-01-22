from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('login', views.login, name='homepage'),
    path('signup', views.signup, name='homepage'),
    # path('profile', views.profile, name='homepage'),
    # # path('settings', views.settings, name='homepage'),
]
