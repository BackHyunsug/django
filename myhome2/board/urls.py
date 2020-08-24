#/myhome2/board/urls.py 
from django.contrib import admin
from django.urls import path 

# . 현재 나와 같은 경로에 있는   views.py 를 import 해라 
from . import views 

app_name = 'board'  # 앱이름 줘야한다. 맨처음 django-admin startapp board 이름

#url와 view를 연결짓는 부분이다. 
urlpatterns = [
    path('', views.list),  #path함수가 url과  view의 함수나 클래스를 
                           #연결시킨다. 
    path('list', views.list, name="board_list"),
    path('view/<int:id>', views.view, name="board_view"),   
    # 최신 : <a href="/board/view/1">제목1</a>         
    # 옛날 : <a href="/board/view?id=1">제목1</a>         
    
]

