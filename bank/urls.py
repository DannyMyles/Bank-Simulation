from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.Home ),
    path('account', views.GetAccount),
    path('defaults', views.DefaultAccounts)
]