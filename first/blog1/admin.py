from django.contrib import admin
from.models import Post #현재 디렉토리에 있는 models.py에서 Post를 import

admin.site.register(Post) #admin 사이트에 Post를 등록