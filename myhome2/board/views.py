from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def index(request):
    return HttpResponse("게시판")

#모델클래스를 import 한다 
from .models import Board 


# def list(request):
#     board_list = Board.objects.all()
#     #쿼리셋 - 모델 클래스안에 objects 함수가 있어서 
#     #이 함수를 이용해서 데이터를 가져온다 
#     return render(request, 'board/board_list.html', 
#       {'board_list':board_list})    

#디비에서 가져온 데이터를  tuple->dict 으로 바꾸는 함수 
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    #테이블의 열에대한 정보를 가져와야 한다 
    columns = [ col[0] for col in cursor.description ]
    #간략화한  list 
    return [ dict( zip(columns, row)) for row in cursor.fetchall()]
    #columns = ['id', 'title', 'writer', 'wdate', 'hit', 'contents']
    #((1, '제목1', '작성자', '2020-08-24', 0), )
    #[{'id':'1', 'title':'제목1', ,,,,}

from django.db import connection
def list(request):
    sql = '''
    select id, title, writer, contents, hit, wdate
    from board_board 
    limit 0, 10 
    '''
    #limit  시작위치, 개수 
    cursor = connection.cursor()
    cursor.execute(sql)
    board_list = dictfetchall(cursor)

    context = {'board_list':board_list}
    return render(request, 'board/board_list.html', context)

 # 최신 : <a href="/board/view/1">제목1</a>         
def view(request, id):
    context={'id':id}
    return render(request, 'board/board_view.html', context)