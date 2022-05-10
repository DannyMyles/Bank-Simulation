from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.Home ),
    path('account', views.GetAccount),
    path('defaults', views.DefaultAccounts),
    path('deposit', views.Deposit),
    path('withdraw', views.Withdrawal),
    path('transfer', views.Transfer),
    path('importtransactions', views.ImportTransactions),
]