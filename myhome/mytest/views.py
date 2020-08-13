from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

#이 함수는 호출자가 장고, 장고가 첫번째 인자는 
#무조건 request 다 
def index(request):
    return HttpResponse("<h1>This is my Home</h1>")

#서버실행 : c:/django_workspace/myhome>python manage.py runserver 
#(mysite2) C:\django_workspace\myhome> python manage.py runserver 

def gugu(request, dan):
    """
    for i in range(1, 10):
        print( "{} X {} = {}", dan, i, dan*i)
    """
    dan = int(dan) #파라미터가  str로 온다. int 로 강제 형전환

    result="" #클라이언트로 보내기 위한 전체 문장 
    for i in range(1, 10):
        s = "{} X {} = {}".format(dan, i, dan*i)
        result = result + s + "\n"  
        # \n-라인브레이크 -> <br>

    # result = """
    #   3 X 1 = 3 <br> 
    #   3 X 2 = 6 <br>
    #   3 X 3 = 9 <br> ....
    # """    
    #return HttpResponse(result)\
   
    data = {'dan':dan, 'result':result}
    return render(request, "mytest/gugu.html", data)

#html파일에서 곱셈 어렵다. 
def gugu2(request, dan):
    return render(request, "mytest/gugu2.html", 
        {'dan':dan, 'range':range(1,10)} )



