#파일명 : bookmark/bookmark_urls.py
from django.contrib import admin
from django.urls import path, include

#클래스형 뷰 
from bookmark.views import BookmarkLV, BookmarkDV 

# http://127.0.0.1:8000/bookmark/detail/1
urlpatterns = [
    path('list', BookmarkLV.as_view()),
    path('detail/<int:pk>', BookmarkDV.as_view())
]
