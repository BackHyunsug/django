#myinfo/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is myinfo")

#호출될 함수뷰의 첫번째 인자는 언제나  request
def add(request, x, y):
    s = f"x={x} y={y}  x+y={int(x)+int(y)}"
    return HttpResponse(s)

def sigma(request, num):
    a = int(num)
    s=0
    for i in range(1, a+1):
        s = s+i 
    msg = f"1부터 {num}의 합계는 {s} 이다"    
    return HttpResponse(msg)
    
       



