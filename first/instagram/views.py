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

#클래스.as_view()를 통해, 호출 가능한 객체를 생성 및 리턴
post_list=PostListView.as_view()

    

# ----------------------------------------------Detail View ----------------------------------------------

# /instagram/
# /instagram/1/
# /instagram/2/
# /instagram/3/

# view 함수는 무조건 HttpResponse 객체를 리턴해야한다. render함수의 리턴은 HttpResponse이다.
# def post_detail(request,pk):
#     post=get_object_or_404(Post,pk=pk) #앞에가 모델의 pk, 뒤에가 인자로 넘겨받은 pk
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#     })


#클래스.as_view()를 통해 호출 가능한 객체를 생성 및 리턴
#post_detail=DetailView.as_view(model=Post)

class PostDetailView(DetailView):
    model=Post
    pk_url_kwarg='pk'

post_detail=PostDetailView.as_view()