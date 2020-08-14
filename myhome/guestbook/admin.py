from django.contrib import admin

# Register your models here.
from guestbook.models import GuestbookModel

@admin.register(GuestbookModel)
class GuestbookAdmin(admin.ModelAdmin):
    list_display=('title', 'writer', 'contents')

    

    
