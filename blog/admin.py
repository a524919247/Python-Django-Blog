from django.contrib import admin
from blog.models import BlogType,Blog

@admin.register(BlogType)
class BlogTypeadmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','author','get_read_num','created_time','last_updated_time')

