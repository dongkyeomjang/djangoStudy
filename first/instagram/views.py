from django.shortcuts import render
from .models import Post

def post_list(request):
    qs=Post.objects.all()
    return render(request, 'instagram/post_list.html',{
        'post_list':qs,
    })

