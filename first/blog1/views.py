from django.shortcuts import render
from .models import Post

def post_list(request): #어떤 요청이 왔을때 호출되는 함수
    qs=Post.objects.all() #QuerySet. 요청이 들어오면, 데이터베이스로부터 모든 포스팅을 가져옴
    return render(request,'blog1/post_list.html',{
        'post_list':qs, #DB로부터 가져온 모든 포스팅을 템플릿에 전달
    })
