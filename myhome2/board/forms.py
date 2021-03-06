#board/forms.py

from django import forms
from board.models import Board 

class BoardForms(forms.ModelForm):
    class Meta:
        model = Board 
        fields=['title', 'writer', 'contents']
        labels={
            'title':'제목',
            'writer':'작성자',
            'contents':'내용',
        }