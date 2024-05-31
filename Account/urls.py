# from django.contrib
from django.urls import path,include
from Account.views import*

urlpatterns = [
    path('ac/',account),
    path('acde/',account_details),
]