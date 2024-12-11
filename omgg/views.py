from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm, CommentForm
from .models import Post, Comment  # Post와 Comment 모델 임포트


def index(request):
    if request.method == 'POST':
        if 'post_form' in request.POST:  # Post 작성 폼에서 요청이 온 경우
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                # 로그인된 사용자는 request.user, 아니면 None으로 저장
                post.author = request.user if request.user.is_authenticated else None
                post.save()
                return redirect('index')  # 저장 후 리다이렉트

        elif 'comment_form' in request.POST:  # Comment 작성 폼에서 요청이 온 경우
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                # 로그인된 사용자는 request.user, 아니면 None으로 저장
                comment.author = request.user if request.user.is_authenticated else None
                comment.post_id = request.POST.get('post_id')  # 숨겨진 필드로 전달된 post_id 활용
                comment.save()
                return redirect('index')  # 저장 후 리다이렉트
    else:  # GET 요청 처리
        # 모든 Post 객체를 가져오기
        posts = Post.objects.all().order_by('-id')  # 최신 Post가 먼저 보이도록 정렬
        for post in posts:
            post.photos = [photo for photo in [post.photo1, post.photo2, post.photo3, post.photo4, post.photo5] if
                           photo]

        form = PostForm()
        comment_form = CommentForm()

        # posts를 템플릿에 전달
        return render(request, 'index.html', {
            'posts': posts,
            'form': form,
            'comment_form': comment_form
        })