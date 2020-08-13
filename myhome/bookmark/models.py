from django.db import models

# Create your models here.
# models.Model클래스를 꼭 상속받아야 한다
class Bookmark(models.Model):
    #id-자동으로 이 필드는 만들어 준다 
    title = models.CharField('TITLE', max_length=100, blank=True)
    #varchar, 최대길이 1000, 공백허용
    url = models.URLField('URL', unique=True)
    #unique제약조건 , 중복 데이터 못들어감
    #이 함수는 반드시 오버라이딩 하자 
    def __str__(self): 
        return self.title 
        
"""     
b = Bookmark()
print(b)
print(b.__str__())
"""
#python manage.py sqlmigrate  bookmark 0001
