from django.db import models

# Create your models here.
class GuestbookModel(models.Model):
    title = models.CharField("제목", max_length=200)
    writer = models.CharField("작성자", max_length=50)
    contents = models.TextField("내용")
    
    def __str__(self):
        return f'{self.title} {self.writer}'
    