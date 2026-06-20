from django.contrib import admin

<<<<<<< HEAD
from .models import Comment, Group, Post
=======
from .models import Post, Group, Comment
>>>>>>> bd37722 (update yatube)


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
