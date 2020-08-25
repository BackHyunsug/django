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
from common.CommonUtil import dictfetchall, CommonPage

from django.db import connection
def list(request):
    """
    1. 전체 레코드 개수를 구한다. 
    select count(*) from board_board
    2. 해당페이지 정보를 얻는다
    3. 페이징 객체를 만들어서 html 페이지에 전달한다 
     
    4. 페이지에 해당하는 데이터를 가져와서  html페이지에 전달한다 
    """ 
    cursor = connection.cursor()
    #1.전체 레코드 개수 구하기 
    sql = "select count(*) from board_board"
    cursor.execute(sql)
    totalCount = int(cursor.fetchone()[0]) #첫번째값 가져오기 
    #http://127.0.0.1:8000/board/list?page=1
    #http://127.0.0.1:8000/board/list
    curPage = int(request.GET.get('page', '1'))
    #앞에 page가 값이 없을때 기본값을 줄 수 있다 
    #curPage = request.GET['page']
    
    commonPage = CommonPage(totalCount, curPage, 10)
    #데이터 가져올 위치값 
    start = (curPage-1)*10 

    sql = f'''
    select id, title, writer, contents, hit, wdate
    from board_board 
    order by id desc
    limit {start}, 10 
    '''
    #limit  시작위치, 개수 
    
    cursor.execute(sql)
    board_list = dictfetchall(cursor)

    context = {'board_list':board_list, 'commonPage':commonPage}
    return render(request, 'board/board_list.html', context)

 # 최신 : <a href="/board/view/1">제목1</a>         
def view(request, id):
    cursor = connection.cursor()
    #읽을 글 조회수 증가 
    sql = f"update board_board set hit=hit+1 where id={id}"
    cursor.execute(sql)

    sql = f"""
    select id, title, writer, contents, hit, wdate 
    from board_board
    where id={id}
    """
    cursor.execute(sql)
    board_item = dictfetchall(cursor)

    #여분의 부가적인 정보를 dict 타입으로 들고 다니면 된다. 
    context={'id':id, 'board_item':board_item[0]}
    return render(request, 'board/board_view.html', context)

from .forms import BoardForms
def write(request):
    form = BoardForms() # form 객체를 만든다 
    return render(request, 'board/board_write.html', 
    {'form':form})

from django.utils import timezone 
from django.shortcuts import redirect 
def save(request):

    form = BoardForms(request.POST)
    board = form.save(commit=False)
    #commit=False 속성을 안주면  form 객체에서 바로 디비로 저장 
    #중간에 가로채서 작업을 해야하는데  form객체가 모델객체를 만들어서 
    #반환만 하도록 
    #board객체에  form 에 있는 값들을 모두 전달받는다 

    board.wdate = timezone.now()
    board.hit=0 
    board.save() #연결된 디비에 등록을 자동으로 한다 

    #등록후 리스트 페이지로 이동시킨다 
    return redirect('board:board_list')
