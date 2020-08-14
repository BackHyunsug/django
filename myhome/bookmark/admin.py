from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

#데코레이터로 등록할때는 Model클래스명 
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'url', 'description')

#admin.site.register(Bookmark, BookmarkAdmin)