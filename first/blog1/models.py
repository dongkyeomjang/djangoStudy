from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100) #포스트의 제목은 최대 100자
    content = models.TextField() #내용은 텍스트필드로
    created_at=models.DateTimeField(auto_now_add=True) #생성시간은 자동으로
    updated_at = models.DateTimeField(auto_now=True) #업데이트 시간은 자동으로