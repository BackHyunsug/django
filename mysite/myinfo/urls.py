"""mysite URL Configuration

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
from django.urls import path, include 

#bookmark 폴더의 views.py모듈을 가져와라 
#.  같은 패키지 내의  views.py  불러와라 
from . import views 

# http://127.0.0.1:8000/bookmark 
#path함수가 url, 연결할 뷰객체 또는 함수 
urlpatterns = [
    path('', views.index), #http://127.0.0.1:8000/myinfo
    #http://127.0.0.1:8000/myinfo/add/3/4\
    #add/<x>/<y>  이때 x, y 는 views.py  파일 아래에 
    #add의 매개변수가 된다. 
    path('add/<x>/<y>', views.add),
    path('sigma/<num>', views.sigma)
]

#http://127.0.0.1:8000/myinfo/sigma/10