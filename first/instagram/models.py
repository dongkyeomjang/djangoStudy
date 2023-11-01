from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Profile은 settings.AUTH_USER_MODEL과 1대1 관계. 즉 한 명의 유저는 하나의 프로필만 가질 수 있음
    blog_url = models.URLField(blank=True)

class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Post는 settings.AUTH_USER_MODEL과 1대다 관계. 즉 한 명의 유저는 여러개의 포스팅을 작성할 수 있음
    title = models.CharField(max_length=100, db_index=True) #db_index=True는 db에 인덱스를 만들어줌
    slug = models.SlugField(allow_unicode=True, db_index=True) #slug는 url의 일부분. 한글을 사용할 수 있게 allow_unicode=True
    desc = models.TextField(blank=True) #blank=True는 빈칸을 허용한다는 뜻
    image= models.ImageField(blank=True) #blank=True는 빈칸을 허용한다는 뜻
    comment_count= models.PositiveIntegerField(default=0) #PositiveIntegerField는 양수만 허용한다는 뜻
    tag_set = models.ManyToManyField('Tag', blank=True) #ManyToMany는 다대다 관계를 의미함. Tag는 아래에 정의되어 있음
    is_publish = models.BooleanField(default=False) #BooleanField는 True/False만 허용한다는 뜻
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True는 생성시간을 자동으로 넣어줌
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True는 수정시간을 d자동으로 넣어줌

class Comment(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Comment는 settings.AUTH_USER_MODEL과 1대다 관계. 즉 한 명의 유저는 여러개의 댓글을 달 수 있음
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #Post는 위에 정의되어 있음
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True는 생성시간을 자동으로 넣어줌
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True는 수정시간을 자동으로 넣어줌


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True) #unique=True는 중복을 허용하지 않는다는 뜻