from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
#html문서와 데이터를 결합해서 클라이언트에게 보내주는걸 
#렌더링 한다고 한다 
from django.shortcuts import render 
#render  html 문서 + 데이터 결합
# Create your views here.

#html문서에 전달할 데이터를 먼저 만들자 
data ={
    'title':'장고란 무엇인가', 
    'desc': '장고란 파이썬으로 만들어진 웹어플리케이션 프레임워크입니다'
}

#index 함수를 만들자 
def index(request):
    #return HttpResponse("Hello Django")
    #render 세번째 인자가 html 보내는 데이터-dict  타입으로 보낸다. 
    r = render(request, "bookmark/index.html", data )
    return r

#http://127.0.0.1:8000/bookmark/add/5/6
#bookmark/add.html 


def test(request):
    msg = "This is Django Test"
    return HttpResponse(msg)
    
def myname(request):
    msg = "<h1>My name is Tom</h1>"
    return HttpResponse(msg)