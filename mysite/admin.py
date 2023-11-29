from django.contrib import admin
from mysite.models import Post, Product, comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Product)
admin.site.register(comment, CommentAdmin)
