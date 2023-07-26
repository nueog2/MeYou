from django.contrib import admin
from .models import MainContent, Comment , CartItem , Cart

# Register your models here.

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date','photo','price']
    search_fields = ['title']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','product','quantity']



admin.site.register(MainContent,MainContentAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(CartItem,CartItemAdmin)
