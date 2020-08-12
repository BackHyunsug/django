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
from django.urls import path

#bookmark 폴더의 views.py모듈을 가져와라 
from bookmark import views 


#path함수가 url, 연결할 뷰객체 또는 함수 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', views.index),
    #url 이 /bookmark라고 오면 bookmark안의 views라는 
    #파일의 index 함수를 호출하라 

    #http://127.0.0.1:8000/bookmark/test
    path('bookmark/test', views.test),

    #http://127.0.0.1:8000/bookmark/myname

]
