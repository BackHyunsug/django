from django.shortcuts import render

# Create your views here.
#함수뷰(점프투장고), 클래스뷰(우리교재)
#제네릭뷰 - 시스템이 만들어 놓은거 중에서 골라서 상속받기 
#목록 - ListView, 상세화면-DetailView

from django.views.generic import ListView, DetailView 
#모델과 연결작업 모델 import 
from bookmark.models import Bookmark 

#뷰클래스를 만든다. - 제네릭뷰를 상속받아야 하고, model 속성에 모델클래스를 
#전달해야 한다 
class BookmarkLV(ListView):
    model = Bookmark #필요최소한 요구사항 
    #테이블 모듀명_모듈명   Bookmark_Bookmark
    #데이터베이스에 가서 model속성에 부여한 Bookmark_Bookmark
    #테이블 데이터를 읽어와서  object_list 변수에 저장하고 
    #templates/bookmark/bookmark_list.html을 호출하는 기능이 숨어있다. 
    
    

class BookmarkDV(DetailView):
    model = Bookmark #필요최소한 요구사항 
