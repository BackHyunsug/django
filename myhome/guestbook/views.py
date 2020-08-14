from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(requst):
    return HttpResponse("guestbook")

#------------------------ 추가하기 
from django.views.generic import ListView, DetailView 
from guestbook.models import GuestbookModel

class GuestbookLV(ListView):
    model = GuestbookModel #필요최소한 요구사항 
    #guestbookmodel_list.html

class GuestbookDV(DetailView):
    model = GuestbookModel #필요최소한 요구사항 
    #guestbookmodel_detail.html,

#templates/guestbook 아래에 파일 두개 만들기 
