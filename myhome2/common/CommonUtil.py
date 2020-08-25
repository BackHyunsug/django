#common/CommonUtil.py 
import math 
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    #테이블의 열에대한 정보를 가져와야 한다 
    columns = [ col[0] for col in cursor.description ]
    #간략화한  list 
    return [ dict( zip(columns, row)) for row in cursor.fetchall()]
    #columns = ['id', 'title', 'writer', 'wdate', 'hit', 'contents']
    #((1, '제목1', '작성자', '2020-08-24', 0), )
    #[{'id':'1', 'title':'제목1', ,,,,}

#페이지 담당 클래스 
class CommonPage:
    def __init__(self, totalCount=1, curPage=1, pagesize=10):
        #totalCount - 전체데이터 개수 
        #curPage - 현재 페이지 정보 
        #pagesize - 한페이지에 보여야 할 데이터 개수 
        # << < 1 2 3 4 5 6 7 8 9 10 > >>
        # << < > >>  1 2 3 4 ...     현재페이지/전체페이지 
        # 맨처음페이지, 이전 가능여부, 다음 가능여부, 맨마지막페이지 
        # 1,2,3,4,5, ...  페이지 범위,  다음블럭 시작과 끝 
        self.curPage = curPage
        self.totalCount = totalCount
        #전체 레코드수를 이용해 페이지수를 구한다 
        #전체레코드/pagesize ->  파이썬은 실수가 나옴 45/10=4.5 그러면 5페이지가
        #필요한다. 이때 필요한 함수가 ceil 함수이다. -올림함수 
        # 4.5 를 바로 넘는 정수값을 구하는 함수이다. 
        # 4.0 - 4.1 5
        self.totalPage = math.ceil(self.totalCount/pagesize)

        #블락 시작위치  (1~10, 11~20, 현재페이지가 어떤 블록에 속하는지 계산)
        self.start_index = (self.curPage-1)//10 * 10 + 1 
        #현재페이지가 5페이로 1 ~ 10     5-1//10
        #현재페이지가 13     11~20      13-1/10 ->1 *10 +1 11 
        #현재페이지가 10                10-1//10->0 *10 +1 1
        self.end_index = self.start_index + 10 

        #페이자가 15개   11~20 ==> 11 ~ 15 
        if self.end_index >=self.totalPage:
            self.end_index = self.totalPage+1
        
        if self.curPage >1: #다시 앞으로 이동 가능 
            self.isPrev = True 
            self.previous_page_number = curPage-1 
        else: #앞으로 이동 불가 
            self.isPrev=False 
            self.previous_page_number=1

        if self.curPage==self.totalPage:
            self.isNext=False 
            self.next_page_number = self.curPage
        else:
            self.isNext=True 
            self.next_page_number = self.curPage+1

        self.page_range = range(self.start_index, self.end_index)
        #html페이지에서 range함수 사용불가 만들어서 보내기 

             






