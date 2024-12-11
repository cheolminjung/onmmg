
# Register your models here.
from django.contrib import admin
from .models import Post, Comment  # 모델 임포트

# Post 모델 등록
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'likes', 'dislikes', 'grade')  # 표시할 필드
    search_fields = ('content', 'author__username')  # 검색 가능 필드
    list_filter = ('grade', 'author')  # 필터 필드

# Comment 모델 등록
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content', 'likes')  # 표시할 필드
    search_fields = ('content', 'author__username', 'post__content')  # 검색 가능 필드
    list_filter = ('author', 'post')  # 필터 필드
