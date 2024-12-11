from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'grade',
            'content',

            'additional_url',
            'photo1', 'photo2', 'photo3', 'photo4', 'photo5',
        ]
        labels = {
            'title': '음식점 이름',
            'content': '내용',
            'additional_url': '지도 URL(선택사항)',
            'grade': '평점',
            'photo1': '사진 1',
            'photo2': '사진 2',
            'photo3': '사진 3',
            'photo4': '사진 4',
            'photo5': '사진 5',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '음식점을 평가해주세요',
                'rows': 3
            }),
            'additional_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': '네이버지도 URL이나 음식점 홈페이지 URL을 입력'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '음식점 이름'
            }),
            'grade': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '10점 만점에 몇 점? (소수점 불가)',
                'step': 1,
                'min': 0,
                'max': 10
            }),
            'photo1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control pe-0',  # Bootstrap 클래스 추가
                'placeholder': '댓글을 작성해주세요...'
            }),
        }
        labels = {
            'content': '',  # 레이블 제거
        }