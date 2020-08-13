#http://127.0.0.1:8000/bookmark/add/5/6
#bookmark/add.html 

1. bookmark/urls.py  

add/<x>/<y>, 뷰의 함수

2.  bookmark/views.py
add함수 request, x, y  

        dict타입을 하나 만들어서  dict에다가 x, y, 결과 저장해서 
        render 를 이용해서 add.html, dict타입변수 

add.html문서 만들고 
{{키값}}