from django.db import models

# Create your models here.
# models.Model클래스를 꼭 상속받아야 한다
class Bookmark(models.Model):
    #id-자동으로 이 필드는 만들어 준다 
    #필드명 id, seq - 게시물들을 식별하기 위한 필드를 추가
    title = models.CharField('TITLE', max_length=100, blank=True)
    #varchar, 최대길이 1000, 공백허용
    url = models.URLField('URL', unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    #unique제약조건 , 중복 데이터 못들어감
    #이 함수는 반드시 오버라이딩 하자 
    def __str__(self): 
        return f'{self.title}  {self.url}  {self.description}' 
        
#모델을 만들고 나면, 모델에 대한 정보 -> 쿼리로 makemigrations 
#모델을 수정하고나면 makemigrations  이걸 반드시 -사전작업
#실제로 디비에 반영은 migrate 
#python manage.py makemigrations
#python manage.py migrate

'''
django-admin startproject myhome
myhome
    ㄴ  manage.py
    ㄴ  myhome
    ㄴ  새로운맵1
    ㄴ  새로운맵2

python manage.py makemigration
python manage.py migrate
'''


"""     
b = Bookmark()
print(b)
print(b.__str__())
"""
#python manage.py sqlmigrate  bookmark 0001
# \\192.168.219.120