from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog_api.models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Category)
class PostAdmin(ModelAdmin):
    pass
