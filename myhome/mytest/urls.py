"""myhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#파일이 다르면 import  해줘야 한다 
from . import views 

#이 파일로 오는 모든 url은 /mytest
urlpatterns = [
    path('', views.index),
    path('gugu/<dan>', views.gugu),
    path('gugu2/<dan>', views.gugu2)

    #http://127.0.0.1:8000/mytest/gugu/3 
    #앞으로 mytest/ 로 시작하는 모든 url은 
    #mytest폴더아래의 urls.py  이 책임진다
    #http://127.0.0.1:8000/mytest/ 
    """
    모든 url 요청은 view가 받아야 하는데 
    게시판 - view 
    게시판2 -  view
    회원가입 - view 
    ......
    /board 
    /board1   또는 /board/1
    /member    
    특정 url이 올 경우 호출될 특정한 뷰는 urls.py 
    """

]
