from django.shortcuts import render
from .models import Post

def post_list(request):
    qs=Post.objects.all()
    q=request.GET.get('q','') # 웹으로부터 q를 받아옴. 없다면 공백을 받아옴.
    if q:
        qs=qs.filter(title__icontains=q) 
    return render(request, 'instagram/post_list.html',{
        'post_list':qs,
        'q':q,
    })
    

