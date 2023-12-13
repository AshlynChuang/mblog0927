from django.contrib import admin
from mysite.models import Post, Mood

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'del_pass', 'pub_time', 'enabled')

admin.site.register(Post, PostAdmin)
admin.site.register(Mood)
