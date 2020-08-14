from django.contrib import admin
from django.urls import path, include
from . import views 

from guestbook.views import GuestbookLV, GuestbookDV 

urlpatterns = [
   path("", views.index),
    path('list', GuestbookLV.as_view()),
    path('detail/<int:pk>', GuestbookDV.as_view())
]