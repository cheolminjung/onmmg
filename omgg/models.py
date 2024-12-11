from django.db import models
from django.contrib.auth.models import User


# Create your models here.


from django.db import models
from django.contrib.auth.models import User

# Post 모델
class Post(models.Model):
    # 글 작성자
    author = models.ForeignKey(User,  related_name="posts", null=True, blank=True, on_delete=models.SET_NULL)
    # 사진 필드
    photo1 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    # 본문 내용
    content = models.TextField()
    # 좋아요/싫어요 수
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    # 추가 URL 필드
    additional_url = models.URLField(blank=True, null=True)
    # 주소
    title = models.CharField(max_length=255)
    # 평점
    grade = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"

# Comment 모델
class Comment(models.Model):
    # 댓글 작성자
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="comments")
    # 댓글 내용
    content = models.TextField()
    # 댓글 좋아요 수
    likes = models.PositiveIntegerField(default=0)
    # 참조된 게시물
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"
