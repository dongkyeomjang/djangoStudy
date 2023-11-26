from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404


# ----------------------------------------------List View ----------------------------------------------

# FBV)
# def post_list(request):
#     qs=Post.objects.all()
#     q=request.GET.get('q','') # 웹으로부터 q를 받아옴. 없다면 공백을 받아옴.
#     if q:
#         qs=qs.filter(title__icontains=q) 
#     return render(request, 'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q,
#     })

# CBV 예시 1)
# post_list=ListView.as_view(model=Post)

# CBV 예시 2)
class PostListView(ListView):
    model=Post
    template_name='instagram/post_list.html'

    def get_queryset(self):
        qs=super().get_queryset()
        q=self.request.GET.get('q','')
        if q:
            qs=qs.filter(title__icontains=q)
        return qs
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['q']=self.request.GET.get('q','')
        return context

post_list=PostListView.as_view()

    

# ----------------------------------------------Detail View ----------------------------------------------

# /instagram/
# /instagram/1/
# /instagram/2/
# /instagram/3/

# def post_detail(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     # try:
#     #     post=Post.objects.get(pk=pk) #존재하지 않는다면, Post.DoesNotExist 예외가 발생함.
#     # except:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#     })

post_detail=DetailView.as_view(model=Post)