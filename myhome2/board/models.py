from django.db import models

# Create your models here.
 
#디비 테이블과 연결될 클래스를 만들자 
#반드시 models.Model 클래스를 상속받아야 한다 
class Board(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용")
    wdate = models.DateTimeField("작성일", auto_now=False, auto_now_add=False) 
    writer = models.CharField("작성자", max_length=50) 
    hit = models.IntegerField("조회수")

    #__str__ 함수 overriding 
    def __str__(self):
        return self.title + " " + self.writer 

#모델클래스만들면 python manage.py makemigrations 
#                python manage.py migrate